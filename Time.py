class Time:
    def __init__(self, hours, miunates):
        self.hours = hours
        self.minuates = miunates

    def __str__(self):
        return f"{self.hours:02d}:{self.minuates:02d}"
    
    def to_seconds(self):
        return self.hours * 3600 + self.minuates *60
    
    def from_seconds(seconds):
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        return Time(hours , minutes)
    
    def add(self, another_time):
        total_minutes = self.hours * 60 + self.minuates + another_time.hours * 60 + another_time.minutes
        new_hours = total_minutes // 60
        new_minutes = total_minutes % 60
        return Time(new_hours, new_minutes)

a = int(input("hours of 1th time ="))
b = int(input("minutes of 1th time ="))
c = int(input("hours of 2th time ="))
d = int(input("minutes of 2th time ="))
time1 = Time(a, b)
time2 = Time(c, d)
option = int(input("what will you do?" 1-add times 2-substract 3-time to second 4-second to time"))
if option ==1:
    result_add = time1.add(time2)
    print(f"add:{time1} + {time2} = {result_add}")
elif optopn ==2:
    result_sustract = time1.substract(time2)
    print(f"substract:{time1} - {time2} = {result_substract}")
elif optopn ==3:
    time_seconds = time1.to second()
    print(f"{time1} in second: {time_seconds}")
elif optopn ==4:
    seconds = 10000
    time_from_seconds = Time.from_seconds(seconds)
    print(f"{seconds} seconds in time: {time.from_seconds}")
else:
print(wrong data)
    


                   