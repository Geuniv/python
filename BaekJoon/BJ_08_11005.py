# 백준 단계별로 풀어보기 챕터 8 ( 일반 수학 1 )
# 11005 ( 진법 변환 2 )

# 풀이
# 진법의 index를 알기위한 arr (string)을 정의한다. (36진법 이하)
# N이 0이 될 때까지 s라는 string에 arr[N%B]가 의미하는 나머지 문자를 추가하고 N을 N//B로 초기화한다.
# s를 뒤집어서 출력한다.

N, B = map(int, input().split())
s = ''
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while N:
    s += str(arr[N%B])
    N //= B

print(s[::-1])