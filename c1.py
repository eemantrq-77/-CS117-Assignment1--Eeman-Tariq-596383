def ohms_current(voltage,resistance):
    return voltage / resistance

def power_dissipated(current, resistance):
    return current ** 2 * resistance

# Given values
voltage = 12
resistance = 6


current = ohms_current(voltage, resistance)

power = power_dissipated(current, resistance)


print("Current =", current, "A")
print("Power =", power, "W")
