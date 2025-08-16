num=int(input("Enter an number: "))
rev=0
while num > 0:
    digit=num % 10
    rev=rev*10+digit
    num//=10
print("Reversed number:",rev)

# num=int(input("Enter a number:"))
# rev=int(str(num)[::-1])
# print("Reversed number:", rev)