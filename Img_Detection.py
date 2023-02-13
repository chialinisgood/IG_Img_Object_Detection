import tkinter as tk
from PIL import ImageTk,Image
from tkinter import filedialog, messagebox
import os
import time

def resize(image):
    w, h = image.size
    mlength = max(w, h)  # 找出最大的邊
    mul = 700 / mlength  # 縮放倍數
    w1 = int(w * mul)  # 重新獲得高和寬
    h1 = int(h * mul)
    return image.resize((w1, h1))

def show_image(path):
    global img   #要申明全局變量我猜測是調用了canvas
    image = Image.open(path)  # 打開圖片
    re_image = resize(image)  # 調用函數
    img = ImageTk.PhotoImage(re_image)  # PhotoImage類是用來在label和canvas展示圖片用的
    canvas.create_image(350, 350, anchor='center', image=img)

def openpicture(): #打開一張圖片並顯示
    global fileindex,fatherpath,files,file_num
    filepath=filedialog.askopenfilename()
    fatherpath=os.path.dirname(filepath)      #獲取該路徑的上一級路徑
    filename=os.path.basename(filepath)   #獲取該路徑下的文件名
    files=os.listdir(fatherpath)     #該路徑下的所有文件並生成列表
    file_num=len(files)
    fileindex=files.index(filename)    #獲取當前文件的索引值
    lab1.config(text = '資料夾 : ' + fatherpath)

def about():
    messagebox.showinfo("程式說明",'請先選取欲辨識的檔案,再選取辨識類別,最後點選Detect按鈕.\n按鈕文字變紅色表示正在辨識中,待辨識完成後即可觀看辨識後結果.\n@author: Chialin Chien')

def previous():
    global fileindex, fatherpath, files,file_num
    fileindex -=1
    if fileindex == -1:
        fileindex = file_num-1
    filepath1=os.path.join(fatherpath, files[fileindex])
    show_image(filepath1)
    txt = get_ans(filepath1)
    result.set('Result : '+txt)

def back():
    global fileindex, fatherpath, files,file_num
    fileindex += 1
    if fileindex == file_num:
        fileindex = 0
    filepath2 = os.path.join(fatherpath, files[fileindex])
    show_image(filepath2)
    txt = get_ans(filepath2)
    result.set('Result : '+txt)

def get_name(key):
    keywords_dic = {'bird':'鳥兒', 'cat':'小貓貓', 'dog':'狗勾', 'horse':'小馬'}
    name = keywords_dic.get(key)
    return name

def get_ans(file_path):
    txt_path = file_path.replace('imgs','labels')
    txt_path = txt_path.replace('jpg','txt')
    key = class_name.get()
    keywords_dic = {'bird':14, 'cat':15, 'dog':16, 'horse':17}
    value = keywords_dic.get(key)
    try:
        f = open(txt_path, 'r')
        ans = f.read().split(' ')[0]
        if ans == str(value):
            return f'抓到你了{get_name(key)}ヾ(*ΦωΦ)ツ'
    except:
        return f'沒有{get_name(key)}(˘̩̩̩ε˘̩ƪ)'

def find_new_file():
    '''查找目录下最新的文件'''
    path = os.getcwd()
    run_path = 'runs/detect'
    file_lists = os.listdir(run_path)
    file_lists.sort(key=lambda fn: os.path.getmtime(run_path + "\\" + fn)
                    if not os.path.isdir(run_path + "\\" + fn) else 0)
    file = os.path.join(run_path, file_lists[-1])
    file = os.path.join(path, file,'imgs')
    return file

def run_detect():
    key = class_name.get()
    keywords_dic = {'bird':14, 'cat':15, 'dog':16, 'horse':17}
    value = keywords_dic.get(key)
    # os.system(f'python yolov7/detect.py --weights yolov7/yolov7.pt --source Imgs/{key} --save-txt --classes {value}')
    os.system(f'python yolov7/detect.py --weights yolov7/yolov7.pt --source {fatherpath} --save-txt --classes {value}')
    # fatherpath
    
def detect():
    global fileindex,fatherpath,files,file_num
    run_detect()
    messagebox.showinfo(title='完成', message="辨識完成")
    fatherpath = find_new_file()
    filepath=os.path.join(fatherpath, files[fileindex])
    show_image(filepath)
    txt = get_ans(filepath)
    result.set('Result : '+txt)
    

root=tk.Tk()
root.title('圖片辨識結果')
root.geometry('800x850')
root.configure(bg='lightyellow')
root.iconbitmap('face.ico')
root.attributes("-topmost", True)

### result
result = tk.StringVar()
result.set("Result:")
class_name = tk.StringVar()
class_name.set(0)
lab1 =tk.Label(root,text = '路徑:',bg='lightyellow',font='微軟正黑體')
lab1.pack(expand=True)
lab2 =tk.Label(root,bg='lightyellow',font='微軟正黑體')
lab2.pack(expand=True)
rb1 = tk.Radiobutton(lab2,text='鳥',variable=class_name,value='bird',bg='lightyellow').pack(side='left')
rb1 = tk.Radiobutton(lab2,text='貓',variable=class_name,value='cat',bg='lightyellow').pack(side='left')
rb1 = tk.Radiobutton(lab2,text='狗',variable=class_name,value='dog',bg='lightyellow').pack(side='left')
rb1 = tk.Radiobutton(lab2,text='馬',variable=class_name,value='horse',bg='lightyellow').pack(side='left')
btn = tk.Button(lab2, text='Detect', command=detect,activeforeground='#f00')
btn.pack(side='left',padx=5)

lab3 =tk.Label(root,textvariable = result,bg='lightyellow',font='微軟正黑體').pack(expand=True)

### Menu
menu = tk.Menu(root)
root.config(menu=menu)
filemenu = tk.Menu(menu,tearoff=0)
menu.add_cascade(label="檔案",menu=filemenu)
filemenu.add_command(label="選擇檔案",command=openpicture)
filemenu.add_separator()
filemenu.add_command(label="結束",command=root.destroy)
helpmenu = tk.Menu(menu,tearoff=0)
menu.add_cascade(label="說明",menu=helpmenu)
helpmenu.add_command(label="程式說明",command=about)

### img
canvas=tk.Canvas(root,height=700,width=700,borderwidth=0,relief ='flat',bg='white')
canvas.pack()

### button
b2=tk.Button(root,text='下一張',command=back,width=10,height=5).pack(side='right',padx=5,pady=5)
b1=tk.Button(root,text='上一張',command=previous,width=10,height=5).pack(side='right',padx=5,pady=5)


root.mainloop()