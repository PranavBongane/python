# 📧 Email Validator (Without Regex)

A lightweight Python project that validates email addresses using core string methods and logical rules — without relying on regular expressions.

---

## 🚀 Overview

This project demonstrates how to build a **custom email validation system** using basic Python concepts like:

- String methods
- Conditional statements
- Loops
- Character validation

It is designed for learning purposes and helps understand how validation works internally.

---

## ✅ Features

- ✔ Validates minimum email length
- ✔ Ensures email starts with an alphabet
- ✔ Checks for exactly one `@` symbol
- ✔ Ensures `.` appears after `@`
- ✔ Rejects spaces in email
- ✔ Allows only valid characters:
  - Alphabets (`a-z`, `A-Z`)
  - Numbers (`0-9`)
  - Special characters: `_`, `.`, `@`
- ✔ Provides meaningful error messages

---

## 🧠 Validation Rules

The email is considered **valid** only if:

1. Length is **at least 6 characters**
2. First character is an **alphabet**
3. Contains **exactly one `@`**
4. Contains at least one `.` **after `@`**
5. Does **not contain spaces**
6. Does **not include restricted special characters**

---

## 🛠️ Code Example

```python
def validate_email(email):
    if len(email) >= 6:
        if email[0].isalpha():
            if ("@" in email) and (email.count("@") == 1):

                at_index = email.index("@")
                dot_index = email.rfind(".")

                if dot_index > at_index:
                    if " " not in email:
                        for char in email:
                            if char.isalnum():
                                continue
                            elif char in ["_", "@", "."]:
                                continue
                            else:
                                return "Invalid e-mail (special characters not allowed)"
                        return "Valid Email ✅"
                    else:
                        return "Invalid e-mail (no spaces allowed)"
                else:
                    return "Invalid e-mail ('.' must be after '@')"
            else:
                return "Invalid e-mail ('@' error)"
        else:
            return "Invalid e-mail (must start with alphabet)"
    else:
        return "Invalid e-mail (too short)"