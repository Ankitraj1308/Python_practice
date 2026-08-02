num = int(input("enter a num to reverse "))
newnum = 0
while(num != 0):
  dig = num%10
  num = num//10
  newnum = newnum * 10 + dig
print(newnum)
