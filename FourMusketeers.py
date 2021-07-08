'''Dhoni joined the group of 3 Musketeers and now their group is called four Musketeers. Meanwhile, Dhoni also moved to a new house in the same locality nearby to the other three. Currently, the houses of Sachin, Dravid and Ganguly are located in the shape of a triangle. When the three musketeers asked Dhoni about the location of his house, he said that his house is equidistant from the houses of the other 3. Can you please help them find out the location of the house? Given the 3 locations {(a1,b1), (a2,b2) and (a3,b3)} of a triangle, write a program to determine the point which is equidistant from all the 3 points.



INPUT FORMAT:

Input consists of 6 integers.

The first integer corresponds to a1.

The second integer corresponds to b1.

The third and fourth integers correspond to a2 and b2 respectively.

The fifth and sixth integers correspond to a3 and b3 respectively.



OUTPUT FORMAT:

The output consists of two floating point numbers which correspond to the location of the house.



SAMPLE INPUT: 

2

4

10

15

5

8 



SAMPLE OUTPUT: 

5.66667

9.0'''



a1=float(input())
b1=float(input())
a2=float(input())
b2=float(input())
a3=float(input())
b3=float(input())
print((a1+a2+a3)/3) 
print((b1+b2+b3)/3)
