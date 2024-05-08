# --------------------------------
# ------- Client side code -------
# --------------------------------
from socket import *
from tkinter import Tk, Label, Entry, Button
from threading import Thread

def connection(server_ip, server_port, buffer_size, data_to_share):
    log_texts = ""

    # Creating a socket using the with statement
    with socket(AF_INET, SOCK_STREAM) as client_socket:

        # Connecting the server socket
        client_socket.connect((server_ip, server_port))
        log_texts += f"Connection established with {server_ip}.\n"
        log.config(text=log_texts)

        # Sending data to the server using the client socket
        client_socket.sendall(bytes(data_to_share, "utf-8"))
        log_texts += f"Data shared with server.\n"
        log.config(text=log_texts)

        # Receving data from the server using the client socket
        received_data = client_socket.recv(buffer_size).decode()
        log_texts += f"Data received from server.\n"
        log.config(text=log_texts)
        received_data_label.config(text=f"{received_data}")

        log_texts += f"Connection with {server_ip} closed.\n"
        log.config(text=log_texts)

def connect_client():

    server_ip = ip_entry.get()
    server_port = int(port_entry.get())
    buffer_size = int(buffer_entry.get())
    data_to_share = data_entry.get()

    received_data_label.config(text="No data received.")
    log.config(text="No data to log.")

    Thread(target=connection, args=(server_ip, server_port, buffer_size, data_to_share)).start()

window = Tk()
window.title("Client configuration")
window.resizable(False, False)


received_data_label = Label(window, text="Client inactive.", width=50, height=10, bg="light grey", fg="black")
received_data_label.grid(row=0, column=0)

log = Label(window, text="Client inactive.", width=50, height=10, bg="grey", fg="black")
log.grid(row=1, column=0)

empty_label1 = Label(window, width=50)
empty_label1.grid(row=2, column=0)

text_label1 = Label(window, text="Server IP:")
text_label1.grid(row=3, columnspan=1, sticky="w")
ip_entry = Entry(window, width=30)
ip_entry.grid(row=3, column=0)


text_label2 = Label(window, text="Server Port:")
text_label2.grid(row=4, columnspan=1, sticky="w")
port_entry = Entry(window, width=30)
port_entry.grid(row=4, column=0)

text_label3 = Label(window, text="Buffer Size:")
text_label3.grid(row=5, columnspan=1, sticky="w")
buffer_entry = Entry(window, width=30)
buffer_entry.grid(row=5, column=0)

text_label4 = Label(window, text="Data to share:")
text_label4.grid(row=6, columnspan=1, sticky="w")
data_entry = Entry(window, width=30)
data_entry.grid(row=6, column=0)

empty_label2 = Label(window, width=50)
empty_label2.grid(row=7, column=0)

connect_client_button = Button(window, text="Connect client", command=connect_client)
connect_client_button.grid(row=8, columnspan=1)


window.mainloop()

# Client side code must be run on another terminal