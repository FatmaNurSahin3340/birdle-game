# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 02:02:18 2024

@author: Fatma Nur Şahin
"""

import tkinter as tk
import random

count=5
def main():

    word_list= [
        "river",
        "plate",
        "glass",
        "queen",
        "onion",
        "money",
        "night",
        "anima",
        "chair",
        "vowel",
        "eagle",
        "fruit",
        "house",
        "allow",
        "bread",
        "basic",
        "cache",
        "daily",
        "favor",
        "habit"
    ]
    kelime_sayısı=len(word_list)
    i= random.randint(1,kelime_sayısı-1)
    pckelime=word_list[i]


    def new():
        root.destroy()
        main()



    print(pckelime)

    def thmn():
            global  count
            lbl5.config(text=" ")
            labelhak = tk.Label(root, text=count)
            labelhak.grid(row=1, column=11)
            kelimem = entryTahmin.get()
            if len(kelimem)==5:

                count -= 1
                if kelimem == pckelime:
                    lbl = tk.Label(root, text="Tebrikler kazandınız")
                    lbl.grid(row=8, column=0)
                    for index, letters in enumerate(pckelime):
                        if kelimem[index] == pckelime[index]:
                           
                            lbl = tk.Label(root, text=kelimem[index])
                            lbl.grid(row=7, column=index + 1)
                            lbl.config(fg="green")
                    btnpredict.config(state=tk.DISABLED)
                else:

                    if count!=0:


                        for index, letters in enumerate(pckelime):
                            if kelimem[index] == pckelime[index]:
                               
                                lbl = tk.Label(root, text=kelimem[index])
                                lbl.grid(row=7, column=index + 1)
                                lbl.config(fg="green")
                            elif kelimem[index] in pckelime:
                               
                                lbl = tk.Label(root, text=kelimem[index])
                                lbl.grid(row=7, column=index + 1)
                                lbl.config(fg="blue")
                            else:
                              
                                lbl = tk.Label(root, text=kelimem[index])
                                lbl.grid(row=7, column=index + 1)
                                lbl.config(fg="red")
                    else:
                        lbl = tk.Label(root, text="Oyun bitti! Doğru kelime:")
                        lbl.grid(row=8, column=0)
                        lbl2 = tk.Label(root, text=pckelime)
                        lbl2.grid(row=8, column=1)
                        lbl2.config(fg="green")

                        btnpredict.config(state=tk.DISABLED)
            else:
               lbl5.config(text="Harf sayısı 5 olmalıdır!!")










    root=tk.Tk()

    root.title("birdle")
    root.geometry("500x400")

    labelPredict=tk.Label(root,text="Tahmininizi Giriniz:")
    labelPredict.grid(row=1,column=0)

    entryTahmin=tk.Entry(root,width=30)
    entryTahmin.grid(row=1,column=9)

    thmnahkkı=tk.Label(root,text="tahmin hakkınız:")
    thmnahkkı.grid(row=1,column=10)
    lbl5 = tk.Label(root, text=" ")
    lbl5.grid(row=10, column=0)


    btnpredict=tk.Button(root,text="Tahmin et",command=thmn)
    btnpredict.grid(row=5,column=9)
    btnnew=tk.Button(root,text="Yeni Oyun",command=new)
    btnnew.grid(row=5,column=10)

    labelhak = tk.Label(root, text=count)
    labelhak.grid(row=1, column=11)



    resultlabel=tk.Label(root,text="Result:")
    resultlabel.grid(row=7,column=0)




    root.mainloop()

main()