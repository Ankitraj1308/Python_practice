salary = float(input("enter your salary:"))
tax = salary*0.1 if salary <= 50000 else salary*0.2
print(tax)
inhand = salary-tax
print(inhand)