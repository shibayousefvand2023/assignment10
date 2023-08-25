class Fraction:
    def __init__(self , s, m):
        self.sorat = s
        self.makhraj = m

    def add(self, another):
        result_sorat = (self.s * another.m) + (another.s*self.m)
        result_makhraj = self.m * another.m
        return Fraction(result_sorat , result_makhraj)
    
    def multiply(self, another):
        result_sorat = self.s * another.s
        result_makhraj = self.m * another.m
        return Fraction(result_sorat , result_makhraj)
    
    def substract(self, another):
        result_sorat = (self.s * another.m) - (another.s*self.m)
        result_makhraj = self.m * another.m
        return Fraction(result_sorat , result_makhraj)
    
    def divide(self, another):
        result_sorat = self.s * another.m
        result_makhraj = self.m * another.s
        return Fraction(result_sorat , result_makhraj)
    
    def simplify(self):
        abc = self._abc(self.s , self.m)
        self.sorat //= abc
        self.makhraj //= abc

    def _abc(a,b):
        while b:
            a,b = b,a % b
            return a
        
    def __str__(self):
        return f"{self.s}/{self.m}"
    
    a = float(input("enter the high of the first fraction= "))
    b = float(input("enter the low of the first fraction= "))
    print(f"the first fraction is {a}/{b}")
    c = float(input("enter the high of the second fraction= "))
    d = float(input("enter the low of the second fraction= "))
    print(f"the first fraction is {c}/{d}")

    fraction1 = Fraction(a,b)
    fraction2 = Fraction(c,d)
    option=int(input("Enter your option with fractions \t 1_add 2_multiply 3_substract 4_divide"))

    if option==1:
        Add_result = fraction1.add(fraction2)
        print(f"Add: {Add_result}")
    elif option==2:
        print(f"({a}/{b}) + ({c}+{d}) =")
        Multipl_result = fraction1. multiply(fraction2)
        print(f"Multipl: {Multipl_result}")
    elif option==3:
        Substract_result = fraction1. substract(fraction2)
        print(f"Substract: {Substract_result}")
    elif option==4:
        Divided_result = fraction1. divide(fraction2)
        print(f"Divided: {Divided_result}")
    else:
        print("wrong option!")
    





        



