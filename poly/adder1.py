# adder1.py

# 함수를 이용해 계산기의 "더하기" 기능을 구현한 예는 다음과 같음

result = 0

def adder(num) :
    global result
    result += num
    return result

# 이전에 계산된 결과값을 유지하기 위해서 result 라는 전역 변수 ( global ) 를 사용했음
# 실행하면 예상한 대로 다음과 같은 결과값이 출력됨

print(adder(3))
print(adder(4))