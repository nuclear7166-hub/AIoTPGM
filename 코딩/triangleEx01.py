n = int(input("라인수를 입력하세요: "))

print("직각 삼각형:")
for i in range(1, n + 1):
    print("*" * i)

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)

print("\n삼각형:")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

print("\n마름모:")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
