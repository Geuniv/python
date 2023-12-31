# 클래스 개녑 잡기
# 클래스라는 것이 마치 뽑기의 틀 ( 별 모양, 하트 모양 ) 과 비슷함
# 별 모양의 틀 ( 클래스 ) 로 찍으면 별 모양의 뽑기 ( 인스턴스 ) 가 생성되고 하트 모양의 틀 ( 클래스 ) 로 찍으면 하트 모양의 뽑기 ( 인스턴스 ) 가 나오는 것임
# 클래스란 똑같은 무엇인가를 계속해서 만들어낼 수 있는 설계 도면 같은 것이고 ( 뽑기 틀 ), 인스턴스란 클래스에 의해서 만들어진 피조물 ( 별 또는 하트가 찍힌 뽑기 ) 을 뜻함
# 다음은 클래스의 가장 간단한 예임

class Simple :
    pass

# 위의 클래스는 아무런 기능도 갖고 있지 않은 껍질뿐인 클래스임
# 하지만 이렇게 껍질뿐인 클래스도 인스턴스라는 것을 생성하는 기능을 가지고 있음
# 인스턴스는 클래스에 의해서 만들어진 객체로, 1개의 클래스는 무수히 많은 인스턴스를 만들어낼 수 있음

# 앞에서 만든 Simple 클래스의 인스턴스를 만드는 방법은 다음과 같음

a = Simple()

# Simple()의 결과 값을 돌려받은 a가 인스턴스임
# 마치 함수를 사용해서 그 결과값을 돌려받는 모습과 비슷함