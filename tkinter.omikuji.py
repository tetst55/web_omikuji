import tkinter as tk
import os
import random

def uranau():  #占いを実行
    show_kuji["image"]=random.choice(kujis)

def clear():  #占いをクリア
    show_kuji["image"]=default_img
#メインウィンドウ
root=tk.Tk()
root.title("おみくじ")#タイトル

kujis=["大吉","中吉","小吉","凶"]#中身

default_img=tk.PhotoImage(file=os.path.join(os.path.dirname(__file__),"kujis/empty.png"))
#くじの四つのイメージ
kujis=[tk.PhotoImage(file=os.path.join(os.path.dirname(__file__),"kujis/kyo.png")),
       tk.PhotoImage(file=os.path.join(os.path.dirname(__file__),"kujis/kichi.png")),
       tk.PhotoImage(file=os.path.join(os.path.dirname(__file__),"kujis/chukichi.png")),
       tk.PhotoImage(file=os.path.join(os.path.dirname(__file__),"kujis/daikichi.png"))]
btn_frame=tk.Frame(root,padx=10,pady=20)#ボタン配置フレーム
btn_frame.pack()
    #占うボタン、クリアボタン
uranau_btn=tk.Button(btn_frame,text="占う",width=10,height=5,command=uranau,bg="lightblue")
uranau_btn.pack(side="left")
clear_btn=tk.Button(btn_frame,text="クリア",width=10,height=5,command=clear,bg="yellow")
clear_btn.pack(side="left")
#占いを表示するラベル
show_kuji=tk.Label(root,image=default_img,width=3500,height=3500,font=("Helvetica",30,"bold"))
show_kuji.pack()

root.mainloop()
