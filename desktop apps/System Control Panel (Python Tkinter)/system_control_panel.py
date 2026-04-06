from tkinter import *
from tkinter import messagebox
import os

# ------------------ FUNCTIONS ------------------ #
def restart():
    if messagebox.askyesno("Confirm", "Restart your system?"):
        os.system("shutdown /r /t 1")

def restart_time():
    if messagebox.askyesno("Confirm", "Restart in 20 seconds?"):
        os.system("shutdown /r /t 20")

def logout():
    if messagebox.askyesno("Confirm", "Log out now?"):
        os.system("shutdown /l")

def shutdown():
    if messagebox.askyesno("Confirm", "Shutdown your system?"):
        os.system("shutdown /s /t 1")


# ------------------ WINDOW ------------------ #
st = Tk()
st.title("System Control Panel")
st.geometry("500x400")
st.resizable(False, False)
st.config(bg="#1e1e2f")   # Dark modern background


# ------------------ TITLE ------------------ #
title = Label(
    st,
    text="⚡ System Control Panel",
    font=("Segoe UI", 20, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=20)


# ------------------ FRAME ------------------ #
frame = Frame(st, bg="#1e1e2f")
frame.pack(pady=10)


# ------------------ BUTTON STYLE ------------------ #
btn_style = {
    "font": ("Segoe UI", 14, "bold"),
    "width": 25,
    "height": 2,
    "bd": 0,
    "cursor": "hand2"
}


# ------------------ BUTTONS ------------------ #
Button(
    frame,
    text="🔄 Restart",
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",
    command=restart,
    **btn_style
).pack(pady=8)

Button(
    frame,
    text="⏳ Restart in 20 sec",
    bg="#2196F3",
    fg="white",
    activebackground="#1976D2",
    command=restart_time,
    **btn_style
).pack(pady=8)

Button(
    frame,
    text="🚪 Log Out",
    bg="#FF9800",
    fg="white",
    activebackground="#F57C00",
    command=logout,
    **btn_style
).pack(pady=8)

Button(
    frame,
    text="⛔ Shutdown",
    bg="#F44336",
    fg="white",
    activebackground="#D32F2F",
    command=shutdown,
    **btn_style
).pack(pady=8)


# ------------------ FOOTER ------------------ #
footer = Label(
    st,
    text="Made by Pranav ⚡",
    font=("Segoe UI", 10),
    bg="#1e1e2f",
    fg="gray"
)
footer.pack(side=BOTTOM, pady=10)


# ------------------ RUN ------------------ #
st.mainloop()