reservoir_volume = 4.445e8
rainfall = 5e6
rainfall *= 0.9
reservoir_volume += rainfall
reservoir_volume *= 1.05
reservoir_volume *= 0.95
reservoir_volume -= 2.5e5
print(reservoir_volume)
