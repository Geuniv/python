# 1번 코드
numbers = []
for _ in range(9):
    i = int(input())
    numbers.append(i)

print(max(numbers))
print(numbers.index(max(numbers)) + 1)

# 2번 코드
numbers = [int(input()) for _ in range(9)]

print(max(numbers))
print(numbers.index(max(numbers)) + 1)