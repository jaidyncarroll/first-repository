print("Welcome to the Space Travel Calculator!")

distance = int(input("enter the distance to a celestial object in light years:"))
speed = int(input("enter the spacecraft speed in fraction of the speed of light:"))

time = distance/speed

print("It would take you", time, "hours to reach your destination, beep bop boop.")
