# 📧 Email Validator using Regex (Python)

A simple and efficient Python project to validate email addresses using **Regular Expressions (Regex)**.

---

## 🚀 Overview

This project demonstrates how to validate email formats using Python’s built-in `re` module.  
Unlike manual validation, this approach is **concise, scalable, and closer to real-world implementations**.

---

## ✅ Features

- ✔ Validates email using Regex pattern
- ✔ Ensures proper structure (`username@domain.extension`)
- ✔ Supports:
  - Letters and numbers
  - Special characters: `.`, `_`, `+`
- ✔ Handles multiple domain extensions (e.g., `.co.in`)
- ✔ Clean and minimal code

---

## 🧠 Regex Pattern Used

```python
pattern = r'^[a-zA-Z][a-zA-Z0-9._+]*@[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+$'
🔍 Explanation
^ → Start of string
[a-zA-Z] → Must start with a letter
[a-zA-Z0-9._+]* → Allows letters, digits, ., _, +
@ → Required symbol
[a-zA-Z0-9-]+ → Domain name
(\.[a-zA-Z]{2,})+ → One or more domain extensions (.com, .co.in)
$ → End of string

▶️ How to Run
Clone the repository:
git clone https://github.com/your-username/email-validator-regex.git
Navigate to the folder:
cd email-validator-regex
Run the script:
python main.py
Enter an email when prompted.
🧪 Examples
✅ Valid Emails
test@gmail.com  
user.name@domain.com  
test+123@gmail.com  
user@domain.co.in  
❌ Invalid Emails
test@.com  
@test.com  
test@gmail  
test gmail.com  
📌 Advantages of Regex Approach
✔ Short and clean code
✔ Easy to maintain
✔ Widely used in real-world applications
✔ More scalable than manual validation
⚠️ Limitations
Does not verify if the email actually exists
Does not check domain validity
Simplified version of real-world email validation rules
🔥 Future Improvements
Add DNS/domain validation
Integrate with a web form (Flask/Django)
Combine with password validation system
Build a complete authentication module
📚 Learning Outcome
Understanding of Regular Expressions in Python
Difference between re.match() and re.fullmatch()
Practical input validation techniques
🤝 Contributing

Feel free to fork and improve this project!

📄 License

This project is open-source and free to use.

