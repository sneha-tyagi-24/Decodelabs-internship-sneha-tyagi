import tkinter as tk
from tkinter import messagebox, ttk
import json, os, re, hashlib, hmac, secrets

USERS_FILE = "users.json"
MIN_STRENGTH_REQUIRED = 3  # scale 0..5

# Hashing settings - PBKDF2 is deliberately slow, unlike plain SHA-256,
# which makes brute-forcing much more expensive for an attacker.
HASH_ALGO = "sha256"
PBKDF2_ITERATIONS = 200_000
SALT_BYTES = 16


# ---------- Helper Functions ----------
def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}


def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)


def hash_password(password: str, salt: bytes = None):
    # Generate a fresh random salt if one wasn't passed in (i.e. new signup).
    if salt is None:
        salt = secrets.token_bytes(SALT_BYTES)

    pwd_hash = hashlib.pbkdf2_hmac(
        HASH_ALGO,
        password.encode("utf-8"),
        salt,
        PBKDF2_ITERATIONS
    )
    return salt.hex(), pwd_hash.hex()


def verify_password(password: str, salt_hex: str, stored_hash_hex: str) -> bool:
    salt = bytes.fromhex(salt_hex)
    _, check_hash_hex = hash_password(password, salt)

    # Constant-time comparison helps reduce timing-attack information leakage.
    return hmac.compare_digest(check_hash_hex, stored_hash_hex)


def contains_username(password: str, username: str) -> bool:
    return username.strip() != "" and username.lower() in password.lower()


def is_sequence(s: str) -> bool:
    if len(s) < 3:
        return False

    if s.isdigit():
        diffs = [int(s[i + 1]) - int(s[i]) for i in range(len(s) - 1)]
    elif s.isalpha():
        chs = [ord(ch.lower()) for ch in s]
        diffs = [chs[i + 1] - chs[i] for i in range(len(chs) - 1)]
    else:
        return False

    return all(d == 1 for d in diffs) or all(d == -1 for d in diffs)


def has_sequential_substring(password: str, min_len: int = 3) -> bool:
    n = len(password)

    for L in range(min_len, n + 1):
        for i in range(0, n - L + 1):
            sub = password[i:i + L]
            if sub.isdigit() or sub.isalpha():
                if is_sequence(sub):
                    return True

    return False


def password_strength(password: str):
    score, reasons = 0, []

    if len(password) >= 8:
        score += 1
    else:
        reasons.append("≥ 8 chars")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        reasons.append("lowercase")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        reasons.append("uppercase")

    if re.search(r"\d", password):
        score += 1
    else:
        reasons.append("digit")

    if re.search(r"[^\w\s]", password):
        score += 1
    else:
        reasons.append("special char")

    return score, reasons


