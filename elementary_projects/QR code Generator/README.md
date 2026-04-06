# 📱 QR Code Generator (Python)

A simple Python project that generates QR codes from user input using the `qrcode` library.

---

## 🚀 Overview

This project allows users to generate QR codes for any text, URL, or data directly from the terminal.  
It includes basic input validation and automatically saves the QR code as an image file.

---

## ✅ Features

- ✔ Generate QR codes from user input
- ✔ Supports URLs, text, or any string data
- ✔ High error correction (up to 30% recovery)
- ✔ Automatically trims user input (`.strip()`)
- ✔ Saves QR code as an image file (`.png`)
- ✔ Dynamic file naming based on input

---

## 🛠️ Technologies Used

- Python 🐍
- `qrcode` library

---

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/qr-code-generator.git
Navigate to the project folder:
cd qr-code-generator
Install required package:
pip install qrcode[pil]
▶️ How to Run
python main.py

Then enter any text or URL:

Enter link to generate Qr-code: https://example.com
🧪 Example
Input:
https://google.com
Output:
A QR code image file will be generated:
https://g_QR.png

⚠️ Limitations
Filename may contain special characters (:/) depending on input
Overwrites file if same prefix is generated
No GUI (command-line only)
🔥 Future Improvements
Sanitize filename (remove special characters)
Add dynamic timestamp-based filenames
Build GUI (Tkinter / PyQt)
Add color customization
Convert into web app (Flask/Django)
📚 Learning Outcome
Working with external Python libraries
Generating QR codes programmatically
Handling user input and validation
Basic error handling using try-except
🤝 Contributing

Feel free to fork this project and improve it!

📄 License

This project is open-source and free to use.

