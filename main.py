import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from calc.e6b import E6BCalculator

def show_main_window():
    # Create the main application window
    window = tk.Tk()
    window.title("E6B Calculator")

    # Create an instance of the E6B calculator
    calculator = E6BCalculator(window)

    # Start the application
    window.mainloop()

# Create the loading screen window
loading_window = tk.Tk()
loading_window.title("Loading...")

# Set the size of the loading window
loading_window.geometry("400x400")

# Load the GIF image
loading_image = Image.open("src/images/loading.gif")

# Create a label to display the loading animation
loading_label = tk.Label(loading_window)
loading_label.pack(pady=50)

# Convert the loaded image to a Tkinter-compatible format
loading_image = ImageTk.PhotoImage(loading_image)

# Set the image as the label's content
loading_label.config(image=loading_image)

# Start the loading animation
loading_label.image = loading_image

# Update the loading screen and wait for a moment (e.g., 2 seconds)
loading_window.update()
loading_window.after(2000)

# Destroy the loading screen and show the main window
loading_window.destroy()
show_main_window()

