class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    def __str__(self):
        return f"{self.year} - {self.month:02d} - {self.day:02d}"
    
    def month_name_1(self):
        month_name = ['f', 'o', 'kh', 't', 'm', 'sh', 'm', 'ab', 'az', 'day', 'b', 'e']
        return month_name[self.month -1]
    
    def add(self, another_date):
        carry = 0

        new_day = self.day + another_date.day
        if new_day>30:
            new_day-=30
            carry =1

        new_month = self.month + another_date.month + carry
        if new_month>12:
           new_month-=12
           carry =1 
        else:
            carry = 0

        new_year = self.year + another_date.year + carry
        return Date(new_year, new_month,  new_day)
    
    def substract(self, another_data):
        year_difer = self.year - another_data.year
        month_difer = self.month - another_data.month
        day_difer = self.day - another_data.day
        if day_difer<0:
            month_difer-=1
            day_difer+=30

        if month_difer<0:
            year_difer-=1
            month_difer+=12
        return Date(year_difer, month_difer, day_difer)
    
a = int(input('enter the 1th date year ='))
b = int(input('enter the 1th date month ='))
c = int(input('enter the 1th date day ='))
d = int(input('enter the 2th date year ='))
e = int(input('enter the 2th date month ='))
f = int(input('enter the 2th date day ='))

date1 = Date(a, b, c)
date2 = Date(d, e, f)
option = int(input('what do you do? 1-add, 2-substract, 3-month name'))
if option==1:
    result_add= date1.add(date2)
    print(f'Add: {date1} + {date2} = {result_add}')
elif option==2:
    result_substract= date1.substract(date2)
    print(f'Substract: {date1} + {date2} = {result_substract}')
elif option==3:
    month_name= date1.month_name_1()
    print(f'Month_name: {month_name}')
else:
    print('wrong data!')