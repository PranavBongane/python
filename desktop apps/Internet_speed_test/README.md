# ⚡ Internet Speed Test (Python Tkinter)

A modern desktop application built with Python and Tkinter that allows users to check real-time internet speed (Download & Upload) with a clean GUI and responsive performance using threading.

---

## 🚀 Features

- 📶 Check Download Speed
- 📤 Check Upload Speed
- ⚡ Fast & Responsive UI (Threading Enabled)
- 🔄 Live Status Updates ("Checking...")
- ❌ Error Handling for Network Issues
- 🎨 Modern Dark-Themed Interface

---

## 🛠️ Technologies Used

- Python 🐍
- Tkinter (GUI framework)
- speedtest-cli (Internet speed API)
- threading (for non-blocking UI)

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/internet-speed-test.git
cd internet-speed-test
2. Install Required Package
pip install speedtest-cli

⚠️ Important: Do NOT install speedtest package
Use only speedtest-cli

3. Run the Application
python main.py
📂 Project Structure
internet-speed-test/
│── main.py
│── README.md
🧠 How It Works
When user clicks CHECK SPEED:
A background thread starts
Internet speed is fetched using speedtest-cli
UI updates without freezing
⚠️ Important Notes
Works best on Windows OS
Requires active internet connection
May fail on:
Restricted networks (office/college WiFi)
Firewalled environments
🔥 Key Concept Used
Threading (Non-blocking UI)
threading.Thread(target=run_speed_test).start()

✔ Prevents GUI from freezing
✔ Runs network call in background

🚀 Future Improvements
📊 Speed history graph
⏱️ Custom test intervals
🌐 Server selection
📦 Convert to .exe
🎯 Speed meter animation
👨‍💻 Author

Pranav Bongane

⭐ Support

If you like this project:

Star the repository
Share it with others
📜 License

This project is open-source and free to use.