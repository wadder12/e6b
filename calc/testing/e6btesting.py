import unittest
from tkinter import Tk
from tkinter.constants import DISABLED, NORMAL
from tkinter.test.support import AbstractTkTest

from calc.e6b import E6BCalculator

class E6BCalculatorTests(unittest.TestCase):
    def setUp(self):
        self.root = Tk()

    def tearDown(self):
        self.root.destroy()

    def test_calculation(self):
        calculator = E6BCalculator(self.root)

        # Simulate input values
        calculator.airspeed_entry.insert(0, "100")
        calculator.distance_entry.insert(0, "200")
        calculator.altitude_entry.insert(0, "10000")
        calculator.fuel_capacity_entry.insert(0, "50")
        calculator.initial_fuel_entry.insert(0, "25")
        calculator.fuel_rate.set(10)

        # Simulate button click
        calculator.animate_calculation()

        # Define a callback function to check the label's text
        def check_label_text():
            expected_text = "Time: 0.20 hours\nGroundspeed: 1000.00 knots\nFuel Consumption: 0.02 gallons\nFuel Remaining: 24.98 gallons"
            self.assertEqual(calculator.output_label.cget("text"), expected_text)

            # Check the button state
            self.assertEqual(calculator.output_frame.winfo_children()[0].cget("state"), NORMAL)

        # Delay for animation to finish
        self.root.after(2000, check_label_text)

        # Start the Tk event loop
        self.root.mainloop()

    def test_button_disabled_during_calculation(self):
        calculator = E6BCalculator(self.root)

        # Simulate input values
        calculator.airspeed_entry.insert(0, "100")
        calculator.distance_entry.insert(0, "200")
        calculator.altitude_entry.insert(0, "10000")
        calculator.fuel_capacity_entry.insert(0, "50")
        calculator.initial_fuel_entry.insert(0, "25")
        calculator.fuel_rate.set(10)

        # Simulate button click
        calculator.animate_calculation()

        # Check the button state
        self.assertEqual(calculator.output_frame.winfo_children()[0].cget("state"), DISABLED)

if __name__ == '__main__':
    unittest.main()
