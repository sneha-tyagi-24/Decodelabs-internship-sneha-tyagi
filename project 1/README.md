# Login & Password Strength Checker

A Python desktop application built with **Tkinter** that provides user registration, password-strength checking, secure password storage, and login authentication.

## Features

- User sign-up and login
- Password strength meter from 0 to 5
- Checks for:
  - Minimum 8 characters
  - Lowercase letter
  - Uppercase letter
  - Digit
  - Special character
- Rejects passwords containing the username
- Detects sequential patterns such as `abc`, `cba`, `123`, and `321`
- Password confirmation during registration
- Show/hide password option
- Stores passwords using **PBKDF2-HMAC-SHA256**
- Uses a unique random salt for each password
- Uses `hmac.compare_digest()` for hash verification
- Stores user credentials locally in `users.json`

## Technologies Used

- Python 3
- Tkinter
- JSON
- `hashlib`
- `hmac`
- `secrets`
- `re`
- `os`

No external Python packages are required.

## Project Structure

```text
password_login_checker/
├── password_login_checker.py
├── README.md
└── documentation.md
```

`users.json` is created automatically after the first successful registration.

## Requirements

Install Python 3.x and make sure Tkinter is available.

Check Python:

```bash
python --version
```

On Windows, Tkinter is normally included with the standard Python installation.

## How to Run

1. Save `password_login_checker.py` in a folder.
2. Open Command Prompt/Terminal in that folder.
3. Run:

```bash
python password_login_checker.py
```

4. The application window will open.
5. Create an account using the **Sign Up** section.
6. Use the same credentials in the **Login** section.

## How Password Storage Works

The application does **not** store the original password.

During registration:

```text
Password
   ↓
Random 16-byte salt
   ↓
PBKDF2-HMAC-SHA256
   ↓
Derived hash
   ↓
users.json
```

The stored record contains the salt, derived hash, algorithm, and iteration count.

PBKDF2 is intentionally computationally expensive, which makes large-scale password guessing more difficult than using a single fast SHA-256 hash.

## Password Strength

The strength score has five possible criteria:

| Criterion | Score |
|---|---:|
| At least 8 characters | +1 |
| Lowercase letter | +1 |
| Uppercase letter | +1 |
| Digit | +1 |
| Special character | +1 |

The current minimum required score is **3/5**.

## Security Notes

This project demonstrates important password-security concepts, but it is intended as an educational/local desktop application.

For a production authentication system, additional controls should be considered, such as:

- Rate limiting and account lockout
- Secure session management
- Generic login error messages
- Stronger password policy
- Password breach checking
- Encrypted database/storage where appropriate
- Secure secret/key management
- Audit logging
- A modern password hashing library such as Argon2id where suitable

Do not commit real `users.json` files containing credential hashes to a public repository.

## License

This project is suitable for educational and academic use. Add a project-specific license if you plan to distribute it publicly.
