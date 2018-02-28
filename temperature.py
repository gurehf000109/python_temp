from tkinter import* #tkinter 불러오기

def process(): # 함수생성
    temperature = float(e1.get()) # e1칸에 있는 수를 받아오기
    mytemp = (temperature-32)*5/9 # 화씨를 섭씨로 변경
    e2.delete(0,END) # 있던 숫자를 지우기
    e2.insert(0,str(mytemp)) # 새로 구한 값을 넣기

def process1():# 함수생성
    temperature = float(e2.get()) # 지역함수로써 같은 temperature을 써도됨
    mytemp = temperature*9/5+32 # 섭씨를 화씨로 변경
    e1.delete(0,END) # 있던 숫자를 지우기
    e1.insert(0,str(mytemp)) # 새로 구한 값을 넣기


window = Tk() # Tk창 생성
window.title("온도를 바꿔 드리죠!") # 이름변경
 
l1 = Label(window, text="화씨") # 라벨1생성 이름은 화씨
l2 = Label(window, text="섭씨") # 라벨2생성 이름은 섭씨
l1.grid(row=0, column=0) # 라벨1의 위치를 0,0(0이 맨처음수)에 넣기
l2.grid(row=1, column=0) # 라벨2의 위치를 0,1(하단)에 넣기

e1 = Entry(window, bg="yellow",fg="black") # 엔트리의 색과 글씨의 색정하기
e2 = Entry(window, bg="yellow",fg="black") # 엔트리의 색과 글씨의 색정하기
e1.grid(row=0, column=1) # 엔트리의 위치를 0,1(우측)넣기
e2.grid(row=1, column=1) # 엔트리의 위치를 1,1에 넣기

b1 = Button(window, text="화씨->섭씨",command=process) # 버튼의 이름과 적용될 함수넣기
b2 = Button(window, text="섭씨->화씨",command=process1) # 버튼의 이름과 적용될 함수넣기
b1.grid(row=2, column=0) # 버튼의 위치를 2,0에 넣기
b2.grid(row=2, column=1) # 버튼의 위치를 2,1에 넣기 

window.mainloop() # 루프생성

#위치의 모식도
#     0,0  1,0
#     0,1  1,1
#     0,2  1,2
