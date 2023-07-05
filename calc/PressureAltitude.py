import tkinter as tk

class PressureAltitudeCalculator:
    def __init__(self, window):
        # Create the input frame
        self.input_frame = tk.Frame(window)
        self.input_frame.pack(pady=10)

        # Sea level pressure input
        sea_level_pressure_label = tk.Label(self.input_frame, text="Sea Level Pressure (inHg):")
        sea_level_pressure_label.grid(row=0, column=0, sticky="e", padx=10, pady=5)
        self.sea_level_pressure_entry = tk.Entry(self.input_frame)
        self.sea_level_pressure_entry.grid(row=0, column=1, padx=10, pady=5)

        # True altitude input
        true_altitude_label = tk.Label(self.input_frame, text="True Altitude (feet):")
        true_altitude_label.grid(row=1, column=0, sticky="e", padx=10, pady=5)
        self.true_altitude_entry = tk.Entry(self.input_frame)
        self.true_altitude_entry.grid(row=1, column=1, padx=10, pady=5)

        # Calculate button
        calculate_frame = tk.Frame(window)
        calculate_frame.pack(pady=10)
        calculate_button = tk.Button(calculate_frame, text="Calculate", command=self.calculate_pressure_altitude, bg="#4CAF50", fg="black", padx=10, pady=5)
        calculate_button.pack()

        # Output label
        self.output_frame = tk.Frame(window)
        self.output_frame.pack(pady=10)
        self.output_label = tk.Label(self.output_frame, text="Pressure Altitude:", font=("Helvetica", 12, "bold"))
        self.output_label.pack()

    def calculate_pressure_altitude(self):
        # Get the values from the input fields
        sea_level_pressure = float(self.sea_level_pressure_entry.get())
        true_altitude = float(self.true_altitude_entry.get())

        # Calculate pressure altitude using the formula
        pressure_altitude = ((sea_level_pressure - 29.92) * 1000) + true_altitude - (true_altitude / 1000)

        # Display the result
        result = f"Pressure Altitude: {pressure_altitude:.2f} feet"
        self.output_label.config(text=result, font=("Helvetica", 12))