# ---------- GUI ----------
class App:
    def __init__(self, root):
        self.root = root
        root.title("Login & Password Checker")
        root.geometry("550x480")
        root.resizable(False, False)

        self.users = load_users()

        # ===== Signup Frame =====
        signup = tk.LabelFrame(root, text="Sign Up", padx=10, pady=10)
        signup.place(x=10, y=10, width=530, height=240)

        tk.Label(signup, text="Username:").grid(row=0, column=0, sticky="w")
        self.su_username = tk.Entry(signup, width=30)
        self.su_username.grid(row=0, column=1, pady=4)

        tk.Label(signup, text="Password:").grid(row=1, column=0, sticky="w")
        self.su_password = tk.Entry(signup, width=30, show="*")
        self.su_password.grid(row=1, column=1, pady=4)
        self.su_password.bind("<KeyRelease>", self.on_password_type)

        self.show_pwd_var = tk.IntVar()
        tk.Checkbutton(
            signup,
            text="Show Password",
            variable=self.show_pwd_var,
            command=self.toggle_password
        ).grid(row=1, column=2, padx=5)

        tk.Label(signup, text="Confirm Password:").grid(
            row=2, column=0, sticky="w"
        )
        self.su_confirm = tk.Entry(signup, width=30, show="*")
        self.su_confirm.grid(row=2, column=1, pady=4)

        # Strength meter
        self.strength_label = tk.Label(signup, text="Strength: ")
        self.strength_label.grid(row=3, column=0, sticky="w", pady=(6, 0))

        self.strength_bar = ttk.Progressbar(
            signup, length=200, maximum=5
        )
        self.strength_bar.grid(
            row=3, column=1, pady=(6, 0), sticky="w"
        )

        self.su_feedback = tk.Label(
            signup, text="", justify="left", fg="gray"
        )
        self.su_feedback.grid(
            row=4, column=0, columnspan=3, sticky="w"
        )

        tk.Button(
            signup, text="Sign Up", command=self.sign_up
        ).grid(row=5, column=1, pady=8, sticky="e")

        # ===== Login Frame =====
        login = tk.LabelFrame(root, text="Login", padx=10, pady=10)
        login.place(x=10, y=260, width=530, height=150)

        tk.Label(login, text="Username:").grid(row=0, column=0, sticky="w")
        self.li_username = tk.Entry(login, width=30)
        self.li_username.grid(row=0, column=1, pady=4)

        tk.Label(login, text="Password:").grid(row=1, column=0, sticky="w")
        self.li_password = tk.Entry(login, width=30, show="*")
        self.li_password.grid(row=1, column=1, pady=4)

        self.show_login_var = tk.IntVar()
        tk.Checkbutton(
            login,
            text="Show Password",
            variable=self.show_login_var,
            command=self.toggle_login_password
        ).grid(row=1, column=2, padx=5)

        tk.Button(
            login, text="Login", command=self.login
        ).grid(row=2, column=1, pady=8, sticky="e")

        tk.Label(
            root,
            text=(
                "Note: Password must be strong, not include username, "
                "and avoid sequences like 'abc' or '123'."
            ),
            fg="blue"
        ).place(x=12, y=420)

    # ---------- Events ----------
    def toggle_password(self):
        show = "" if self.show_pwd_var.get() else "*"
        self.su_password.config(show=show)
        self.su_confirm.config(show=show)

    def toggle_login_password(self):
        self.li_password.config(
            show="" if self.show_login_var.get() else "*"
        )

    def on_password_type(self, event=None):
        pwd = self.su_password.get()
        score, reasons = password_strength(pwd)

        if has_sequential_substring(pwd):
            reasons.append("avoid sequences")

        self.strength_label.config(text=f"Strength: {score}/5")
        self.strength_bar["value"] = score

        self.su_feedback.config(
            text=(
                "Improve: " + ", ".join(reasons)
                if reasons else "Good password!"
            )
        )

    def sign_up(self):
        username = self.su_username.get().strip()
        password = self.su_password.get()
        confirm = self.su_confirm.get()

        if not username:
            messagebox.showwarning(
                "Invalid", "Username cannot be empty."
            )
            return

        if password != confirm:
            messagebox.showwarning(
                "Mismatch", "Passwords do not match."
            )
            return

        if contains_username(password, username):
            messagebox.showwarning(
                "Invalid", "Password must not contain username."
            )
            return

        if has_sequential_substring(password):
            messagebox.showwarning(
                "Invalid", "Password contains sequential substring."
            )
            return

        score, reasons = password_strength(password)

        if score < MIN_STRENGTH_REQUIRED:
            messagebox.showwarning(
                "Weak",
                f"Strength {score}/5. Improve: {', '.join(reasons)}"
            )
            return

        if username in self.users:
            messagebox.showwarning(
                "Exists", "Username already exists."
            )
            return

        # Store salt + derived hash instead of a raw password or plain SHA-256.
        salt_hex, hash_hex = hash_password(password)

        self.users[username] = {
            "salt": salt_hex,
            "hash": hash_hex,
            "algo": HASH_ALGO,
            "iterations": PBKDF2_ITERATIONS,
        }

        save_users(self.users)

        messagebox.showinfo(
            "Success", "Account created successfully!"
        )

        self.su_username.delete(0, tk.END)
        self.su_password.delete(0, tk.END)
        self.su_confirm.delete(0, tk.END)
        self.strength_label.config(text="Strength: ")
        self.strength_bar["value"] = 0
        self.su_feedback.config(text="")

    def login(self):
        username = self.li_username.get().strip()
        password = self.li_password.get()

        if not username or not password:
            messagebox.showwarning(
                "Invalid", "Enter both username and password."
            )
            return

        record = self.users.get(username)

        if record is None:
            messagebox.showerror(
                "Failed", "No such user. Please sign up."
            )
            return

        if verify_password(
            password, record["salt"], record["hash"]
        ):
            messagebox.showinfo(
                "Welcome",
                f"Login successful. Welcome, {username}!"
            )
            self.li_username.delete(0, tk.END)
            self.li_password.delete(0, tk.END)
        else:
            messagebox.showerror(
                "Failed", "Wrong password."
            )


# ---------- Run ----------
if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
