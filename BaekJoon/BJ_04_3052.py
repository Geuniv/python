# 1 : for문을 사용한 풀이법
arr = []
for i in range(10):
    a = int(input())
    if a%42 not in arr:
        arr.append(a % 42)
print(len(arr))

# 2 : set()함수를 사용한 풀이법
arr = []
for i in range(10):
    a = int(input())
    arr.append(a % 42)
print(len(set(arr)))
