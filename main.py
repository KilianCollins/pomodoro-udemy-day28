from tkinter import *
import time
#started 10-18-25
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
round_count = 0

tomato_path = r'C:\Users\kilia\Downloads\UDEMY\pomodoro-start\tomato.png'


# ---------------------------- TIMER RESET ------------------------------- #

def start_timer():
    count_down(WORK_MIN)


def reset_timer():
    canvas.itemconfig(timer_text, timer_text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #





def count_down(count):
    # count = count * 60
    # h = count / 3600
    #why and how does this work?
    global round_count


    if count >0:
        s = count % (24 * 3600)
        m = count // 60  # // always produces a integer instead of a float
        s %= 60
        # if round_count == 0 or round_count % 2 == 0:
        print(count)
        window.after(1000, count_down, count - 1)
        canvas.itemconfig(timer_text, text=f"{"%02d:%02d" % (m, s)}")

    elif count <=0:
        round_count +=1
        if round_count %7 == 0:
            count = SHORT_BREAK_MIN
            s = count % (24 * 3600)
            m = count // 60  # // always produces a integer instead of a float
            s %= 60
            print(count)
            window.after(1000, count_down, count - 1)
            canvas.itemconfig(timer_text, text=f"{"%02d:%02d" % (m, s)}")
            # count_down(SHORT_BREAK_MIN)
        elif round_count % 3 ==0:
            count = LONG_BREAK_MIN
            s = count % (24 * 3600)
            m = count // 60  # // always produces a integer instead of a float
            s %= 60
            print(count)
            window.after(1000, count_down, count - 1)
            canvas.itemconfig(timer_text, text=f"{"%02d:%02d" % (m, s)}")
            # count_down(LONG_BREAK_MIN)
        elif round_count % 2== 0:
            count = WORK_MIN
            s = count % (24 * 3600)
            m = count // 60  # // always produces a integer instead of a float
            s %= 60
            print(count)
            window.after(1000, count_down, count - 1)
            canvas.itemconfig(timer_text, text=f"{"%02d:%02d" % (m, s)}")


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
timer_text = canvas.create_text(103,135, text="00:00",font=(FONT_NAME, 30, "bold"), fill=YELLOW)

# start button
# start_button = Button(text="Start", font=(FONT_NAME,10,"bold"), foreground=YELLOW, bg=GREEN, border=0, command=lambda:count_down(WORK_MIN *60))
start_button = Button(text="Start", font=(FONT_NAME,10,"bold"), foreground=YELLOW, bg=GREEN, border=0, command=start_timer)

start_button.grid(column=0,row=4)

# reset button
reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), foreground=YELLOW, bg=RED, border=0, command=reset_timer)
reset_button.grid(column=2, row=4)

# label
label = Label(text="Timer",font=(FONT_NAME,30,"bold"),foreground=GREEN,bg=YELLOW)
label.grid(column=1,row=0)

# check mark
checkmark_label = Label(text="✔",foreground=GREEN,bg=YELLOW)
checkmark_label.grid(column=1,row=5)

# count_down(5)

window.mainloop()
