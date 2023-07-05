import tkinter as tk
from tkinter import ttk
from time import sleep
from calc.e6b import E6BCalculator

def show_main_window():
    # Create the main application window
    window = tk.Tk()
    window.title("E6B Calculator")
    window.iconbitmap("src/images/icons8-plane-pastel-128.svg")  # Replace "path_to_icon.ico" with the actual path to your icon file

    # Create an instance of the E6B calculator
    calculator = E6BCalculator(window) #!LandingDistanceCalculator(window) #!PressureAltitudeCalculator(window)
    
    # Start the application
    window.mainloop()

# Create the loading screen window
loading_window = tk.Tk()
loading_window.title("Starting Up...")
loading_window.iconbitmap("src/images/icons8-plane-64.png")  # Replace "path_to_icon.ico" with the actual path to your icon file

# Set the size of the loading window
loading_window.geometry("400x400")

# Create a frame to hold the progress bar
frame = tk.Frame(loading_window, bg="#2a9d8f")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Create a canvas to draw the progress bar
canvas = tk.Canvas(frame, bg="#f4a261", width=0, height=10)
canvas.pack()

# Define the animation function
def animate_progress(width):
    canvas.config(width=width)

# Update the progress bar animation
for width in range(0, 100, 10):
    animate_progress(width)
    loading_window.update()
    sleep(0.5)

# Destroy the loading screen and show the main window
loading_window.destroy()
show_main_window()




