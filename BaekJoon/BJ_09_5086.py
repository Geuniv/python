# 백준 단계별로 풀어보기 챕터 9 ( 약수, 배수와 소수 )
# 5086 ( 배수와 약수 )

while (1):
    x,y = map(int,input().split())

    if x==0 and y==0:
        break

    if x<y and y%x==0:
        print("factor")
    elif x>y and x%y==0:
        print("multiple")
    else:
        print("neither")