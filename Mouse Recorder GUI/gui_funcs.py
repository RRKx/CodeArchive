from pyautogui import *
import click_record

record = False
movement_duration = 0.5

def start_record():
    global record
    record = True
    click_record.recorded_clicks = []
    click_record.start_click_listener()     

def stop_record():
    global record
    record = False
    click_record.stop_click_listener()

def play_record():
    for data in click_record.recorded_clicks:
        if data[2] == "invalid":
            moveTo(data[0], data[1], movement_duration)
        elif data[2] == "left":
            click(data[0], data[1], duration=movement_duration, button=data[2])
        elif data[2] == "right":
            click(data[0], data[1], duration=movement_duration, button=data[2])
        else:
            print("Error occured in play record function")

def main(func_code):
    
    if func_code == 1:
       start_record()
    elif func_code == 2:
        stop_record()
    elif func_code == 3:
        play_record()