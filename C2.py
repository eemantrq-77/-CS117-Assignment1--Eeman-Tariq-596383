def parallel_resistance(resistors):
    reciprocal_sum = 0

    for resistance in resistors:
        reciprocal_sum = reciprocal_sum + 1 / resistance

    return 1 / reciprocal_sum


print(parallel_resistance([10, 10]))
print(round(parallel_resistance([100, 200, 300]), 2))
