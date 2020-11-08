a, b = input().split()
hour = int(a)
min = int(b)
if(min >= 45):
    print(f"{hour} {min-45}")
elif(min < 45 and hour != 0):
    print(f"{hour-1} {60-(45-min)}")
elif(min < 45 and hour == 0):
    print(f"23 {60-(45-min)}")

