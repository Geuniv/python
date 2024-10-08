# 백준 단계별로 풀어보기 챕터 8 ( 일반 수학 1 )
# 2292 ( 벌집 )

# 입력된 숫자 (목적지의 숫자).
num = int(input())

# 벌집의 중앙 1번 방에서 시작하기 때문에 초기값은 1.
numbox = 1

# 레이어(겹)의 개수를 세는 변수. 초기값은 1로 시작.
cnt = 1

# 입력된 숫자가 현재 레이어의 최대 숫자보다 클 때까지 반복.
while num > numbox:
    # 각 레이어의 방의 개수는 이전 레이어의 방의 개수에 6을 곱한 값만큼 늘어남.
    numbox += 6 * cnt
    # 레이어 수 증가.
    cnt += 1

# 입력된 숫자가 위치한 레이어(겹)의 수를 출력.
print(cnt)