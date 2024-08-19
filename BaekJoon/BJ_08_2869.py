# 백준 단계별로 풀어보기 챕터 8 ( 일반 수학 1 )
# 2869 ( 달팽이는 올라가고 싶다 )

A, B, V = map(int, input().split())

x = (V-B)/(A-B)
if x == int(x):
    print(int(x))
else:
    print(int(x) + 1)