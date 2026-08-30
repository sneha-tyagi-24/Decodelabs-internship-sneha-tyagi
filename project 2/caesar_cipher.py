import tkinter as tk
from tkinter import ttk, messagebox


# ----------------------------
# Core Cryptographic Logic
# ----------------------------
def caesar_shift(text: str, shift: int, encrypt: bool = True) -> str:
    """
    Shift each alphabetic character by `shift` positions.
    Non-alphabetic characters are left unchanged.
    """
    if not encrypt:
        shift = -shift

    result = []
    for char in text:
        if char.isupper():
            base = ord("A")
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(new_char)
        elif char.islower():
            base = ord("a")
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(new_char)
        else:
            result.append(char)

    return "".join(result)


def encrypt_text(plaintext: str, shift: int) -> str:
    return caesar_shift(plaintext, shift, encrypt=True)


def decrypt_text(ciphertext: str, shift: int) -> str:
    return caesar_shift(ciphertext, shift, encrypt=False)


# ----------------------------
# GUI Application
# ----------------------------
class CaesarCipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DecodeLabs | Caesar Cipher Tool")
        self.root.geometry("560x520")
        self.root.resizable(False, False)
        self.root.configure(bg="#eef3ee")

        self._build_ui()

    def _build_ui(self):
        pad = {"padx": 15, "pady": 6}

        title = tk.Label(
            self.root,
            text="🔒 Caesar Cipher — Encrypt & Decrypt",
            font=("Segoe UI", 16, "bold"),
            bg="#eef3ee",
            fg="#3f5f3f",
        )
        title.pack(pady=(15, 5))

        subtitle = tk.Label(
            self.root,
            text="Project 2: Basic Encryption & Decryption",
            font=("Segoe UI", 10),
            bg="#eef3ee",
            fg="#5a7a5a",
        )
        subtitle.pack(pady=(0, 10))

        input_frame = tk.LabelFrame(
            self.root,
            text="Input Text",
            bg="#eef3ee",
            font=("Segoe UI", 10, "bold"),
            fg="#3f5f3f",
        )
        input_frame.pack(fill="x", **pad)

        self.input_text = tk.Text(
            input_frame, height=4, width=60, font=("Consolas", 11)
        )
        self.input_text.pack(padx=10, pady=10)

        key_frame = tk.Frame(self.root, bg="#eef3ee")
        key_frame.pack(fill="x", **pad)

        tk.Label(
            key_frame,
            text="Shift Key (1-25):",
            bg="#eef3ee",
            font=("Segoe UI", 10, "bold"),
            fg="#3f5f3f",
        ).pack(side="left")

        self.shift_var = tk.StringVar(value="3")
        shift_entry = ttk.Spinbox(
            key_frame,
            from_=1,
            to=25,
            textvariable=self.shift_var,
            width=5,
        )
        shift_entry.pack(side="left", padx=10)

        btn_frame = tk.Frame(self.root, bg="#eef3ee")
        btn_frame.pack(pady=10)

        encrypt_btn = tk.Button(
            btn_frame,
            text="🔐 Encrypt",
            width=15,
            bg="#4a7a4a",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            command=self.handle_encrypt,
        )
        encrypt_btn.grid(row=0, column=0, padx=10)

        decrypt_btn = tk.Button(
            btn_frame,
            text="🔓 Decrypt",
            width=15,
            bg="#7a9a4a",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            command=self.handle_decrypt,
        )
        decrypt_btn.grid(row=0, column=1, padx=10)

        clear_btn = tk.Button(
            btn_frame,
            text="🧹 Clear",
            width=15,
            bg="#c9c9c9",
            fg="black",
            font=("Segoe UI", 10, "bold"),
            command=self.handle_clear,
        )
        clear_btn.grid(row=0, column=2, padx=10)

        enc_frame = tk.LabelFrame(
            self.root,
            text="Encrypted Output (Ciphertext)",
            bg="#eef3ee",
            font=("Segoe UI", 10, "bold"),
            fg="#3f5f3f",
        )
        enc_frame.pack(fill="x", **pad)

        self.encrypted_text = tk.Text(
            enc_frame,
            height=3,
            width=60,
            font=("Consolas", 11),
            bg="#f5f5f5",
        )
        self.encrypted_text.pack(padx=10, pady=10)

        dec_frame = tk.LabelFrame(
            self.root,
            text="Decrypted Output (Plaintext)",
            bg="#eef3ee",
            font=("Segoe UI", 10, "bold"),
            fg="#3f5f3f",
        )
        dec_frame.pack(fill="x", **pad)

        self.decrypted_text = tk.Text(
            dec_frame,
            height=3,
            width=60,
            font=("Consolas", 11),
            bg="#f5f5f5",
        )
        self.decrypted_text.pack(padx=10, pady=10)

    # ----------------------------
    # Event Handlers
    # ----------------------------
    def _get_shift(self):
        try:
            shift = int(self.shift_var.get())
            if not (1 <= shift <= 25):
                raise ValueError
            return shift
        except ValueError:
            messagebox.showerror(
                "Invalid Key",
                "Shift key must be an integer between 1 and 25.",
            )
            return None

    def handle_encrypt(self):
        shift = self._get_shift()
        if shift is None:
            return

        plaintext = self.input_text.get("1.0", tk.END).rstrip("\n")
        if not plaintext:
            messagebox.showwarning(
                "Empty Input",
                "Please enter some text to encrypt.",
            )
            return

        ciphertext = encrypt_text(plaintext, shift)

        self.encrypted_text.delete("1.0", tk.END)
        self.encrypted_text.insert(tk.END, ciphertext)

        self.decrypted_text.delete("1.0", tk.END)
        self.decrypted_text.insert(tk.END, decrypt_text(ciphertext, shift))

    def handle_decrypt(self):
        shift = self._get_shift()
        if shift is None:
            return

        ciphertext = self.encrypted_text.get("1.0", tk.END).rstrip("\n")
        if not ciphertext:
            messagebox.showwarning(
                "Empty Input",
                "Encrypted box is empty. Encrypt some text first, "
                "or paste ciphertext there directly.",
            )
            return

        plaintext = decrypt_text(ciphertext, shift)

        self.decrypted_text.delete("1.0", tk.END)
        self.decrypted_text.insert(tk.END, plaintext)

    def handle_clear(self):
        self.input_text.delete("1.0", tk.END)
        self.encrypted_text.delete("1.0", tk.END)
        self.decrypted_text.delete("1.0", tk.END)


# ----------------------------
# Run App
# ----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = CaesarCipherApp(root)
    root.mainloop()
