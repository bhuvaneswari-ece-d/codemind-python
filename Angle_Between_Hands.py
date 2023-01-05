h,m=map(int,input().split(":"))
hour = 0.5 * (h * 60 + m)
minute= 6 * m
angle = abs(hour - minute)
angle = min(360 - angle, angle)
print(angle)