# adder2.py

# 만약 한 프로그램에서 2개의 계산기가 필요한 상황이 발생하면 어떻게 해야 할까 ?
# 각각의 계산기는 각각의 결과값을 유지해야 하기 때문에 위와 같이 adder 함수 하나만으로는 결과값을 따로 유지할 수 없음
# 이런 상황을 해결하려면 아래와 같이 함수를 각각 따로 만들어야 함
# 똑같은 일을 하는 adder1과 adder2라는 함수가 만들어졌음
# 각각의 함수에서 계산된 결과값을 유지하면서 저장하기 위한 전역 변수 result1, result2가 필요하게 되었음
# 결과 값은 다음과 같이 출력됨

# 계산기 1의 결과값이 계산기 2에 영향을 끼치지 않음을 확인함
# 하지만 계산기가 3개, 5개, 10개로 점점 더 많이 필요해진다면 어떻게 할 것인가 ?
# 그 때마다 전역 변수와 함수를 추가할 것인가 ?
# 위와 같은 경우 클래스를 이용하면 다음과 같이 해결할 수 있음

result1 = 0
result2 = 0

def adder1(num) :
    global result1
    result1 += num
    return result1

def adder2(num) :
    global result2
    result2 += num
    return result2

print(adder1(3))
print(adder1(4))
print(adder2(3))
print(adder2(7))