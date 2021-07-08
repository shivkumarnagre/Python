'''Get two integers x and y from the user and write a python program to relate 2 integers as equal to, less than or greater than.

Input format:

Input consist of 2 integers The first input corresponds to the first number(x) The second input corresponds to the second number(y)

Output format:

If the first number is equal to the second number, print "x and y are equal". Otherwise, print "x greater than y" or "x less than y"

Sample Input:

17

12

Sample Output:

17 greater than 12'''


x=int(input())
y=int(input())
if x==y:
  print("{} equal to {}".format(x,y))
elif x>y:
  print("{} greater than {}".format(x,y))
else:
  print("{} less than {}".format(x,y))
  
