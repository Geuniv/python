# marks3.py
# 60점 이상이라면 합격이라는 문장을 출력하는 예제를 range 함수를 이용하여 구현

marks = [90, 25, 67, 45, 80]

# len 함수는 리스트 내 요소의 개수를 돌려주는 함수임.
for number in range(len(marks)) :
    if marks[number] < 60 : continue
    print("%d번 학생 축하합니다. 합격입니다." % (number + 1))