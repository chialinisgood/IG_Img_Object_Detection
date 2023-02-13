import tkinter as tk
from tkinter import filedialog, messagebox
from ig_img_download_test3 import Download_IG

def openpicture(): 
    global path
    filepath=filedialog.askdirectory()
    path.set(filepath)

def try_class():
    web = Download_IG(acc_e.get(),pwd_e.get(),save_e.get(),class_name.get())
    try:
        web.run()
        messagebox.showinfo(title='完成', message="圖片抓取完成")
    except:
        messagebox.showerror("爬取失敗",'請確認網域是否正常或帳號密碼是否正確')

root=tk.Tk()
root.title('IG_爬蟲')
root.geometry('500x150')
root.configure(bg='lightblue')
root.iconbitmap('face2.ico')
root.attributes("-topmost", True)

acc = tk.Label(root,text='Account',bg='lightblue')
acc.grid(row=0,padx=3,pady=3)
pwd = tk.Label(root,text='Password',bg='lightblue')
pwd.grid(row=1,padx=3,pady=3)
dir = tk.Label(root,text='Save Path',bg='lightblue')
dir.grid(row=2,padx=3,pady=3)

acc_e = tk.Entry(root,width=50)
acc_e.grid(row=0,column=1,padx=3,pady=3)
pwd_e = tk.Entry(root,show='*',width=50)
pwd_e.grid(row=1,column=1,padx=3,pady=3)
path = tk.StringVar()
save_e = tk.Entry(root,textvariable=path,width=50)
save_e.grid(row=2,column=1,sticky='w',padx=3,pady=3)
dir_btn = tk.Button(root,text = '選擇路徑',command=openpicture).grid(row=2,column=2,padx=3,pady=3)

class_name = tk.StringVar()
class_name.set(0)
class_lab =tk.Label(root,bg='lightblue',font='微軟正黑體')
class_lab.grid(row=3,column=0,columnspan=10,padx=3)
rb1 = tk.Radiobutton(class_lab,text='鳥',variable=class_name,value='bird',bg='lightblue').grid(row=4,column=1,padx=3,pady=3)
rb1 = tk.Radiobutton(class_lab,text='貓',variable=class_name,value='cat',bg='lightblue').grid(row=4,column=2,padx=3,pady=3)
rb1 = tk.Radiobutton(class_lab,text='狗',variable=class_name,value='dog',bg='lightblue').grid(row=4,column=3,padx=3,pady=3)
rb1 = tk.Radiobutton(class_lab,text='馬',variable=class_name,value='horse',bg='lightblue').grid(row=4,column=4,padx=3,pady=3)
login_btn = tk.Button(root,text = 'Start',command=try_class,activeforeground='#f00').grid(row=4,column=1)

root.mainloop()