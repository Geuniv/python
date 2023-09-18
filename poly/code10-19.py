# code 10 - 19.py

from tkinter import *
from tkinter import messagebox

# 함수 선언 부분
# 7 ~ 8행에서는 열기 메뉴를 선택하면 간단한 메시지 창이 열림
def func_open() :
    messagebox.showinfo("메뉴선택", "열기 메뉴를 선택함")

# 8 ~ 10행에서는 [ 종료 ] 메뉴를 선택하면 프로그램이 종료됨
def func_exit() :
    window.quit()
    window.destroy()

# 메인 코드 부분
window = Tk()

mainMenu = Menu(window)
window.config(menu = mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
# 22행에서는 [ 열기 ] 메뉴를 선택하면 무언가 작동을 해야 하므로 add_command() 함수를 사용함
# [ 파일 메뉴를 선택하면 하위 메뉴가확장되고, [ 열기 ]  메뉴를 선택하면 5행의 func_open() 함수가 실행됨
fileMenu.add_command(label = "열기", command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "종료", command = func_exit)

window.mainloop()