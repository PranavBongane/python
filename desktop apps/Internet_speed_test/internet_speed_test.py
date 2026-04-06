from tkinter import *
import speedtest
import threading

def speed_check():
    threading.Thread(target=run_speed_test).start()

def run_speed_test():
    try:
        lab_down.config(text="Checking...")
        lab_up.config(text="Checking...")

        sp = speedtest.Speedtest(secure=True)
        sp.get_servers()

        down = str(round(sp.download()/(10**6), 2)) + " Mbps"
        up = str(round(sp.upload()/(10**6), 2)) + " Mbps"

        lab_down.config(text=down)
        lab_up.config(text=up)

    except Exception as e:
        lab_down.config(text="Error")
        lab_up.config(text="Try Again")
        print("Error:", e)


sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x500")
sp.config(bg="#1e1e2f")

# Title
title = Label(
    sp,
    text="⚡ Internet Speed Test",
    font=("Segoe UI", 25, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.place(x=30, y=40)

# Download
Label(
    sp,
    text="Download Speed",
    font=("Segoe UI", 20, "bold"),
    bg="#151556",
    fg="white"
).place(x=65, y=110, height=50, width=380)

lab_down = Label(
    sp,
    text="00 Mbps",
    font=("Segoe UI", 30, "bold"),
    bg="#1e1e2f",
    fg="white"
)
lab_down.place(x=65, y=170, height=50, width=380)

# Upload
Label(
    sp,
    text="Upload Speed",
    font=("Segoe UI", 20, "bold"),
    bg="#151556",
    fg="white"
).place(x=65, y=230, height=50, width=380)

lab_up = Label(
    sp,
    text="00 Mbps",
    font=("Segoe UI", 30, "bold"),
    bg="#1e1e2f",
    fg="white"
)
lab_up.place(x=65, y=290, height=50, width=380)

# Button
Button(
    sp,
    text="CHECK SPEED",
    font=("Segoe UI", 15, "bold"),
    bg="#7F0404",
    fg="white",
    command=speed_check
).place(x=65, y=400, height=50, width=380)

sp.mainloop()