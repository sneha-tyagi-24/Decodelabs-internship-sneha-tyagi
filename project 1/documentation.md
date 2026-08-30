# Project Documentation: Login & Password Strength Checker

## 1. Project Title

**Login & Password Strength Checker**

## 2. Introduction

The Login & Password Strength Checker is a Python-based desktop application designed to demonstrate secure user registration and authentication.

The application combines a graphical user interface with password validation and password hashing. Instead of storing passwords directly, it stores a password-derived hash generated using PBKDF2-HMAC-SHA256 and a random salt.

## 3. Objectives

The main objectives are:

1. Create a simple registration and login system.
2. Check password strength before accepting a new account.
3. Prevent users from selecting passwords containing their username.
4. Detect simple sequential patterns such as `abc` and `123`.
5. Store password credentials without saving the original password.
6. Demonstrate the use of salting and key derivation.
7. Provide a simple GUI using Tkinter.

## 4. System Requirements

### Hardware

- Any modern computer
- Minimum 2 GB RAM recommended
- Approximately 50 MB free storage for Python/project files

### Software

- Python 3.x
- Windows, Linux, or macOS
- Tkinter

The project uses only Python standard-library modules, so no `pip install` command is normally required.

## 5. Modules Used

### tkinter

Used to create the desktop graphical user interface.

### tkinter.messagebox

Used for warnings, errors, and success messages.

### tkinter.ttk

Used for the password-strength progress bar.

### json

Used to store user records locally in `users.json`.

### os

Used to check whether the user-data file exists.

### re

Used for regular-expression checks for lowercase, uppercase, digits, and special characters.

### hashlib

Used to generate the PBKDF2-HMAC-SHA256 password-derived hash.

### hmac

Used for constant-time comparison of the stored and calculated hashes.

### secrets

Used to generate cryptographically secure random salts.

## 6. Functional Requirements

### Registration

The system should:

- Accept a username.
- Accept a password.
- Accept a confirmation password.
- Display password strength.
- Reject mismatched passwords.
- Reject passwords containing the username.
- Reject passwords containing sequential substrings.
- Reject passwords below the minimum strength score.
- Reject duplicate usernames.
- Store the password-derived hash and salt.

### Login

The system should:

- Accept username and password.
- Check whether the username exists.
- Derive a hash from the entered password using the stored salt.
- Compare the calculated hash with the stored hash.
- Display a successful-login message for valid credentials.
- Display an error for an incorrect password.

## 7. Password Strength Algorithm

The function `password_strength()` evaluates five criteria.

```text
Start score = 0

If length >= 8       → +1
If lowercase exists  → +1
If uppercase exists  → +1
If digit exists      → +1
If special exists    → +1

Maximum score = 5
```

The application currently requires:

```text
MIN_STRENGTH_REQUIRED = 3
```

Therefore, a password needs at least 3 of the 5 criteria to pass the strength requirement.

## 8. Sequential Password Detection

The application uses:

```text
has_sequential_substring()
```

to search for sequential alphabetical or numerical patterns.

Examples that can be rejected:

- `abc`
- `cba`
- `123`
- `321`
- `abcd`
- `987`

The check is intended to prevent predictable password patterns.

## 9. Password Hashing Process

The project uses:

```text
PBKDF2-HMAC-SHA256
```

with:

```text
Iterations = 200,000
Salt size = 16 bytes
```

### Registration flow

```text
User enters password
        ↓
Generate random salt
        ↓
PBKDF2-HMAC-SHA256
        ↓
Convert salt/hash to hexadecimal
        ↓
Store record in users.json
```

The original password is not written to `users.json`.

## 10. Password Verification

When a user logs in:

```text
Entered password
        ↓
Read stored salt
        ↓
PBKDF2-HMAC-SHA256
        ↓
Generate verification hash
        ↓
hmac.compare_digest()
        ↓
Match → Login successful
No match → Wrong password
```

Using the same salt is necessary because the salt is part of the password-derivation process.

## 11. Data Storage

After registration, `users.json` has a structure similar to:

```json
{
  "username": {
    "salt": "random hexadecimal value",
    "hash": "derived hexadecimal value",
    "algo": "sha256",
    "iterations": 200000
  }
}
```

The exact salt and hash values will be different for every account.

## 12. Main Functions

### `load_users()`

Loads existing user records from `users.json`.

### `save_users(users)`

Writes user records to `users.json`.

### `hash_password(password, salt=None)`

Generates a random salt for new passwords and derives the password hash using PBKDF2.

### `verify_password(password, salt_hex, stored_hash_hex)`

Recreates the password hash using the stored salt and compares it with the stored hash.

### `contains_username(password, username)`

Checks whether the username appears inside the password.

### `is_sequence(s)`

Determines whether a string contains consecutive increasing or decreasing letters/digits.

### `has_sequential_substring(password)`

Searches the complete password for sequential substrings.

### `password_strength(password)`

Calculates the password-strength score and returns suggestions for improvement.

## 13. GUI Components

The interface contains two major sections.

### Sign Up

- Username input
- Password input
- Confirm password input
- Show Password checkbox
- Strength label
- Strength progress bar
- Feedback message
- Sign Up button

### Login

- Username input
- Password input
- Show Password checkbox
- Login button

## 14. Testing

### Test Case 1: Empty username

**Input:** Empty username

**Expected:** Warning message saying username cannot be empty.

### Test Case 2: Password mismatch

**Input:**
- Password: `Example@123`
- Confirm: `Example@124`

**Expected:** Password mismatch warning.

### Test Case 3: Username inside password

**Input:**
- Username: `sneha`
- Password: `Sneha@1234`

**Expected:** Password rejected.

### Test Case 4: Sequential password

**Input:** `abc@12345`

**Expected:** Password rejected because sequential patterns are present.

### Test Case 5: Weak password

**Input:** `password`

**Expected:** Password rejected if its strength is below 3/5.

### Test Case 6: Successful registration

**Input:** A unique username and password satisfying all validation rules.

**Expected:** Account-created message and a new record in `users.json`.

### Test Case 7: Successful login

**Input:** Correct registered username and password.

**Expected:** Login successful message.

### Test Case 8: Wrong password

**Input:** Registered username with an incorrect password.

**Expected:** Wrong-password error.

## 15. Advantages

- Easy-to-use graphical interface
- No external packages required
- Real-time password-strength feedback
- Prevents simple password patterns
- Does not store plaintext passwords
- Uses a unique salt
- Demonstrates a standard password key-derivation technique

## 16. Limitations

- Uses a local JSON file rather than a database.
- No account lockout or rate limiting.
- No email verification or password reset.
- No multi-factor authentication.
- Login error messages reveal whether a username exists.
- The password-strength algorithm is rule-based and does not measure real-world password entropy.
- The application is designed primarily for learning and demonstration.

## 17. Future Enhancements

Possible improvements include:

1. Add multi-factor authentication (MFA).
2. Add account lockout/rate limiting.
3. Use a database such as SQLite.
4. Add password reset functionality.
5. Add a password generator.
6. Add a better password-strength estimator.
7. Use Argon2id or another modern password hashing approach where appropriate.
8. Add user sessions and logout.
9. Improve GUI design.
10. Add audit logs.
11. Add a secure migration system for changing hashing parameters.
12. Package the application as a Windows executable.

## 18. Conclusion

The project demonstrates how a basic desktop login system can incorporate password-security principles. It combines password-strength validation, sequence detection, random salting, PBKDF2-HMAC-SHA256, and constant-time hash comparison.

Although it is not intended to replace a production authentication service, it provides a practical foundation for understanding secure password storage and authentication in Python.
