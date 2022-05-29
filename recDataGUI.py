"""
Author: cxy
Date: 2022/03/24
"""
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import receiveData

dataReceive = tk.Tk()
dataReceive.geometry('600x400')
dataReceive.title('接收数据软件')

# 文件路径获取
fileOption = tk.LabelFrame(dataReceive, text='文件路径', padx=10, pady=10)
fileOption.place(x=20, y=20)
v1 = tk.StringVar()


def filePath():
    file_path = filedialog.askdirectory()
    if file_path is not None:
        v1.set(file_path)
    return file_path


inputWindow = tk.Entry(fileOption, width=50, textvariable=v1).grid(column=0, row=0)
tk.Button(fileOption, text='打开文件夹', command=filePath).grid(column=1, row=0, padx=5, stick=tk.E)

### 参数设置
paramOption = tk.LabelFrame(dataReceive, text='服务器端参数配置', padx=10, pady=10)
paramOption.place(x=20, y=100)
entryH_var = tk.StringVar()
entryH_var.set('127.0.0.1')
ttk.Label(paramOption, text='Host：').grid(column=0, row=0)
entryHost = tk.Entry(paramOption, width=31, textvariable=entryH_var, state='normal').grid(column=1, row=0)

entryP_var = tk.StringVar()
entryP_var.set('6379')
ttk.Label(paramOption, text='Port：').grid(column=0, row=1)
entryPort = tk.Entry(paramOption, width=31, textvariable=entryP_var, state='normal').grid(column=1, row=1)

### 订阅模式选择
subOption = tk.LabelFrame(dataReceive, text='订阅通道选择', padx=10, pady=10)
subOption.place(x=20, y=200)
ttk.Label(subOption, text='订阅通道：').grid(column=0, row=0)
parameter = tk.StringVar()
parameter_list = ttk.Combobox(subOption, width=25, textvariable=parameter, state='readonly')
parameter_list['values'] = ('TWSC0002.DATA.DATX', 'TWSC0002.DATA.DATR', 'TWSC0002.DATA.DATF', 'TWSC0002.DATA.DATD')
parameter_list.current(1)
parameter_list.grid(column=1, row=0)

# 运行指令
processOption = tk.LabelFrame(dataReceive, text='运行指令', padx=10, pady=10)
processOption.place(x=330, y=200)
dataModel = receiveData.DataReceive(filePath(), entryH_var.get(), int(entryP_var.get(), 10), parameter_list.get())


def start():
    dataModel.openFile()
    dataModel.recDatafromServe()
    dataModel.closeFile()

def stop():
    dataModel.closeFile()
    messagebox.showinfo('提示', '停止数据传输')


tk.Button(processOption, text='开始接收', width=8, command=start).grid(column=0, row=0, padx=5, sticky=tk.W)
tk.Button(processOption, text='停止接收', width=8, command=stop).grid(column=1, row=0, padx=5, sticky=tk.E)

tk.mainloop()
