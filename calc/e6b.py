import tkinter as tk

class E6BCalculator:
    def __init__(self, window):
        # Create the input frame
        self.input_frame = tk.Frame(window)
        self.input_frame.pack(pady=10)

        # Airspeed input
        airspeed_label = tk.Label(self.input_frame, text="Airspeed (Knots):")
        airspeed_label.grid(row=0, column=0, sticky="e", padx=10, pady=5)
        self.airspeed_entry = tk.Entry(self.input_frame)
        self.airspeed_entry.grid(row=0, column=1, padx=10, pady=5)

        # Distance input
        distance_label = tk.Label(self.input_frame, text="Distance (NM):")
        distance_label.grid(row=1, column=0, sticky="e", padx=10, pady=5)
        self.distance_entry = tk.Entry(self.input_frame)
        self.distance_entry.grid(row=1, column=1, padx=10, pady=5)

        # Fuel rate scale
        fuel_rate_label = tk.Label(self.input_frame, text="Fuel Consumption Rate (GPH):")
        fuel_rate_label.grid(row=2, column=0, sticky="e", padx=10, pady=5)
        self.fuel_rate = tk.Scale(self.input_frame, from_=5, to=20, orient=tk.HORIZONTAL, length=200)
        self.fuel_rate.set(10)  # Set the initial value
        self.fuel_rate.grid(row=2, column=1, padx=10, pady=5)

        # Altitude input
        altitude_label = tk.Label(self.input_frame, text="Altitude:")
        altitude_label.grid(row=3, column=0, sticky="e", padx=10, pady=5)
        self.altitude_entry = tk.Entry(self.input_frame)
        self.altitude_entry.grid(row=3, column=1, padx=10, pady=5)

        # Fuel capacity input
        fuel_capacity_label = tk.Label(self.input_frame, text="Fuel Capacity (Gallons):")
        fuel_capacity_label.grid(row=4, column=0, sticky="e", padx=10, pady=5)
        self.fuel_capacity_entry = tk.Entry(self.input_frame)
        self.fuel_capacity_entry.grid(row=4, column=1, padx=10, pady=5)

        # Initial fuel input
        initial_fuel_label = tk.Label(self.input_frame, text="Initial Fuel (Gallons):")
        initial_fuel_label.grid(row=5, column=0, sticky="e", padx=10, pady=5)
        self.initial_fuel_entry = tk.Entry(self.input_frame)
        self.initial_fuel_entry.grid(row=5, column=1, padx=10, pady=5)

        # Calculate button
        calculate_frame = tk.Frame(window)
        calculate_frame.pack(pady=10)
        calculate_button = tk.Button(calculate_frame, text="Calculate", command=self.animate_calculation, bg="#4CAF50", fg="black", padx=10, pady=5)
        calculate_button.pack()

        # Output label
        self.output_frame = tk.Frame(window)
        self.output_frame.pack(pady=10)
        self.output_label = tk.Label(self.output_frame, text="Result:", font=("Helvetica", 12, "bold"))
        self.output_label.pack()

    def animate_calculation(self):
    # Disable the Calculate button during animation
        calculate_button = self.output_frame.winfo_children()[0]
        calculate_button.config(state=tk.DISABLED)

        # Get the values from the input fields
        airspeed = float(self.airspeed_entry.get())
        distance = float(self.distance_entry.get())
        fuel_rate = self.fuel_rate.get()
        altitude = self.altitude_entry.get()
        fuel_capacity = float(self.fuel_capacity_entry.get())
        initial_fuel = float(self.initial_fuel_entry.get())

        # Clear the output label
        self.output_label.config(text="Calculating...", font=("Helvetica", 12))

        # Perform the calculation step by step with animation
        self.animate_time(0, distance, airspeed, fuel_rate, altitude, fuel_capacity, initial_fuel)

    def animate_time(self, step, distance, airspeed, fuel_rate, altitude, fuel_capacity, initial_fuel):
        if step <= 10:
            time = distance / airspeed * step / 10
            result = f"Time: {time:.2f} hours"
            self.output_label.config(text=result, font=("Helvetica", 12))

            # Animate the label color change
            if step % 2 == 0:
                self.output_label.config(fg="red")
            else:
                self.output_label.config(fg="black")

            # Animate the label size change
            font_size = 12 + step
            self.output_label.config(font=("Helvetica", font_size, "bold"))

            self.output_label.after(100, lambda: self.animate_time(step + 1, distance, airspeed, fuel_rate, altitude, fuel_capacity, initial_fuel))
        else:
            self.animate_groundspeed(0, distance, airspeed, fuel_rate, altitude, fuel_capacity, initial_fuel)

    def animate_groundspeed(self, step, distance, airspeed, fuel_rate, altitude, fuel_capacity, initial_fuel):
        if step <= 10:
            time = distance / airspeed
            groundspeed = distance / time * step / 10
            result = f"Time: {time:.2f} hours\nGroundspeed: {groundspeed:.2f} knots"
            self.output_label.config(text=result, font=("Helvetica", 12))

            # Animate the label color change
            if step % 2 == 0:
                self.output_label.config(fg="blue")
            else:
                self.output_label.config(fg="black")

            # Animate the label size change
            font_size = 12 + step
            self.output_label.config(font=("Helvetica", font_size, "bold"))

            self.output_label.after(100, lambda: self.animate_groundspeed(step + 1, distance, airspeed, fuel_rate, altitude, fuel_capacity, initial_fuel))
        else:
            self.animate_fuel_consumption(distance, airspeed, fuel_rate, altitude, fuel_capacity, initial_fuel)

    def animate_fuel_consumption(self, distance, airspeed, fuel_rate, altitude, fuel_capacity, initial_fuel):
        time = distance / airspeed
        groundspeed = distance / time * 60
        fuel_consumption = time * fuel_rate
        fuel_remaining = initial_fuel - fuel_consumption
        result = f"Time: {time:.2f} hours\nGroundspeed: {groundspeed:.2f} knots\nFuel Consumption: {fuel_consumption:.2f} gallons\nFuel Remaining: {fuel_remaining:.2f} gallons"
        self.output_label.config(text=result, font=("Helvetica", 12))

        # Animate the label color change
        self.output_label.config(fg="green")

        # Animate the label size change
        self.output_label.config(font=("Helvetica", 18, "bold"))

        # Re-enable the Calculate button after animation
        calculate_button = self.output_frame.winfo_children()[0]
        calculate_button.config(state=tk.NORMAL)

