# Problem 10: A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The trace of robot movement is shown as the following:

# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# !
# The numbers after the direction are steps.

# ! means robot stop there.

# Please write a program to compute the distance from current position after a sequence of movement and original point.

# If the distance is a float, then just print the nearest integer.

# Example:

# Input:

# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# !

# Output:

# # 2



(x,y)=(0,0)
while True:   # run forever until i manually stops you
    user=input("enter value with direction: ")
    if(user!="!"):
        direct,value=user.split()
        value=int(value)
        if(direct=="up"):
            y+=value
        elif(direct=="down"):
            y-=value
        elif(direct=="left"):
            x-=value
        elif(direct=="right"):
            x+=value
    else:
        break


dist=((x**2)+(y**2))**(1/2)
print(dist)

   
   
    
