# # 배열 슬라이싱
a = int(input())
b = input()

print(a * int(b[2]))
print(a * int(b[1]))
print(a * int(b[0]))
print(a * int(b))

# for문 이용
a = int(input())
b = input()

for i in range(3, 0, -1) :
    print(a * int(b[i-1]))

print(a * int(b))

# int형식으로 연산
a = int(input())
b = int(input())

print(a * (b % 10))
print(a * (b % 100 // 10))
print(a * (b // 100))
print(a*b)