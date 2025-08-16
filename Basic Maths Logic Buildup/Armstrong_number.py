
num=int(input("Enter a number: "))
temp=num
order=len(str(num))
sumno=0
while temp>0:
    digit=temp%10
    sumno+=digit ** order
    temp//=10
if sumno==num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")