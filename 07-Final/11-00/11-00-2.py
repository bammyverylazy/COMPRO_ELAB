import numpy as np
filename = input("Enter filename: ")
zone = np.loadtxt(filename,delimiter=",",max_rows=1,dtype=str)
energy = np.loadtxt(filename,delimiter=",",skiprows=1)

# saimai's code
print("Total energy consumption for each day:")
for x in range(len(energy)):
  total_energy = np.sum(energy[x])
  print(f" Day {x+1} -> {total_energy:.2f}")

print()
print("Average energy consumption for each zone:")
for y in range(len(energy[0])):
  average_energy = np.mean(energy[:,y])
  print(f" {zone[y]} -> {average_energy:.2f}")

print()
print("Highest energy consumption:")
highest_energy = np.max(energy)
max_days, max_zones = np.where(energy == highest_energy)
for day_idx, zone_idx in zip(max_days, max_zones):
  print(f" Day {day_idx+1}, {zone[zone_idx]} -> {highest_energy:.2f}")

print()
print("Lowest energy consumption:")
lowest_energy = np.min(energy)
min_days, min_zones = np.where(energy == lowest_energy)
for day_idx, zone_idx in zip(min_days, min_zones):
  print(f" Day {day_idx+1}, {zone[zone_idx]} -> {lowest_energy:.2f}")

print()
print(f"Number of measurements greater than 160: {np.count_nonzero(energy>160)}")
