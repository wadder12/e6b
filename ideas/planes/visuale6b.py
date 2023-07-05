import tkinter as tk
import math

def calculate():
    # Retrieve input values from the entry fields
    wind_angle = int(wind_angle_entry.get())
    wind_speed = int(wind_speed_entry.get())
    ground_speed = int(ground_speed_entry.get())
    heading = int(heading_entry.get())

    # Perform E6B calculations
    true_airspeed = ground_speed + wind_speed * math.cos(math.radians(wind_angle - heading))
    wind_correction_angle = math.degrees(math.asin(wind_speed * math.sin(math.radians(wind_angle - heading)) / true_airspeed))
    heading_to_track = heading + wind_correction_angle
    ground_track = heading + wind_angle

    # Update the result labels with the calculated results
    tas_label.configure(text=f"True Airspeed: {true_airspeed:.2f} knots")
    wca_label.configure(text=f"Wind Correction Angle: {wind_correction_angle:.2f}°")
    hdt_label.configure(text=f"Heading to Track: {heading_to_track:.2f}°")
    gtrk_label.configure(text=f"Ground Track: {ground_track:.2f}°")

def rotate(event):
    # Calculate rotation angle based on cursor position
    x = event.x - canvas_width / 2
    y = canvas_height / 2 - event.y
    angle = math.degrees(math.atan2(y, x))

    # Rotate the E6B components
    canvas.delete("e6b_components")
    draw_e6b_components(angle)

def draw_e6b_components(angle):
    # Outer circle representing the E6B
    canvas.create_oval(50, 50, 550, 350, outline='black', width=2, tags="e6b_components")

    # Draw radial lines
    for i in range(0, 360, 30):
        x1 = 300 + 140 * math.cos(math.radians(i))
        y1 = 200 - 140 * math.sin(math.radians(i))
        x2 = 300 + 150 * math.cos(math.radians(i))
        y2 = 200 - 150 * math.sin(math.radians(i))
        canvas.create_line(x1, y1, x2, y2, fill='black', width=2, tags="e6b_components")

    # Draw numbers
    for i in range(0, 360, 30):
        x = 300 + 175 * math.cos(math.radians(i))
        y = 200 - 175 * math.sin(math.radians(i))
        canvas.create_text(x, y, text=str(i), font=("Arial", 10), tags="e6b_components")

    # Heading disk
    heading_disk_x = 300 + 150 * math.cos(math.radians(angle))
    heading_disk_y = 200 - 150 * math.sin(math.radians(angle))
    canvas.create_oval(heading_disk_x - 10, heading_disk_y - 10, heading_disk_x + 10, heading_disk_y + 10, fill='red', tags="e6b_components")

    # Wind disk
    wind_disk_x = 300 + 100 * math.cos(math.radians(angle + 180))
    wind_disk_y = 200 - 100 * math.sin(math.radians(angle + 180))
    canvas.create_oval(wind_disk_x - 10, wind_disk_y - 10, wind_disk_x + 10, wind_disk_y + 10, fill='blue', tags="e6b_components")

# Create the main window
window = tk.Tk()
window.title("Interactive E6B Calculator")

# Create a Canvas widget to display the E6B components
canvas = tk.Canvas(window, width=600, height=400)
canvas.pack()

# Get the dimensions of the canvas
canvas_width = canvas.winfo_width()
canvas_height = canvas.winfo_height()

# Draw the initial E6B components
draw_e6b_components(0)

# Bind the rotation function to mouse movements
canvas.bind("<B1-Motion>", rotate)

# Create labels and entry fields for input
wind_angle_label = tk.Label(window, text="Wind Angle:")
wind_angle_label.pack()

wind_angle_entry = tk.Entry(window)
wind_angle_entry.pack()

wind_speed_label = tk.Label(window, text="Wind Speed:")
wind_speed_label.pack()

wind_speed_entry = tk.Entry(window)
wind_speed_entry.pack()

ground_speed_label = tk.Label(window, text="Ground Speed:")
ground_speed_label.pack()

ground_speed_entry = tk.Entry(window)
ground_speed_entry.pack()

heading_label = tk.Label(window, text="Heading:")
heading_label.pack()

heading_entry = tk.Entry(window)
heading_entry.pack()

# Create a button to perform the calculation
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

# Create labels to display the results
tas_label = tk.Label(window, text="True Airspeed: ")
tas_label.pack()

wca_label = tk.Label(window, text="Wind Correction Angle: ")
wca_label.pack()

hdt_label = tk.Label(window, text="Heading to Track: ")
hdt_label.pack()

gtrk_label = tk.Label(window, text="Ground Track: ")
gtrk_label.pack()

# Start the main event loop
window.mainloop()
