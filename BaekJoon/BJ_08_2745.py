# 백준 단계별로 풀어보기 챕터 8 ( 일반 수학 1 )
# 2745 ( 진법 변환 )

# 예제 1
# 진법 변환에 사용할 숫자 리스트 (최대 36진법까지 지원).
num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 입력값을 읽어옴: 'n'은 'b' 진법의 숫자, 'b'는 진법.
n, b = input().split()

# 10진수 값을 저장할 변수를 초기화.
answer = 0

# 숫자 문자열 'n'을 거꾸로 뒤집어서 각 자리 숫자를 순회.
for i, num in enumerate(n[::-1]):
    # 각 자리 숫자의 10진수 값을 계산하여 더함.
    answer += int(b) ** i * num_list.index(num)

# 최종 결과 출력.
print(answer)

# 예제 2
# 입력값을 읽어옴: 'n'은 'b' 진법의 숫자, 'b'는 진법.
n, b = input().split()

# 파이썬의 int 함수는 두 번째 인자로 주어진 진법의 숫자를 10진수로 변환해줌.
print(int(n, int(b)))
