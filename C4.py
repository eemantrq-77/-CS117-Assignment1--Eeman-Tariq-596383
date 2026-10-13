def loaded_divider(vs, r1, r2, rl):
    parallel = (r2 * rl) / (r2 + rl)

    unloaded_voltage = vs * r2 / (r1 + r2)
    loaded_voltage = vs * parallel / (r1 + parallel)

    return unloaded_voltage, loaded_voltage


result = loaded_divider(12, 1000, 1000, 500)

print("Unloaded voltage =", result[0], "V")
print("Loaded voltage =", result[1], "V")

