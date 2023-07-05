import tkinter as tk
from tkinter import scrolledtext
import socket
import threading

# Constants
HOST = '40.76.247.226'  # Change this to your desired host
PORT = 22  # Change this to your desired port

# Function to handle receiving messages
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            message_box.insert(tk.END, message)
        except ConnectionAbortedError:
            break
        except:
            print("An error occurred while receiving messages.")
            client_socket.close()
            break

# Function to handle sending messages
def send_message():
    message = message_entry.get()
    message_entry.delete(0, tk.END)
    client_socket.sendall(message.encode('utf-8'))

# Function to handle closing the application
def close_app():
    client_socket.close()
    window.destroy()

# Create the GUI window
window = tk.Tk()
window.title("Simple Chat")
window.resizable(width=False, height=False)

# Create a scrolled text box to display the chat messages
message_box = scrolledtext.ScrolledText(window, width=50, height=20)
message_box.grid(row=0, column=0, columnspan=2)

# Create an entry field for typing messages
message_entry = tk.Entry(window, width=40)
message_entry.grid(row=1, column=0)

# Create a button to send messages
send_button = tk.Button(window, text="Send", command=send_message)
send_button.grid(row=1, column=1)

# Create a button to close the application
close_button = tk.Button(window, text="Close", command=close_app)
close_button.grid(row=2, column=0, columnspan=2)

# Connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Start a thread to receive messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Start the GUI event loop
window.mainloop()
