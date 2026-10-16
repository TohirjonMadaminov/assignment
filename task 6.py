batteries = [25, 80, 95, 60]
p = []
charge = int(input("Enter the amount of  charging: "))
for i in range(len(batteries)):
    l = batteries[i] + charge
    if l > 100:
        # batteries[i] = 100
        l = 100
    p.append(l)
level = p.pop()
print(f"Disconnected device: {level}%")
battery = int(input("Battery level of new device: "))
p.append(battery)
print(f"Battery levels: {p} ")



