import tkinter as tk
 
window = tk.Tk()
window.title('my window')
window.geometry('500x500')#注意：这里的乘是×不是*
 
var = tk.StringVar()    # 这时文字变量储存器
l = tk.Label(window, 
    textvariable=var,   # 使用 textvariable 替换 text, 因为这个可以变化
    bg='green', font=('Arial', 12), width=15, height=2)
l.pack() 

b = tk.Button(window, 
    text='hit me',      # 显示在按钮上的文字
    width=15, height=2, 
  )     # 点击按钮式执行的命令
b.pack()    # 按钮位置


 
window.mainloop()




























