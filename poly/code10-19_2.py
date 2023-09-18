# code 10 - 19.py

# 대화상자의 생성과 사용
# 파이썬은 대화상자를 제공함
# 기본적인 메시지창을 표시하는 messagebox.showinfo() 이 있음
# 이외에도 숫자나 문자를 입력받을 수 있도록 tkinter.simpledialog 모듈을 임포트한 후 askinteger() 및 askstring() 등을 사용함
from tkinter import *
# 입력창을 사용하기 위해 4행의 tkinter.simpledialog 모듈을 임포트함
from tkinter.simpledialog import *

# 함수 선언 부분
window = Tk()
window.geometry("400x100")

# 10 ~ 11행에서는 레이블을 하나 준비함
label1 = Label(window, text = "입력된 값")
label1.pack()

# 13 ~ 14행에서 askinteger ("제목", "내용", 옵션) 함수로 입력 받음
# 옵션 중에 minvalue는 최소값이고 maxvalue는 최대값임
# 이 값을 벗어나서 입력하면 경고창을 표시하며 입력되지 않음
value = askinteger ("확대배수", "주사위 숫자(1~6)을 입력하세요",
                                minvalue = 1, maxvalue = 6)

# 16행에서 입력 받은 숫자를 문자열로 변경해서 레이블을 씀
# 실수를 입력 받으려면 askfloat() 함수를 사용하고, 문자열을 입력 받으려면 askstring() 함수를 사용함
label1.configure(text = str(value))
window.mainloop()