'''Swapping without third variable
Write a python program to swap two values without the use of 3rd variable. Input format: First input: an integer Second input: an integer Output format: The output will be integers(swapped values)

Sample Input:



10

20



Sample Output:



20

10'''
a=int(input())
b=int(input())
a,b=b,a
print(a)
print(b)
