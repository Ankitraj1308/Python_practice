'''
Add new item to list after a specified item
Write a program to add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
Output:
[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]'''

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].append(7000)

print(list1)




'''
Q2
Update no of items available
Suppose you are given a list of candy and another list of same size representing no of items of respective candy.

i.e -

candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
no_of_items = [10,20,34,74,32]
Write a program to show no. of items of each candy type.

Output:

Jelly Belly-10
Kit Kat-20
Double Bubble-34
Milky Way-74
Three Musketeers-32
'''

candy_list = ['Jelly Belly', 'Kit Kat', 'Double Bubble', 'Milky Way', 'Three Musketeers']
no_of_items = [10, 20, 34, 74, 32]

for i in range(len(candy_list)):
    print(candy_list[i] + "-" + str(no_of_items[i]))