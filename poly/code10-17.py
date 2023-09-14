# code 10 - 17.py

from tkinter import *

window = Tk()

# 7행에서 Menu ( 부모윈도우 ) 로 mainMenu 변수를 생성함 ( mainMenu는 메뉴 자체를 나타내는 변수임 )
mainMenu = Menu(window)
window.config(menu = mainMenu)

# 10 ~ 11행은 상위 메뉴인 [ 파일 ] 을 생성을 생성하고 메뉴 자체에 부착함
# [ 파일 ] 메뉴는 선택하고 끝나는 것이 아니라, 그 아래에 다른 메뉴가 확장되어야 하므로 add_cascade() 함수를 사용함
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)

# 12행에서는 [ 파일 ] 메뉴의 하위에 [ 열기 ] 메뉴를 준비함. 열기 메뉴는 선택할 때 어떤 작동을 해야 하므로, add_command () 함수를 사용함
fileMenu.add_command(label = "열기")

# 13행은 메뉴 사이에 구분선을 넣음
fileMenu.add_separator()
fileMenu.add_command(label = "종료")

window.mainloop()