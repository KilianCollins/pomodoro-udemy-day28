from tkinter import *
import time
import winsound
import sys
import os
'''
10-24-25
comand that activates pyinstaller (with pillow installed,(and pillow doesnt need to be imported for this to work) for the .ico automatic conversion) to create the executable
pyinstaller --onefile --windowed --add-data "tomato.png;." --add-data "Ring02.wav;." --icon=ChatGPTPomodoro.ico --name "PomodoroTimer_v3" main.py

pyinstaller --onefile --windowed --add-data "tomato.png;." --add-data "Ring02.wav;." --icon=tomato.ico --name "PomodoroTimer_v3" main.py

'''


# started 10-18-25 completed 10-22-25
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
# RED = "#e7305b"
RED = "#F26849"
LIGHT_GREEN = "#9bdeac"
GREEN = "#379B46"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
BUTTON_FONT = (FONT_NAME, 10, "bold")
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK ="✔"
CHECK_MARK_FONT = (FONT_NAME,10)
tomato_path = r'tomato.png'

# flags
reps = 0
work_count =0
notif_flag = 0
#
timer = None
button_pressed = True
button = None
paused= False

# ---------------------------- POP UP FUNCITONALITY ------------------------------- #
def stay_on_top():
    window.lift()
    window.attributes('-topmost', True)
    window.after(500, stay_on_top)
    window.attributes('-topmost', False)
# ---------------------------- START BUTTON DISABLE AFTER 1ST PRESS ------ #
def on_button_click():
    start_timer()
    start_button.config(state=DISABLED)

def enable_button():
    start_button.config(state=NORMAL)

# ---------------------------- PATH HELPER ------------------------------- #
def resource_path(relative_path): #how and why does this work with pythoninstaller?? 10-22-25
    """ Get absolute path to resource, works for dev and PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global work_count
    global timer
    global reps
    start_button.config(state=NORMAL)
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text,text="00:00")
    checkmark_label.config(text="")
    work_count = 0
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #

def pause():
    global paused
    paused = True

def start_timer():
    global reps
    global timer
    global work_count
    global notif_flag
    reps +=1
    global timer
    if timer is not None:
        window.after_cancel(timer)
    else:
        start_button.config(state=NORMAL)

    work_time = WORK_MIN
    short_break = SHORT_BREAK_MIN
    long_break = LONG_BREAK_MIN
    if reps %8 ==0:

        count_down(long_break)
        notif_flag = LONG_BREAK_MIN
        timer_label.config(text="Break: 20mins", foreground=RED)
    elif reps %2==0:
        notif_flag = SHORT_BREAK_MIN
        count_down(short_break)
        timer_label.config(text="Break: 5mins",foreground=PINK)
    else:
        work_count +=1
        notif_flag = WORK_MIN
        count_down(work_time)
        timer_label.config(text="Work: 25mins",foreground=GREEN)
        checkmark_label.config(text=CHECK_MARK*work_count, font=CHECK_MARK_FONT)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    global notif_flag
    global paused
    s = count % (24 * 3600)
    m = count //60
    s %= 60
    canvas.itemconfig(timer_text, text=f"{"%02d:%02d" % (m, s)}")

    if count >0:
        timer = window.after(1000, count_down, count -1)
    else:
        if notif_flag == LONG_BREAK_MIN:
            play_sound_LONG_BREAK()
            # time.sleep(2.5)
            start_timer()
        elif notif_flag  == SHORT_BREAK_MIN:
            play_sound_SHORT_BREAK()
            # time.sleep(2.5)
            start_timer()
        else:
            play_sound_WORK()
            stay_on_top()
            # time.sleep(2.5)
            start_timer()
# ---------------------------- SOUND SETUP ------------------------------- #
def play_sound_WORK():
    winsound.PlaySound(resource_path(r"Ring02.wav"),winsound.SND_FILENAME)
def play_sound_SHORT_BREAK():
    winsound.PlaySound(resource_path(r"Alarm07.wav"), winsound.SND_FILENAME)
def play_sound_LONG_BREAK():
    winsound.PlaySound(resource_path(r"Alarm02.wav"),winsound.SND_FILENAME)
# ---------------------------- UI SETUP ------------------------------- #
window =Tk()
# window.minsize(600,600)
window.config(bg=YELLOW)
window.title("Pomodoro Study Timer")
window.config(padx=80,pady=100)
# window.overrideredirect(True) # removes the default bar and border on the window, why? bc i dont like the way it looks so im changing it.


# custom window border and title



# tomato image
tomato_img = PhotoImage(file=resource_path(tomato_path))
canvas = Canvas(width=210,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(103,112,image=tomato_img)
canvas.grid(column=1,row=3)
# timer
timer_text = canvas.create_text(103,135, text="00:00",font=(FONT_NAME, 30, "bold"), fill=YELLOW)

# start button
start_button = Button(text="Start", font=BUTTON_FONT, foreground=YELLOW, bg=GREEN, border=0, command=on_button_click)
start_button.grid(column=0,row=4)

# pause button
pause_button = Button(text="Pause",font=BUTTON_FONT,foreground=YELLOW,bg=LIGHT_GREEN,border=0,command=pause)
pause_button.grid(column=0,row=3)

# reset button
reset_button = Button(text="Reset", font=BUTTON_FONT, foreground=YELLOW, bg=RED, border=0, command=reset_timer)
reset_button.grid(column=2, row=4)

# label
timer_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), foreground=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# check mark
checkmark_label = Label(foreground=GREEN,bg=YELLOW)
checkmark_label.grid(column=1,row=5)



# end
window.mainloop()
