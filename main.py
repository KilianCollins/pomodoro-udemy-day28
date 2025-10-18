from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
# RED = "#e7305b"
RED = "#F26849"
LIGHT_GREEN = "#9bdeac"
GREEN = "#379B46"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

tomato_path = r'C:\Users\kilia\Downloads\UDEMY\pomodoro-start\tomato.png'


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

def count_down_mech():
    current_time = time.time()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window =Tk()
# window.minsize(600,600)
window.config(bg=YELLOW)
window.title("Pomodoro Timer")
window.config(padx=80,pady=100)

# tomato image
tomato_img = PhotoImage(file=tomato_path)
canvas = Canvas(width=210,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(103,112,image=tomato_img)
canvas.grid(column=1,row=3)

# counter
canvas.create_text(103,135, text="00:00",font=(FONT_NAME, 30, "bold"), fill=YELLOW)

# start button
start_button = Button(text="Start", font=(FONT_NAME,10,"bold"), foreground=YELLOW, bg=GREEN, border=0, command=count_down_mech)
start_button.grid(column=0,row=4)

# reset button
reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), foreground=YELLOW, bg=RED, border=0, command=count_down_mech)
reset_button.grid(column=2, row=4)

# label
label = Label(text="Timer",font=(FONT_NAME,30,"bold"),foreground=GREEN,bg=YELLOW)
label.grid(column=1,row=0)

# check mark
checkmark_label = Label(text="✔",foreground=GREEN,bg=YELLOW)
checkmark_label.grid(column=1,row=5)

window.mainloop()
