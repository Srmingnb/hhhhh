import tkinter as tk
 
window = tk.Tk()
window.title('my window')
window.geometry('500x500')#ע�⣺����ĳ��ǡ�����*
 
var = tk.StringVar()    # ��ʱ���ֱ���������
l = tk.Label(window, 
    textvariable=var,   # ʹ�� textvariable �滻 text, ��Ϊ������Ա仯
    bg='green', font=('Arial', 12), width=15, height=2)
l.pack() 

b = tk.Button(window, 
    text='hit me',      # ��ʾ�ڰ�ť�ϵ�����
    width=15, height=2, 
  )     # �����ťʽִ�е�����
b.pack()    # ��ťλ��


 
window.mainloop()




























