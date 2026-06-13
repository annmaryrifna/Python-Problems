# Python Basic Programs

## 1. Add Two Numbers

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sum = a + b
print("Sum =", sum)

#print("Sum =", sum([a, b]))
```

---

## 2. Maximum of Two Numbers

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Maximum =", a)
else:
    print("Maximum =", b)

#print("Maximum =", max(a, b))
```

---

## 3. Factorial of a Number

```python
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial =", fact)

#import math
#print("Factorial =", math.factorial(n))
```

---

## 4. Check Even or Odd Number

```python
n = int(input("Enter a number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

#result = lambda x: "Even" if x % 2 == 0 else "Odd"
#print(result(n))
```

---

## 5. Swap Two Variables

```python
a = int(input("Enter a: "))
b = int(input("Enter b: "))
temp = a
a = b
b = temp

#a, b = b, a

print("a =", a)
print("b =", b)
```

---

## 6. Reverse a Number

```python
n = int(input("Enter number: "))
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10
print("Reverse =", rev)

#print("Reverse =", n[::-1])
```

---

## 7. Find GCD of Two Numbers

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
gcd = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i
print("GCD =", gcd)

#import math
#print("GCD =", math.gcd(a, b))
```

---

## 8. Find Sum of Digits

```python
n = int(input("Enter number: "))
sumofd = 0
while n > 0:
    sumofd += n % 10
    n //= 10
print("Sum =", sumofd)

#n = input("Enter number: ")
#print("Sum =", sum(map(int, n)))
```

---

## 9. Check Armstrong Number

```python
n = int(input("Enter number: "))
temp = n
dlen = len(str(n))
total = 0
while temp > 0:
    digit = temp % 10
    total += digit ** dlen
    temp //= 10
if total == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
```

---

## 10. Find Simple Interest

```python
p = float(input("Principal: "))
r = float(input("Rate: "))
t = float(input("Time: "))
si = (p * r * t) / 100
print("Simple Interest =", si)
```

---

## 11. Find Compound Interest

```python
p = float(input("Principal: "))
r = float(input("Rate: "))
t = float(input("Time: "))

amount = p * (1 + r / 100) ** t
ci = amount - p
print("Compound Interest =", ci)
```

---

## 12. Find Area of Circle

```python
radius = float(input("Enter radius: "))
area = 3.14159 * radius * radius
#area=math.pi * radius ** 2
print("Area =", area)
```

---

## 13. Print All Prime Numbers in an Interval

```python
start = int(input("Start: "))
end = int(input("End: "))
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
```


---

## 14. Check Prime Number

```python
n = int(input("Enter number: "))
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")
```

---

## 15. Nth Fibonacci Number

```python
n = int(input("Enter n: "))
a, b = 0, 1
for i in range(n - 1):
    a, b = b, a + b

print(a)
```

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(6))
```

---

## 16. Check if a Number is Fibonacci

```python
n = int(input("Enter number: "))

a, b = 0, 1
while b < n:
    a, b = b, a + b

if b == n or n == 0:
    print("Fibonacci Number")
else:
    print("Not Fibonacci Number")
```

---

## 17. Nth Multiple in Fibonacci Series

```python
n = int(input("Enter n: "))
count = 0
a, b = 0, 1

while count < n:
    if b % 3 == 0:
        count += 1

        if count == n:
            print(b)

    a, b = b, a + b
```

---

## 18. Print ASCII Value of Character

```python
ch = input("Enter character: ")
print(ord(ch))
```

---

## 19. Sum of Squares of First n Natural Numbers

```python
n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    total += i * i
print(total)

#print(n*(n+1)*(2*n+1)//6)
```

---

## 20. Cube Sum of First n Natural Numbers

```python
n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    total += i ** 3
print(total)

#print((n*(n+1)//2) ** 2)
```

---
