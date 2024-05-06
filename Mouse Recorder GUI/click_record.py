from pynput.mouse import Listener, Controller

recorded_clicks = []
listener = None

def recording_clicks(x, y, button, pressed):
    if pressed:
        recorded_clicks.append([int(x), int(y), button.name])
    else:
        x, y = Controller().position
        recorded_clicks.append([x, y, 'invalid'])

def start_click_listener():
    global listener
    if listener is None or not listener.is_alive():
        listener = Listener(on_click=recording_clicks)
        listener.start()

def stop_click_listener():
    if listener is not None:
        listener.stop()