"""
This is my unit converter
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Börjar med user friendly meddalande.
print("\n Welcome to Unit Converter! Ready to transform your measurements?\n")
# Använder float function med input istället för int, för att göra användare input mer flexible.
m = float(input("Enter current hight in meter over sea, and press enter:"))
v = float(input("Enter current velocity in km/h, and press enter:"))
t = float(input("Enter current outside temperature in °C, and press enter:"))
# Nu börjar jag göra beräkningarna för att konvertera enheterna .
fe = m * 3.28084
mph = v * 0.62137
f = (t * 9/5) + 32
# Använder .2f för att få två decimaler.
print(f"\nThe hight {m} m in feet over the see is {fe:.2f} feet")
print(f"The velocity {v} km/h in mph is {mph:.2f} mph")
print(f"The temperature {t} °C in Fahrenheit is {f:.2f} °F")
