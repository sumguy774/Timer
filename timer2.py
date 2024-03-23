import time
from tkinter import *
from tkinter import messagebox

root = Tk()

paused = False

root.geometry("300x250")
root.title("Set Timer")

hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set("00")
minute.set("00")
second.set("00")

root.resizable(False, False)


hourEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=hour)
hourEntry.place(x=80, y=20)

minuteEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=minute)
minuteEntry.place(x=130, y=20)

secondEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=second)
secondEntry.place(x=180, y=20)

def submit():
    popup = Toplevel(root)
    popup.title("Countdown Time")
    popup.geometry("500x100")

    popup.resizable(False, False)

    countdown_label = Label(popup, text="", font=("Arial", 72))
    countdown_label.pack()

    popup.attributes('-topmost', 1)

    try:
        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except ValueError:
        popup.destroy()
        messagebox.showerror("Error", "Please enter valid time values.")
        hour.set("00")
        minute.set("00")
        second.set("00")
        root.update()
        return

    while temp > -1:
        mins, secs = divmod(temp, 60)
        hours, mins = divmod(mins, 60)
        hour.set("{:02d}".format(hours))
        minute.set("{:02d}".format(mins))
        second.set("{:02d}".format(secs))
        h = hour.get()
        m = minute.get()
        s = second.get()
        countdown_time_h = f"{h}:{m}:{s}"
        countdown_time_m = f"{m}:{s}"
        if h > "00":
            countdown_label.config(text=countdown_time_h)
        elif m > "00":
            countdown_label.config(text=countdown_time_m)
        else:
            countdown_label.config(text=countdown_time_m)
        root.update()

        if not popup.winfo_exists():
            messagebox.showinfo("Time Countdown", "Time's up")
            hour.set("00")
            minute.set("00")
            second.set("00")
            root.update()
            break

        if temp == 0:
            countdown_label.config(text="Time's up!")
            popup.update()
            messagebox.showinfo("Time Countdown", "Time's up")
        temp -= 1
        time.sleep(1)


    popup.destroy()

btn = Button(root, text='Set Time Countdown', bd='5', command=submit)
btn.place(x=70, y=120)

root.mainloop()