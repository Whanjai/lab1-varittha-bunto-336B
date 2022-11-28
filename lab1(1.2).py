h= int(input("Enter the desired number = "))
a = 0
for i in range(1, h + 1):
    for j in range(1, h - i + 1):
        print(end = ' ')
    while a != 2 * i - 1:
        print('*', end = '')
        a = a + 1
    a = 0
    print()
a = 2
l = 1
for i in range(1, h):
    for j in range(1, a):
        print(end = ' ')
    a = a + 1
    while l <= (2 * (h - i) - 1):
        print('*', end = '')
        l = l + 1
    l = 1
