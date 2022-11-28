h = (input("Enter num h: "))
for j in range(h):
    print(" " * (h - x), "*" * (2*x + 1))
for j in range(h - 2, -1, -1):
    print(" " * (h - x), "*" * (2*x + 1))
