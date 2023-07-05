import tkinter as tk
from math import sqrt, atan, tan, degrees

# Create a tkinter application
app = tk.Tk()
app.title("E6B Calculator")

# Function to calculate True Airspeed (TAS)
def calculate_tas():
    ias = float(ias_entry.get())
    alt = float(altitude_entry.get())
    tat = float(tat_entry.get())
    isa = float(isa_entry.get())

    tas = ias + (ias * (alt/1000) * 0.02)
    tas = tas * sqrt(tat/isa)

    tas_result_label.config(text=f"TAS: {tas:.2f} knots")

# Function to calculate Density Altitude (DA)
def calculate_da():
    pa = float(pressure_altitude_entry.get())
    oat = float(outside_air_temp_entry.get())
    isa_entry_value = isa_entry.get()

    if isa_entry_value:
        isa = float(isa_entry_value)
        da = pa + (120 * (oat - isa))
        da_result_label.config(text=f"Density Altitude: {da:.2f} feet")
    else:
        # Handle the case when the isa_entry is empty or not a valid float
        da_result_label.config(text="Invalid input for ISA")


# Function to calculate Wind Correction Angle (WCA) and Groundspeed (GS)
def calculate_wind_correction():
    tas = float(tas_wc_entry.get())
    wind_component = float(wind_component_entry.get())

    wca = degrees(atan(wind_component / tas))
    gs = tas - wind_component

    wca_result_label.config(text=f"Wind Correction Angle: {wca:.2f} degrees")
    gs_result_label.config(text=f"Groundspeed: {gs:.2f} knots")

# Create the GUI components
ias_label = tk.Label(app, text="Indicated Airspeed (IAS):")
ias_entry = tk.Entry(app)

altitude_label = tk.Label(app, text="Altitude (in thousands):")
altitude_entry = tk.Entry(app)

tat_label = tk.Label(app, text="Total Air Temperature (TAT):")
tat_entry = tk.Entry(app)

isa_label = tk.Label(app, text="International Standard Atmosphere (ISA) temperature:")
isa_entry = tk.Entry(app)

calculate_tas_button = tk.Button(app, text="Calculate TAS", command=calculate_tas)
tas_result_label = tk.Label(app, text="TAS: ")

pressure_altitude_label = tk.Label(app, text="Pressure Altitude:")
pressure_altitude_entry = tk.Entry(app)

outside_air_temp_label = tk.Label(app, text="Outside Air Temperature (OAT):")
outside_air_temp_entry = tk.Entry(app)

calculate_da_button = tk.Button(app, text="Calculate DA", command=calculate_da)
da_result_label = tk.Label(app, text="Density Altitude: ")

tas_wc_label = tk.Label(app, text="True Airspeed (TAS):")
tas_wc_entry = tk.Entry(app)

wind_component_label = tk.Label(app, text="Wind Component:")
wind_component_entry = tk.Entry(app)

calculate_wind_correction_button = tk.Button(app, text="Calculate Wind Correction", command=calculate_wind_correction)
wca_result_label = tk.Label(app, text="Wind Correction Angle: ")
gs_result_label = tk.Label(app, text="Groundspeed: ")

# Arrange the GUI components using the grid layout
ias_label.grid(row=0, column=0, sticky="e")
ias_entry.grid(row=0, column=1)

altitude_label.grid(row=1, column=0, sticky="e")
altitude_entry.grid(row=1, column=1)

tat_label.grid(row=2, column=0, sticky="e")

tat_entry.grid(row=2, column=1)

isa_label.grid(row=3, column=0, sticky="e")
isa_entry.grid(row=3, column=1)

calculate_tas_button.grid(row=4, column=0, columnspan=2)
tas_result_label.grid(row=5, column=0, columnspan=2)

pressure_altitude_label.grid(row=6, column=0, sticky="e")
pressure_altitude_entry.grid(row=6, column=1)

outside_air_temp_label.grid(row=7, column=0, sticky="e")
outside_air_temp_entry.grid(row=7, column=1)

calculate_da_button.grid(row=8, column=0, columnspan=2)
da_result_label.grid(row=9, column=0, columnspan=2)

tas_wc_label.grid(row=10, column=0, sticky="e")
tas_wc_entry.grid(row=10, column=1)

wind_component_label.grid(row=11, column=0, sticky="e")
wind_component_entry.grid(row=11, column=1)

calculate_wind_correction_button.grid(row=12, column=0, columnspan=2)
wca_result_label.grid(row=13, column=0, columnspan=2)
gs_result_label.grid(row=14, column=0, columnspan=2)

# Start the tkinter event loop
app.mainloop()
