'''Take a user input as integer N. Find out the sum from 1 to N. If any number if divisible by 5, then skip that number. And if the sum is greater than 300, don't need to calculate the sum further more. Print the final result. And don't use for loop to solve this problem.'''
n = int(input("enter a number: "))
sum = 0
i = 1
while(i<n):
  if(i%5!=0):
    if sum + i > 300:
      break
    sum += i
  i += 1
print(sum)

  
