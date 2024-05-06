from tkinter import *

# Main code

sum = 0
ordered_items = []
ordered_items_cost = []
command_log_text = ''

def total(item, cost):
    global sum, command_log, ordered_items, ordered_items_cost, command_log_text, cost_label

    command_log_text = ''
    sum += cost
    ordered_items.append(item)
    ordered_items_cost.append(cost)

    for index in range(len(ordered_items)):
        command_log_text = command_log_text + f"\n{ordered_items[index]} | {ordered_items_cost[index]}$"

    command_log.config(text=command_log_text)
    cost_label.config(text=f"{sum}")

def other(operation_code):
    global ordered_items, ordered_items_cost, command_log_text, command_log, sum, cost_label

    command_log_text = ''
    try:
        if operation_code == 0:
            del ordered_items[-1]
            sum -= ordered_items_cost[-1]
            del ordered_items_cost[-1]

            for index in range(len(ordered_items)):
                command_log_text = command_log_text + f"\n{ordered_items[index]} | {ordered_items_cost[index]}$"
            
            command_log.config(text=command_log_text)
            cost_label.config(text=f"{sum}")

        elif operation_code == 1:
            ordered_items = []
            ordered_items_cost = []
            command_log.config(text=command_log_text)
            sum = 0
            cost_label.config(text=f"{sum}")

    except IndexError as error:
        pass

receipt_number = 1

def save():

    try:
        global ordered_items, ordered_items_cost, sum, receipt_number, save_text

        file_name = f"Receipt {receipt_number}"
        # Edit folder name, make sure folder exists in local directory
        file_location = f"FolderName/{file_name}.txt"

        if ordered_items:
            with open(file_location, "w") as receipt:
                receipt.write("---------------------------")
                receipt.write("\n------Item(s) ordered------")
                receipt.write("\n---------------------------")

                for index in range(len(ordered_items)):
                    receipt.write(f"\n{ordered_items[index]} | {ordered_items_cost[index]}")

                receipt.write("\n---------------------------")
                receipt.write("\n---------Total cost--------")
                receipt.write("\n---------------------------")
                receipt.write(f"\n            {sum}            ")
                receipt.write("\n---------------------------")

            receipt_number += 1

            save_text.config(text="Receipt Saved!")
            save_text.after(3000, lambda: save_text.config(text=''))
        else:
            save_text.config(text="Receipt not saved!")
            save_text.after(3000, lambda: save_text.config(text=''))

    except FileNotFoundError as error:
        pass


# GUI

window = Tk()

window.title("Simple Receipt System")
window.resizable(False, False)

item_button_width = 2
item1_cost = 5
item2_cost = 10
item3_cost = 15
item4_cost = 20

items_frame = Frame(window)
items_frame.grid(row=0, column=0)

item1_label = Label(items_frame, text='item1')
item1_button = Button(items_frame, text=f'{item1_cost}$', width=item_button_width, command= lambda: total("item1", item1_cost))
item1_label.grid(row=0, column=0)
item1_button.grid(row=0, column=1)

item2_label = Label(items_frame, text='item2')
item2_button = Button(items_frame, text=f'{item2_cost}$', width=item_button_width, command= lambda: total("item2", item2_cost))
item2_label.grid(row=1)
item2_button.grid(row=1, column=1)

item3_label = Label(items_frame, text='item3')
item3_button = Button(items_frame, text=f'{item3_cost}$', width=item_button_width, command= lambda: total("item3", item3_cost))
item3_label.grid(row=0, column=2)
item3_button.grid(row=0, column=3)

item4_label = Label(items_frame, text='item4')
item4_button = Button(items_frame, text=f'{item4_cost}$', width=item_button_width, command= lambda: total("item4", item4_cost))
item4_label.grid(row=1, column=2)
item4_button.grid(row=1, column=3)

empty_label1 = Label(window, height=1)
empty_label1.grid(row=2)

command_log = Label(window, bg="light grey", height=7, width=30, fg="black")
command_log.grid(row=3)

empty_label2 = Label(window, height=1)
empty_label2.grid(row=4)

cost_text_label = Label(window, text="Total cost")
cost_text_label.grid(row=5, column=0)

cost_label = Label(window, text=0)
cost_label.grid(row=6, column=0)

empty_label3 = Label(window, height=1)
empty_label3.grid(row=7)

delete_button = Button(window, text="Remove last item", width=10, command= lambda: other(0))
clear_button = Button(window, text="Clear receipt", width=10, command= lambda: other(1))

delete_button.grid(row=8, column=0)
clear_button.grid(row=9, column=0)

save_button = Button(window, text="Save receipt", command=save)
save_button.grid(row=10, column=0)

save_text = Label(window)
save_text.grid(row=11, column=0)

empty_label5 = Label(window, height=1)
empty_label5.grid(row=12)

window.mainloop()

# Used ChatGPT for debugging
# Code is not refined, i rushed its development
# command_log will overflow with items, need to add a scrollbar

# Notes to self
# .after(miliseconds, lambda: expression) executes the expression after specified time
# \n is used as a escape character for new line