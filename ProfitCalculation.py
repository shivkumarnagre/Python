'''Each Sunday, a newspaper agency sells x copies of a certain newspaper for Rs.a per copy. The cost to the agency of each newspaper is Rs.b . The agency pays a fixed cost for storage, delivery and so on of Rs.100 per Sunday. The newspaper agency wants to calculate the profit obtained on sundays. Can you please help them out by writing a python program to compute the profit given x, a and b.



Input Format:

Input consists of 3 integers --- x, a and b. X is the number of copies sold, a is the cost per copy and b is the cost the agency spends per copy.

Output Format:

Refer Sample Input and Output for exact formatting specifications.



Sample Input :



1000

2

1



Sample Output:

The profit obtained is Rs.900'''


x=int(input())
a=int(input())
b=int(input())
sp=x*a
cp=x*b
profit=sp-cp-100
#profit=x*a-x*b-100 #Can do it in a single line
print("The profit obtained is Rs.",profit)
