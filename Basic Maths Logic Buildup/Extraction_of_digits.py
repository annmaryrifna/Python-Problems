num=int(input("Enter a number: "))
digits=[]
while num > 0:
    digit=num%10     
    digits.append(digit)
    num //=10           

digits.reverse() 
print("Digits:",digits)


# num = int(input("Enter an integer: "))
# digits = [int(ch) for ch in str(num)]
# print("Digits:", digits)

num=int(input("Enter a number: "))
digits =list(map(int, str(num)))
print("Digits:", digits)
