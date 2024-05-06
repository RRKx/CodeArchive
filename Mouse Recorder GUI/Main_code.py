import gui_funcs
from tkinter import Tk, Label, Button, Frame

def main_func(func_code):

    if func_code == 1:
        status_label.config(text="Recording started!")
        start_rec_btn.config(state="disabled")
        stop_rec_btn.config(state="active")
        gui_funcs.main(1)
    elif func_code == 2:
        stop_rec_btn.config(state="disabled")
        play_rec_btn.config(state="active")
        start_rec_btn.config(state="active")
        gui_funcs.main(2)
        status_label.config(text="Recording stopped!")
    elif func_code == 3:
        status_label.config(text="Playing recording!")
        window.update()
        gui_funcs.main(3)
        status_label.config(text="Finished playing recording!")

window = Tk()
window.title("Mouse Recorder")
window.resizable(False, False)

frame_one = Frame(window)

start_rec_btn = Button(frame_one, text="Start", width=10, height=6, command=lambda: main_func(1))
start_rec_btn.grid(row=0, column=0)

stop_rec_btn = Button(frame_one, text="Stop", width=10, height=6, state="disabled", command=lambda: main_func(2))
stop_rec_btn.grid(row=0, column=1)

play_rec_btn = Button(frame_one, text="Play", width=10, height=6, state="disabled", command=lambda: main_func(3))
play_rec_btn.grid(row=0, column=2)

frame_one.grid(row=0, column=0)

status_label = Label(window, text="Waiting for information", height=3)
status_label.grid(row=1, column=0)

window.mainloop()