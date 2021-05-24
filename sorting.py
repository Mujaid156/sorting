from tkinter import *

selec = Tk()
selec.geometry("500x500")
selec.title("Sorting")
selec.config(bg="#5900D3")

def selection_sort():

    L = [42, 12, 13, 89, 63, 11]
    for i in range(len(L)):
        min_index = i
        for j in range(i+1, len(L)):
            if L[j] < L[min_index]:
                min_index = j
        L[i], L[min_index] = L[min_index], L[i]
    orlist.config(text=L)



# selection_sort(L)

# Creating labels
un = Label(selec, text="Unordered list", bg="#5900D3")
list = Label(selec, text="42, 12, 13, 89, 63, 11")
order = Label(selec, text="Ordered list", bg="#5900D3")
orlist = Label(selec, text="")

# Creating buttons
dis = Button(selec, text="Display", command=selection_sort)

# Placing labels
un.place(x=200, y=50)
list.place(x=175, y=100)
order.place(x=200, y=225)
orlist.place(x=175, y=275)

# Placing buttons
dis.place(x=200, y=180)

selec.mainloop()
