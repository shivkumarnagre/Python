'''Write a python program to check whether the given character is vowel or consonant

Input format:

The input consist of a character

Output format:

The output consists of a below-given string “Vowel” / “Consonant” / “Not an alphabet”

Sample Input:

a

Sample Output:

Vowel

'''


ch=input()
vowel=['a','e','i','o','u','A','E','I','O','U']

if ((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
  if ch in vowel:
    print("Vowel")
  else:
    print("Consonant")
else:
  print("Not an alphabet")
