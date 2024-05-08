# This code is written to understand the basics of sockets
# --------------------------------
# ------- Server side code -------
# --------------------------------

from socket import *
from tkinter import Tk, Label, Entry, Button
from threading import Thread

# The server will automatically close after receiving a connection from the client

server_active = False

def connection(server_ip, server_port, queue_limit, buffer_size, data_to_share):
    global server_active

    start_server_button.config(state="disabled")
    log_texts = ""

    # Creating a socket using the with statement
    while server_active:
        with socket(AF_INET, SOCK_STREAM) as server_socket:
            try:
                # Assigns the socket to an ip address and a port
                server_socket.bind((server_ip, server_port))

                # Enables the socket to receive connections upto the queue limit
                server_socket.listen(queue_limit)

                # Accept the received connection, which returns a tuple with client socket and client address
                client_socket, client_address = server_socket.accept()
                log_texts += f"Connection established with {client_address}.\n"
                log.config(text=log_texts)

                # To receive data from the client socket, decoding it using .decode()
                received_data = client_socket.recv(buffer_size).decode()
                received_data_label.config(text=f"{received_data}")

                log_texts += f"Client shared the data.\n"
                log.config(text=log_texts)

                # To send data to the client
                client_socket.sendall(bytes(data_to_share, 'utf-8'))
                log_texts += "Shared data with client.\n"
                log.config(text=log_texts)

                # To end the connection between the server and the client socket
                client_socket.close()
                log_texts += f"Connection with {client_address} closed.\n"

                log_texts += f"Closing server.\n"
                log.config(text=log_texts)

                server_active = False
                received_data_label.after(5000, lambda: received_data_label.config(text="Server inactive."))
                log.after(10000, lambda: log.config(text="Server inactive."))
                break

            except OSError as error:
                print(f"{error} occured, terminating server.")
                break
            finally:
                start_server_button.config(state="active")

def start_server():
    global server_active

    try:
        server_ip = ip_entry.get()
        server_port = int(port_entry.get())
        queue_limit = int(Q_limit_entry.get())
        buffer_size = int(buffer_entry.get())
        data_to_share = data_entry.get()

        received_data_label.config(text="No data received.")
        log.config(text="No data to log.")
        
        server_active = True
        Thread(target=connection, args=(server_ip, server_port, queue_limit, buffer_size, data_to_share)).start()
    except ValueError as error:
        print(f"{error} occured, server startup request failed.")

window = Tk()
window.title("Server configuration")
window.resizable(False, False)

received_data_label = Label(window, text="Server inactive.", width=50, height=10, bg="light grey", fg="black")
received_data_label.grid(row=0, column=0)

log = Label(window, text="Server inactive.", width=50, height=10, bg="grey", fg="black")
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

text_label3 = Label(window, text="Queue Limit:")
text_label3.grid(row=5, columnspan=1, sticky="w")
Q_limit_entry = Entry(window, width=30)
Q_limit_entry.grid(row=5, column=0)

text_label4 = Label(window, text="Buffer Size:")
text_label4.grid(row=6, columnspan=1, sticky="w")
buffer_entry = Entry(window, width=30)
buffer_entry.grid(row=6, column=0)

text_label5 = Label(window, text="Data to share:")
text_label5.grid(row=7, columnspan=1, sticky="w")
data_entry = Entry(window, width=30)
data_entry.grid(row=7, column=0)

empty_label2 = Label(window, width=50)
empty_label2.grid(row=8, column=0)

start_server_button = Button(window, text="Start Server", command=start_server)
start_server_button.grid(row=9, columnspan=1)

window.mainloop()

# Used ChatGPT for debugging and threading

# Default settings
# server_ip = '127.0.0.1' This is a loopback address, it refers to the local host
# server_port = 1234
# buffer_size = 1024


# Notes to self,
# Threading allows for the execution of multiple tasks concurrently within a single process (an instance of a program)
# For threading, target=function name, args=(arguments for the function). args paremeter only applies if there are arguments for the function

# b"" is used to convert characters within the quotation into bytes, you can use "".encode() or bytes("", "type of encoding, generally utf-8")

# send(data) Sends the specified data over the socket. It will attempt to send as much data as possible in a single call, up to the buffer size. 
#   If the buffer is full and not all data is sent, 
#   the unsent data remains in the buffer and must be sent manually by calling send() again.
# sendall(data): Sends all the data in the buffer over the socket. 
#   It repeatedly calls send() to send all the data until either all data has been sent or an error occurs. 
#   It ensures that all data is sent before returning, simplifying the process of sending large amounts of data.

# The server socket is used only for accepting connections.
# Once a connection is accepted, both the server and the client use the same client socket to communicate over the established connection.

# Functions can always access global variables but cannot modify them unless the global keyword is used

# AF_INET refers to IPV4, SOCK_STREAM refers to TCP