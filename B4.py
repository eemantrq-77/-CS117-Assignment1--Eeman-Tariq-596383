Voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]

longest = 0
current = 1

start_Voltage = Voltages[0]
end_start = Voltages[0]

current_start = Voltages[0]

for i in range(1, len(Voltages)):
    if Voltages[i] < Voltages[i - 1]:
        current = current + 1
    else:
        current = 1
        current_start = Voltages[i]

    if current > longest:
        longest = current
        start_Voltage = current_start
        end_start = Voltages[i]

print("Longest continuous drop:", longest, "minutes")
print("Started at:", start_Voltage, "V")
print("Ended at:", end_start, "V")
