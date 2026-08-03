'''
 A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The trace of robot movement is shown as the following:

UP 5
DOWN 3
LEFT 3
RIGHT 2
!
The numbers after the direction are steps.

! means robot stop there.

Please write a program to compute the distance from current position after a sequence of movement and original point.

If the distance is a float, then just print the nearest integer.

Example:

Input:

UP 5
DOWN 3
LEFT 3
RIGHT 2
!
Output:

2
'''
x = 0
y = 0

while True:
    s = input()

    if s == "!":
        break

    direction, steps = s.split()
    steps = int(steps)

    if direction == "UP":
        y = y + steps
    elif direction == "DOWN":
        y = y - steps
    elif direction == "LEFT":
        x = x - steps
    elif direction == "RIGHT":
        x = x + steps

distance = (x * x + y * y) ** 0.5

print(round(distance))