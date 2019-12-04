import os

def calc(x):
    return int(x/3) - 2

total_fuel = 0

with open('input', 'r') as f:
    modules = f.readlines()
    for module in modules:
        fuel_required = int(int(module)/3) - 2
        total_fuel += fuel_required
        while calc(fuel_required) > 0:
            fuel_required = calc(fuel_required)
            total_fuel += fuel_required

print(total_fuel)
