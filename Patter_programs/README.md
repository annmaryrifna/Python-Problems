
# Python Pattern Programs

## 1. Right Triangle Star Pattern

```text
*
**
***
****
*****
```

```python
for i in range(1, 6):
    print("*" * i)
```

---

## 2. Inverted Right Triangle Star Pattern

```text
*****
****
***
**
*
```

```python
for i in range(5, 0, -1):
    print("*" * i)
```

---

## 3. Pyramid Pattern

```text
    *
   ***
  *****
 *******
*********
```

```python
for i in range(1, 6):
    print(" " * (5 - i) + "*" * (2 * i - 1))
```

---

## 4. Diamond Pattern

```text
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```

```python
for i in range(1, 6):
    print(" " * (5 - i) + "*" * (2 * i - 1))

for i in range(4, 0, -1):
    print(" " * (5 - i) + "*" * (2 * i - 1))
```

---

## 5. Hollow Square Pattern

```text
*****
*   *
*   *
*   *
*****
```

```python
n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
```

---

## 6. Hollow Pyramid Pattern

```text
    *
   * *
  *   *
 *     *
*********
```

```python
n = 5

for i in range(n):
    print(" " * (n - i - 1), end="")

    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
```

---

## 7. Number Right Triangle Pattern

```text
1
12
123
1234
12345
```

```python
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
```

---

## 8. Number Pyramid Pattern

```text
    1
   121
  12321
 1234321
123454321
```

```python
for i in range(1, 6):

    print(" " * (5 - i), end="")

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()
```

---

## 9. Floyd's Triangle

```text
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
```

```python
num = 1

for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
```

---

## 10. Pascal's Triangle

```text
        1
      1 1
    1 2 1
  1 3 3 1
1 4 6 4 1
```

```python
n = 5

for i in range(n):
    num = 1

    print(" " * (n - i), end="")

    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)

    print()
```

---

## 11. Alphabet Right Triangle Pattern

```text
A
AB
ABC
ABCD
ABCDE
```

```python
for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end="")
    print()
```

---


---

## 12. Butterfly Pattern

```text
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
```

```python
n = 5

for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

for i in range(n - 1, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
```

---

## 13. Cross Pattern (X Pattern)

```text
*   *
 * *
  *
 * *
*   *
```

```python
n = 5

for i in range(n):
    for j in range(n):

        if i == j or i + j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print()
```

---
## 14. Plus Pattern

```text
  *
  *
*****
  *
  *
```

```python
n = 5

for i in range(n):
    for j in range(n):

        if i == n // 2 or j == n // 2:
            print("*", end="")
        else:
            print(" ", end="")

    print()
```

---

## 15. Alphabet C Pattern

```text
*****
*
*
*
*****
```

```python
n = 5

for i in range(n):
    for j in range(n):

        if i == 0 or i == n - 1 or j == 0:
            print("*", end="")
        else:
            print(" ", end="")

    print()
```

---

## 16. Alphabet H Pattern

```text
*   *
*   *
*****
*   *
*   *
```

```python
n = 5

for i in range(n):
    for j in range(n):

        if j == 0 or j == n - 1 or i == n // 2:
            print("*", end="")
        else:
            print(" ", end="")

    print()
```

---

## 17. Alphabet I Pattern

```text
*****
  *
  *
  *
*****
```

```python
n = 5

for i in range(n):
    for j in range(n):

        if i == 0 or i == n - 1 or j == n // 2:
            print("*", end="")
        else:
            print(" ", end="")

    print()
```

---

## 18. Alphabet L Pattern

```text
*
*
*
*
*****
```

```python
n = 5

for i in range(n):
    for j in range(n):

        if j == 0 or i == n - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print()
```

---

## 19. Alphabet U Pattern

```text
*   *
*   *
*   *
*   *
*****
```

```python
n = 5

for i in range(n):
    for j in range(n):

        if j == 0 or j == n - 1 or i == n - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print()
```

---

## 20. Alphabet E Pattern

```text
*****
*
*****
*
*****
```

```python
n = 5

for i in range(n):
    for j in range(n):

        if i == 0 or i == n - 1 or i == n // 2 or j == 0:
            print("*", end="")
        else:
            print(" ", end="")

    print()
```
