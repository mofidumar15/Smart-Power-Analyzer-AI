import numpy as np
import matplotlib.pyplot as plt

# ENTER DATA AS INPUT
days = int(input("ENTER YOUR TOTAL CONSUMPTION DAYS: "))
hours_per_day = float(input("ENTER HOW MANY HOURS YOU USE ELECTRICITY IN A DAY ON AN AVERAGE: "))
power_watt = float(input("ENTER TOTAL LOAD POWER (W): "))
price_per_kwh = float(input("ENTER PRICE PER KWH IN YOUR AREA (₹): "))

# DAILY ENERGY (kWh) USED
daily_energy = (power_watt * hours_per_day) / 1000

# MONTHLY ENERGY USED
total_energy = daily_energy * days

# COST OF USAGE
total_cost = total_energy * price_per_kwh

print("\n--- ANALYSIS OF THE POWER CONSUMPTION ---")
print(f"Daily Energy Consumption: {daily_energy:.2f} kWh")
print(f"Monthly Energy Consumption: {total_energy:.2f} kWh")
print(f"Total Electricity Cost: ₹{total_cost:.2f}")

# DAY-WISE SIMULATION OF POWER CONSUMPTION
daily_usage = np.random.normal(daily_energy, 0.2, days)

# PLOTING GRAPH
plt.plot(daily_usage, marker='o')
plt.title("Daily Power Consumption (kWh)")
plt.xlabel("Day")
plt.ylabel("Energy (kWh)")
plt.grid()
plt.show()
