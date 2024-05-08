from tkinter import Tk, Button, Label, Frame

window = Tk()
window.title("Tic Tac Toe V1 GUI")
window.resizable(False, False)

text_label = Label(window, text="X's turn", bg="yellow", fg="black", width=25, height=4)
text_label.grid(row=0, column=0)

buttons_frame = Frame(window)
buttons_frame.grid(row=1, column=0, sticky='w')

win_combos = ["123", "456", "789", "147", "258", "369", "159", "357"]
x_turn = True
change_made = False
x_values = []
o_values = []
x_check = 0
o_check = 0
buttons_pressed = 0
accept_input = True

def reset_program():
    global x_turn, change_made, x_values, o_values, x_check, o_check, buttons_pressed, accept_input
    button_1.config(text="")
    button_2.config(text="")
    button_3.config(text="")
    button_4.config(text="")
    button_5.config(text="")
    button_6.config(text="")
    button_7.config(text="")
    button_8.config(text="")
    button_9.config(text="")
    x_turn = True
    change_made = False
    x_values = []
    o_values = []
    x_check = 0
    o_check = 0
    text_label.config(text="X's turn")
    buttons_pressed = 0
    accept_input = True

def main_program(button_value):
    global x_turn, change_made, x_check, o_check, buttons_pressed, accept_input

    if accept_input:
        turn_letter = 'X' if x_turn else 'O'
        label_turn_letter = 'O' if turn_letter == 'X' else 'X'
        
        if not button_1["text"] and button_value == 1:
            button_1.config(text=turn_letter)
            change_made = True
            buttons_pressed += 1
        elif not button_2["text"] and button_value == 2:
            button_2.config(text=turn_letter)
            change_made = True
            buttons_pressed += 1
        elif not button_3["text"] and button_value == 3:
            button_3.config(text=turn_letter)
            change_made = True
            buttons_pressed += 1
        elif not button_4["text"] and button_value == 4:
            button_4.config(text=turn_letter)
            change_made = True
            buttons_pressed += 1
        elif not button_5["text"] and button_value == 5:
            button_5.config(text=turn_letter)
            change_made = True
            buttons_pressed += 1
        elif not button_6["text"] and button_value == 6:
            button_6.config(text=turn_letter)
            change_made = True
            buttons_pressed += 1
        elif not button_7["text"] and button_value == 7:
            button_7.config(text=turn_letter)
            change_made = True
            buttons_pressed += 1
        elif not button_8["text"] and button_value == 8:
            button_8.config(text=turn_letter)
            change_made = True
            buttons_pressed += 1
        elif not button_9["text"] and button_value == 9:
            button_9.config(text=turn_letter)
            change_made = True
            buttons_pressed += 1

        if change_made:

            if x_turn:
                x_values.append(str(button_value))
            else:
                o_values.append(str(button_value))

            for combo in win_combos:
                for character in combo:
                    if character in x_values:
                        x_check += 1
                    else:
                        x_check = 0
                        break

                for character in combo:
                    if character in o_values:
                        o_check += 1
                    else:
                        o_check = 0
                        break
            
                if x_check == 3:
                    print("X Won!")
                    text_label.config(text="X Won!")
                    accept_input = False
                    window.after(5000, lambda: reset_program())
                    return
                elif o_check == 3:
                    print("O Won!")
                    text_label.config(text="O Won!")
                    accept_input = False
                    window.after(5000, lambda: reset_program())
                    return
            
            if buttons_pressed == 9:
                print("No one won!")
                text_label.config(text="No one won!")
                accept_input = False
                window.after(5000, lambda: reset_program())
                return
            
            x_turn = not x_turn
            change_made = False
            text_label.config(text=f"{label_turn_letter}'s turn")



button_1 = Button(buttons_frame, text="", width=5, height=4, command= lambda: main_program(1))
button_1.grid(row=1, column=0)

button_2 = Button(buttons_frame, text="", width=5, height=4, command= lambda: main_program(2))
button_2.grid(row=1, column=1)

button_3 = Button(buttons_frame, text="", width=5, height=4, command= lambda: main_program(3))
button_3.grid(row=1, column=2)

button_4 = Button(buttons_frame, text="", width=5, height=4, command= lambda: main_program(4))
button_4.grid(row=2, column=0)

button_5 = Button(buttons_frame, text="", width=5, height=4, command= lambda: main_program(5))
button_5.grid(row=2, column=1)

button_6 = Button(buttons_frame, text="", width=5, height=4, command= lambda: main_program(6))
button_6.grid(row=2, column=2)

button_7 = Button(buttons_frame, text="", width=5, height=4, command= lambda: main_program(7))
button_7.grid(row=3, column=0)

button_8 = Button(buttons_frame, text="", width=5, height=4, command= lambda: main_program(8))
button_8.grid(row=3, column=1)

button_9 = Button(buttons_frame, text="", width=5, height=4, command= lambda: main_program(9))
button_9.grid(row=3, column=2)

window.mainloop()

# Used ChatGPT for debugging and linear statements

# Notes to self,
# There are various types of linear statements used in Python
# The return keyword can be used to exit out of the function