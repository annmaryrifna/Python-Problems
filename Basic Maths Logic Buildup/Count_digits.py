num=int(input("Enter a number: "))
count=0
if num==0:
    count=1
else:
    while num > 0:
        num //= 10
        count += 1
print("Number of digits:",count)

# num=int(input("Enter a number: "))
# count=len(str(num))
# print("Number of digits:",count)
