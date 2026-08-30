# 🔐 DecodeLabs — Caesar Cipher Tool

**Cyber Security Project 2: Basic Encryption & Decryption**

A simple GUI-based encryption and decryption application developed in Python using the **Caesar Cipher** technique and **Tkinter**.

---

## 📌 Project Overview

DecodeLabs Caesar Cipher Tool demonstrates the basic concept of cryptography through a customizable Caesar Cipher.

The application allows users to:

- Enter plaintext.
- Select a shift key between **1 and 25**.
- Encrypt text using the Caesar Cipher.
- Decrypt ciphertext back to the original plaintext.
- Display encrypted and decrypted results.
- Preserve spaces, punctuation, numbers, symbols, and emojis.
- Handle invalid shift keys and empty input.

The project is designed primarily for **learning and demonstrating basic cryptographic concepts**.

> ⚠️ **Security Note:** Caesar Cipher is not considered secure for real-world communication. It is a classical substitution cipher intended for educational purposes.

---

## ✨ Features

- 🔐 Caesar Cipher encryption
- 🔓 Caesar Cipher decryption
- 🎚️ Customizable shift key
- 🔤 Supports uppercase and lowercase letters
- 🔢 Preserves numbers
- ✍️ Preserves punctuation and symbols
- 😀 Preserves emojis and other non-alphabetic characters
- ⚠️ Input validation
- 🧹 Clear button
- 🖥️ User-friendly graphical interface
- 🔄 Automatic decryption after encryption

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Tkinter | GUI development |
| ttk | Spinbox widget |
| messagebox | Error and warning messages |
| Unicode/ASCII operations | Character shifting |

---

## 📂 Project Structure

```text
DecodeLabs-Caesar-Cipher/
│
├── caesar_cipher.py
├── README.md
├── PROJECT_DOCUMENTATION.md
└── PROJECT_REPORT.md
```

---

## 💻 Requirements

### Software Requirements

- Python 3.x
- Windows, Linux, or macOS
- Tkinter

Tkinter is normally included with standard Python installations.

### Check Python Installation

```bash
python --version
```

or:

```bash
python3 --version
```

---

## 🚀 How to Run

### Step 1 — Clone or Download the Project

Download the project files to your computer.

### Step 2 — Open the Project Directory

Open Command Prompt, PowerShell, Terminal, or VS Code terminal inside the project folder.

### Step 3 — Run the Program

```bash
python caesar_cipher.py
```

If your system uses `python3`:

```bash
python3 caesar_cipher.py
```

---

## 🔐 How Caesar Cipher Works

The Caesar Cipher shifts each alphabetic character by a fixed number of positions.

For example, with a shift of **3**:

```text
A → D
B → E
C → F
...
X → A
Y → B
Z → C
```

### Example

Plaintext:

```text
Hello World!
```

Shift:

```text
3
```

Ciphertext:

```text
Khoor Zruog!
```

When the ciphertext is decrypted using the same shift:

```text
Hello World!
```

---

## 🔄 Encryption Process

1. User enters plaintext.
2. User selects a shift key.
3. The program reads every character.
4. Alphabetic characters are shifted.
5. Uppercase letters remain uppercase.
6. Lowercase letters remain lowercase.
7. Numbers, spaces, punctuation, symbols, and emojis remain unchanged.
8. The encrypted text is displayed.

---

## 🔓 Decryption Process

Decryption reverses the encryption operation.

For example:

```text
Ciphertext: Khoor
Shift: 3
Plaintext: Hello
```

The program uses a negative shift during decryption.

---

## 🧪 Example Test Cases

| Input | Shift | Expected Output |
|---|---:|---|
| `Hello` | 3 | `Khoor` |
| `ABC` | 3 | `DEF` |
| `XYZ` | 3 | `ABC` |
| `Hello World!` | 3 | `Khoor Zruog!` |
| `12345` | 3 | `12345` |
| `Hello@123` | 3 | `Khoor@123` |

---

## ⚠️ Limitations

The Caesar Cipher has several important security weaknesses:

- Only 25 meaningful shift keys exist.
- It can easily be broken using brute force.
- It does not provide modern cryptographic security.
- It should not be used for passwords or sensitive information.
- It does not provide authentication or integrity protection.

---

## 🔮 Future Improvements

Possible improvements include:

- Add file encryption and decryption.
- Add copy-to-clipboard functionality.
- Add save/load functionality.
- Add automatic key generation.
- Add multiple classical ciphers.
- Add AES encryption for real cryptographic security.
- Add password-based encryption.
- Add unit tests.
- Improve the GUI design.
- Add encryption/decryption history.

---

## 🎯 Learning Outcomes

Through this project, the following concepts can be understood:

- Basic cryptography
- Encryption and decryption
- Substitution ciphers
- Symmetric-key concepts
- ASCII/Unicode character manipulation
- Modular arithmetic
- Python functions
- Object-oriented programming
- Tkinter GUI development
- Input validation
- Edge-case handling

---

## 👩‍💻 Project Information

**Project Name:** DecodeLabs — Caesar Cipher Tool  
**Project:** Cyber Security Project 2  
**Language:** Python  
**GUI Framework:** Tkinter  
**Cryptographic Technique:** Caesar Cipher  
**Project Type:** Educational Cyber Security Project

---

## 📜 License

This project is intended for educational and learning purposes.