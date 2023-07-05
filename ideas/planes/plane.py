import tkinter as tk

class Plane:
    def __init__(self):
        self.weight = 0

    def add_weight(self, weight):
        self.weight += weight

    def calculate_landing_effects(self):
        # Calculate the landing effects based on the plane's weight
        # You can implement your own logic here
        # For simplicity, let's assume a linear relationship between weight and landing distance
        landing_distance = self.weight * 10  # Just an example formula, you can adjust it as needed
        return landing_distance

def add_weight():
    try:
        weight = float(weight_entry.get())
        plane.add_weight(weight)
        weight_entry.delete(0, tk.END)
        update_plane_position()
        confirmation_label.config(text="Weight added successfully!", fg="green")
    except ValueError:
        confirmation_label.config(text="Invalid weight. Please enter a number.", fg="red")

def calculate_landing_effects():
    landing_distance = plane.calculate_landing_effects()
    confirmation_label.config(text=f"Landing Distance: {landing_distance} meters", fg="black")

def update_plane_position():
    canvas.coords(plane_image, 20, 120 - plane.weight)
    canvas.itemconfig(plane_weight_text, text=f"Weight: {plane.weight} tons")

# Create the main window
window = tk.Tk()
window.title("Plane Weight Simulation")

# Create a Plane instance
plane = Plane()

# Create the GUI elements
canvas = tk.Canvas(window, width=200, height=200, bg="white")
runway = canvas.create_rectangle(10, 150, 190, 160, fill="gray")
plane_image = canvas.create_polygon(20, 120, 40, 120, 30, 110, fill="blue")
plane_weight_text = canvas.create_text(100, 180, text="Weight: 0 tons", fill="black", font=("Arial", 12))

weight_label = tk.Label(window, text="Enter Weight:")
weight_entry = tk.Entry(window)
add_button = tk.Button(window, text="Add Weight", command=add_weight)
calculate_button = tk.Button(window, text="Calculate Landing Effects", command=calculate_landing_effects)
confirmation_label = tk.Label(window, text="", fg="black")

# Arrange the GUI elements using the grid layout
canvas.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
weight_label.grid(row=1, column=0, padx=10, pady=10)
weight_entry.grid(row=1, column=1, padx=10, pady=10)
add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
confirmation_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the Tkinter event loop
window.mainloop()

