import tkinter as tk#导入tkinter模块


input_num_ls=[]#用来接收输入的数据的列表


def add(sl):
    global input_num_ls

    input_num_ls.append(sl)

    current_value.set(input_num_ls)#在屏幕上显示输入的数据

def result():

    global input_num_ls

    string=''.join(input_num_ls)#将列表类型转换为字符串类型，方便用eval函数
    try:
      #异常处理，除数不能为零
      # eval函数将字符串当作表达式来运算，将结果输入在屏幕上

      current_value.set( eval(string))

    except ZeroDivisionError:

        current_value.set("You can't divide by zero!")





def clear():
    global input_num_ls
    input_num_ls = []
    current_value.set(0)

#界面布局

window =tk.Tk()#初始化窗口

window.title('我的计算器')#窗口题目

window.geometry('300x500')#窗口大小

screen_area = tk.Frame(width='400',height='100',bg='#ddd')#屏幕的布局位置

screen_area.pack()#window中显示出来

current_value = tk.StringVar()#显示数据
current_value.set(0)#在不计算的时候屏幕显示0

show_screen_lable=tk.Label(screen_area,textvariable=current_value,bg='white',width='400',height='2',font={'黑体',40,'bold'},anchor='e')#在屏幕处显示信息
show_screen_lable.pack(padx=10,pady=5)

button_area =tk.Frame(width='500',height='500',bg='#ccc')#按钮布局
button_area.pack(padx=10,pady=5)

#添加按钮
tk.Button(button_area,text='C',width='7',height='4',command=lambda :clear()).grid(row='1',column='0')
tk.Button(button_area, text='+', width='7', height='4', command=lambda: add('+')).grid(row='1', column='1')
tk.Button(button_area, text='-', width='7', height='4', command=lambda: add('-')).grid(row='1', column='2')
tk.Button(button_area, text='*', width='7', height='4', command=lambda: add('*')).grid(row='1', column='3')
tk.Button(button_area, text='7', width='7', height='4', command=lambda: add('7')).grid(row='2', column='0')
tk.Button(button_area, text='8', width='7', height='4', command=lambda: add('8')).grid(row='2', column='1')
tk.Button(button_area, text='9', width='7', height='4', command=lambda: add('9')).grid(row='2', column='2')
tk.Button(button_area, text='/', width='7', height='4', command=lambda: add('/')).grid(row='2', column='3')
tk.Button(button_area, text='4', width='7', height='4', command=lambda: add('4')).grid(row='3', column='0')
tk.Button(button_area, text='5', width='7', height='4', command=lambda: add('5')).grid(row='3', column='1')
tk.Button(button_area, text='6', width='7', height='4', command=lambda: add('6')).grid(row='3', column='2')
tk.Button(button_area, text='=', width='7', height='4', command=lambda: result()).grid(row='3', column='3')
tk.Button(button_area, text='1', width='7', height='4', command=lambda: add('1')).grid(row='4', column='0')
tk.Button(button_area, text='2', width='7', height='4', command=lambda: add('2')).grid(row='4', column='1')
tk.Button(button_area, text='3', width='7', height='4', command=lambda: add('3')).grid(row='4', column='2')
tk.Button(button_area, text='0', width='7', height='4', command=lambda: add('0')).grid(row='4', column='3')

window.mainloop()#循环执行窗口，没有他代码执行不了