# if 조건식 코드

A,B = map(int,input().split())

if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')

# 삼항연산자 코드


A,B = map(int,input().split())

print('>') if A > B else print('<') if A < B else print('==')