import tkinter as tk

class LandingDistanceCalculator:
    def __init__(self, window):
        # Create the input frame
        self.input_frame = tk.Frame(window)
        self.input_frame.pack(pady=10)

        # Approach speed input
        approach_speed_label = tk.Label(self.input_frame, text="Approach Speed (Knots):")
        approach_speed_label.grid(row=0, column=0, sticky="e", padx=10, pady=5)
        self.approach_speed_entry = tk.Entry(self.input_frame)
        self.approach_speed_entry.grid(row=0, column=1, padx=10, pady=5)

        # Groundspeed input
        groundspeed_label = tk.Label(self.input_frame, text="Groundspeed (Knots):")
        groundspeed_label.grid(row=1, column=0, sticky="e", padx=10, pady=5)
        self.groundspeed_entry = tk.Entry(self.input_frame)
        self.groundspeed_entry.grid(row=1, column=1, padx=10, pady=5)

        # Wind component input
        wind_component_label = tk.Label(self.input_frame, text="Wind Component (Knots):")
        wind_component_label.grid(row=2, column=0, sticky="e", padx=10, pady=5)
        self.wind_component_entry = tk.Entry(self.input_frame)
        self.wind_component_entry.grid(row=2, column=1, padx=10, pady=5)

        # Pressure altitude input
        pressure_altitude_label = tk.Label(self.input_frame, text="Pressure Altitude (feet):")
        pressure_altitude_label.grid(row=3, column=0, sticky="e", padx=10, pady=5)
        self.pressure_altitude_entry = tk.Entry(self.input_frame)
        self.pressure_altitude_entry.grid(row=3, column=1, padx=10, pady=5)

        # Temperature input
        temperature_label = tk.Label(self.input_frame, text="Temperature (°C):")
        temperature_label.grid(row=4, column=0, sticky="e", padx=10, pady=5)
        self.temperature_entry = tk.Entry(self.input_frame)
        self.temperature_entry.grid(row=4, column=1, padx=10, pady=5)

        # Calculate button
        calculate_frame = tk.Frame(window)
        calculate_frame.pack(pady=10)
        calculate_button = tk.Button(calculate_frame, text="Calculate", command=self.calculate_distance, bg="#4CAF50", fg="black", padx=10, pady=5)
        calculate_button.pack()

        # Output label
        self.output_frame = tk.Frame(window)
        self.output_frame.pack(pady=10)
        self.output_label = tk.Label(self.output_frame, text="Total Distance Required:", font=("Helvetica", 12, "bold"))
        self.output_label.pack()

    def calculate_distance(self):
        # Get the values from the input fields
        approach_speed = float(self.approach_speed_entry.get())
        groundspeed = float(self.groundspeed_entry.get())
        wind_component = float(self.wind_component_entry.get())
        pressure_altitude = float(self.pressure_altitude_entry.get())
        temperature = float(self.temperature_entry.get())

        # Calculate the total distance required to land
        density_altitude = pressure_altitude + (120 * (temperature - 15))
        total_distance = (approach_speed / groundspeed) * (approach_speed + (2 * wind_component)) * (density_altitude / 1000)

        # Display the result
        result = f"Total Distance Required: {total_distance:.2f} feet"
        self.output_label.config(text=result, font=("Helvetica", 12))


