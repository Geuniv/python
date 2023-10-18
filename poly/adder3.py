# adder3.py

# 실행하면 함수 2개를 사용했을 때와 동일한 결과가 출력됨

# Calculator 클래스로 만들어진 cal1, cal2 라는 별개의 계산기 ( 인스턴스 ) 가 각각의 역할을 수행함
# 계산기 ( cal1, cal2 ) 의 결과값 역시 다른 계산기 결과값과 상관없이 독립적인 결과값을 유지함
# 클래스를 이용하면 계산기의 개수가 늘어나더라도 인스턴스를 생성하기만 하면 되기 때문에 함수를 사용하는 경우와 달리 매우 간단해짐

class Calculator:
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result


cal1 = Calculator()
cal2 = Calculator()

print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))