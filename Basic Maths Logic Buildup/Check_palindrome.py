num=int(input("Enter a number: "))
orig=num
rev=0
while num > 0:
    digit=num%10
    rev=rev*10+digit
    num//=10
if orig==rev:
    print("Palindrome")
else:
    print("Not Palindrome")


# s = input("Enter a string: ")
# print("Palindrome" if s == s[::-1] else "Not Palindrome")
