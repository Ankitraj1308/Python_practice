salary = float(input("enter your salary:"))
tax = salary*0.1 if salary <= 50000 else salary*0.2
print(tax)
inhand = salary-tax
print(inhand)


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if(n%2 != 0):
        print("Weird")
    elif((n%2==0) and (n>=2 and n<=5)):
        print("Not Weird")
    elif((n%2==0) and (n>=6 and n<=20)):
        print("Weird")
    elif((n%2==0) and (n>20)):
        print("Not Weird")
