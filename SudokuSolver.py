

import tkinter as tk
from tkinter import ttk
def insert(n,my,mx,by,bx):
    if (my,mx) == (0,0):
        if (by,bx) == (0,0):
            entry00.delete(0, tk.END)
            entry00.insert(0, f'{n}')
            entry00.config(foreground='red')
        elif (by,bx) == (0,1):
            entry01.delete(0, tk.END)
            entry01.insert(0, f'{n}')
            entry01.config(foreground='red')
        elif (by,bx) == (0,2):
            entry02.delete(0, tk.END)
            entry02.insert(0, f'{n}')
            entry02.config(foreground='red')
        elif (by,bx) == (1,0):
            entry10.delete(0, tk.END)
            entry10.insert(0, f'{n}')
            entry10.config(foreground='red')
        elif (by,bx) == (1,1):
            entry11.delete(0, tk.END)
            entry11.insert(0, f'{n}')
            entry11.config(foreground='red')
        elif (by,bx) == (1,2):
            entry12.delete(0, tk.END)
            entry12.insert(0, f'{n}')
            entry12.config(foreground='red')
        elif (by,bx) == (2,0):
            entry20.delete(0, tk.END)
            entry20.insert(0, f'{n}')
            entry20.config(foreground='red')
        elif (by,bx) == (2,1):
            entry21.delete(0, tk.END)
            entry21.insert(0, f'{n}')
            entry21.config(foreground='red')
        elif (by,bx) == (2,2):
            entry22.delete(0, tk.END)
            entry22.insert(0, f'{n}')
            entry22.config(foreground='red')
    elif (my,mx) == (0,1):
        if (by,bx) == (0,0):
            entry03.delete(0, tk.END)
            entry03.insert(0, f'{n}')
            entry03.config(foreground='red')
        elif (by,bx) == (0,1):
            entry04.delete(0, tk.END)
            entry04.insert(0, f'{n}')
            entry04.config(foreground='red')
        elif (by,bx) == (0,2):
            entry05.delete(0, tk.END)
            entry05.insert(0, f'{n}')
            entry05.config(foreground='red')
        elif (by,bx) == (1,0):
            entry13.delete(0, tk.END)
            entry13.insert(0, f'{n}')
            entry13.config(foreground='red')
        elif (by,bx) == (1,1):
            entry14.delete(0, tk.END)
            entry14.insert(0, f'{n}')
            entry14.config(foreground='red')
        elif (by,bx) == (1,2):
            entry15.delete(0, tk.END)
            entry15.insert(0, f'{n}')
            entry15.config(foreground='red')
        elif (by,bx) == (2,0):
            entry23.delete(0, tk.END)
            entry23.insert(0, f'{n}')
            entry23.config(foreground='red')
        elif (by,bx) == (2,1):
            entry24.delete(0, tk.END)
            entry24.insert(0, f'{n}')
            entry24.config(foreground='red')
        elif (by,bx) == (2,2):
            entry25.delete(0, tk.END)
            entry25.insert(0, f'{n}')
            entry25.config(foreground='red')
    elif (my,mx) == (0,2):
        if (by,bx) == (0,0):
            entry06.delete(0, tk.END)
            entry06.insert(0, f'{n}')
            entry06.config(foreground='red')
        elif (by,bx) == (0,1):
            entry07.delete(0, tk.END)
            entry07.insert(0, f'{n}')
            entry07.config(foreground='red')
        elif (by,bx) == (0,2):
            entry08.delete(0, tk.END)
            entry08.insert(0, f'{n}')
            entry08.config(foreground='red')
        elif (by,bx) == (1,0):
            entry16.delete(0, tk.END)
            entry16.insert(0, f'{n}')
            entry16.config(foreground='red')
        elif (by,bx) == (1,1):
            entry17.delete(0, tk.END)
            entry17.insert(0, f'{n}')
            entry17.config(foreground='red')
        elif (by,bx) == (1,2):
            entry18.delete(0, tk.END)
            entry18.insert(0, f'{n}')
            entry18.config(foreground='red')
        elif (by,bx) == (2,0):
            entry26.delete(0, tk.END)
            entry26.insert(0, f'{n}')
            entry26.config(foreground='red')
        elif (by,bx) == (2,1):
            entry27.delete(0, tk.END)
            entry27.insert(0, f'{n}')
            entry27.config(foreground='red')
        elif (by,bx) == (2,2):
            entry28.delete(0, tk.END)
            entry28.insert(0, f'{n}')
            entry28.config(foreground='red')
    elif (my,mx) == (1,0):
        if (by,bx) == (0,0):
            entry30.delete(0, tk.END)
            entry30.insert(0, f'{n}')
            entry30.config(foreground='red')
        elif (by,bx) == (0,1):
            entry31.delete(0, tk.END)
            entry31.insert(0, f'{n}')
            entry31.config(foreground='red')
        elif (by,bx) == (0,2):
            entry32.delete(0, tk.END)
            entry32.insert(0, f'{n}')
            entry32.config(foreground='red')
        elif (by,bx) == (1,0):
            entry40.delete(0, tk.END)
            entry40.insert(0, f'{n}')
            entry40.config(foreground='red')
        elif (by,bx) == (1,1):
            entry41.delete(0, tk.END)
            entry41.insert(0, f'{n}')
            entry41.config(foreground='red')
        elif (by,bx) == (1,2):
            entry42.delete(0, tk.END)
            entry42.insert(0, f'{n}')
            entry42.config(foreground='red')
        elif (by,bx) == (2,0):
            entry50.delete(0, tk.END)
            entry50.insert(0, f'{n}')
            entry50.config(foreground='red')
        elif (by,bx) == (2,1):
            entry51.delete(0, tk.END)
            entry51.insert(0, f'{n}')
            entry51.config(foreground='red')
        elif (by,bx) == (2,2):
            entry52.delete(0, tk.END)
            entry52.insert(0, f'{n}')
            entry52.config(foreground='red')
    elif (my,mx) == (1,1):
        if (by,bx) == (0,0):
            entry33.delete(0, tk.END)
            entry33.insert(0, f'{n}')
            entry33.config(foreground='red')
        elif (by,bx) == (0,1):
            entry34.delete(0, tk.END)
            entry34.insert(0, f'{n}')
            entry34.config(foreground='red')
        elif (by,bx) == (0,2):
            entry35.delete(0, tk.END)
            entry35.insert(0, f'{n}')
            entry35.config(foreground='red')
        elif (by,bx) == (1,0):
            entry43.delete(0, tk.END)
            entry43.insert(0, f'{n}')
            entry43.config(foreground='red')
        elif (by,bx) == (1,1):
            entry44.delete(0, tk.END)
            entry44.insert(0, f'{n}')
            entry44.config(foreground='red')
        elif (by,bx) == (1,2):
            entry45.delete(0, tk.END)
            entry45.insert(0, f'{n}')
            entry45.config(foreground='red')
        elif (by,bx) == (2,0):
            entry53.delete(0, tk.END)
            entry53.insert(0, f'{n}')
            entry53.config(foreground='red')
        elif (by,bx) == (2,1):
            entry54.delete(0, tk.END)
            entry54.insert(0, f'{n}')
            entry54.config(foreground='red')
        elif (by,bx) == (2,2):
            entry55.delete(0, tk.END)
            entry55.insert(0, f'{n}')
            entry55.config(foreground='red')
    elif (my,mx) == (1,2):
        if (by,bx) == (0,0):
            entry36.delete(0, tk.END)
            entry36.insert(0, f'{n}')
            entry36.config(foreground='red')
        elif (by,bx) == (0,1):
            entry37.delete(0, tk.END)
            entry37.insert(0, f'{n}')
            entry37.config(foreground='red')
        elif (by,bx) == (0,2):
            entry38.delete(0, tk.END)
            entry38.insert(0, f'{n}')
            entry38.config(foreground='red')
        elif (by,bx) == (1,0):
            entry46.delete(0, tk.END)
            entry46.insert(0, f'{n}')
            entry46.config(foreground='red')
        elif (by,bx) == (1,1):
            entry47.delete(0, tk.END)
            entry47.insert(0, f'{n}')
            entry47.config(foreground='red')
        elif (by,bx) == (1,2):
            entry48.delete(0, tk.END)
            entry48.insert(0, f'{n}')
            entry48.config(foreground='red')
        elif (by,bx) == (2,0):
            entry56.delete(0, tk.END)
            entry56.insert(0, f'{n}')
            entry56.config(foreground='red')
        elif (by,bx) == (2,1):
            entry57.delete(0, tk.END)
            entry57.insert(0, f'{n}')
            entry57.config(foreground='red')
        elif (by,bx) == (2,2):
            entry58.delete(0, tk.END)
            entry58.insert(0, f'{n}')
            entry58.config(foreground='red')
    elif (my,mx) == (2,0):
        if (by,bx) == (0,0):
            entry60.delete(0, tk.END)
            entry60.insert(0, f'{n}')
            entry60.config(foreground='red')
        elif (by,bx) == (0,1):
            entry61.delete(0, tk.END)
            entry61.insert(0, f'{n}')
            entry61.config(foreground='red')
        elif (by,bx) == (0,2):
            entry62.delete(0, tk.END)
            entry62.insert(0, f'{n}')
            entry62.config(foreground='red')
        elif (by,bx) == (1,0):
            entry70.delete(0, tk.END)
            entry70.insert(0, f'{n}')
            entry70.config(foreground='red')
        elif (by,bx) == (1,1):
            entry71.delete(0, tk.END)
            entry71.insert(0, f'{n}')
            entry71.config(foreground='red')
        elif (by,bx) == (1,2):
            entry72.delete(0, tk.END)
            entry72.insert(0, f'{n}')
            entry72.config(foreground='red')
        elif (by,bx) == (2,0):
            entry80.delete(0, tk.END)
            entry80.insert(0, f'{n}')
            entry80.config(foreground='red')
        elif (by,bx) == (2,1):
            entry81.delete(0, tk.END)
            entry81.insert(0, f'{n}')
            entry81.config(foreground='red')
        elif (by,bx) == (2,2):
            entry82.delete(0, tk.END)
            entry82.insert(0, f'{n}')
            entry82.config(foreground='red')
    elif (my,mx) == (2,1):
        if (by,bx) == (0,0):
            entry63.delete(0, tk.END)
            entry63.insert(0, f'{n}')
            entry63.config(foreground='red')
        elif (by,bx) == (0,1):
            entry64.delete(0, tk.END)
            entry64.insert(0, f'{n}')
            entry64.config(foreground='red')
        elif (by,bx) == (0,2):
            entry65.delete(0, tk.END)
            entry65.insert(0, f'{n}')
            entry65.config(foreground='red')
        elif (by,bx) == (1,0):
            entry73.delete(0, tk.END)
            entry73.insert(0, f'{n}')
            entry73.config(foreground='red')
        elif (by,bx) == (1,1):
            entry74.delete(0, tk.END)
            entry74.insert(0, f'{n}')
            entry74.config(foreground='red')
        elif (by,bx) == (1,2):
            entry75.delete(0, tk.END)
            entry75.insert(0, f'{n}')
            entry75.config(foreground='red')
        elif (by,bx) == (2,0):
            entry83.delete(0, tk.END)
            entry83.insert(0, f'{n}')
            entry83.config(foreground='red')
        elif (by,bx) == (2,1):
            entry84.delete(0, tk.END)
            entry84.insert(0, f'{n}')
            entry84.config(foreground='red')
        elif (by,bx) == (2,2):
            entry85.delete(0, tk.END)
            entry85.insert(0, f'{n}')
            entry85.config(foreground='red')
    elif (my,mx) == (2,2):
        if (by,bx) == (0,0):
            entry66.delete(0, tk.END)
            entry66.insert(0, f'{n}')
            entry66.config(foreground='red')
        elif (by,bx) == (0,1):
            entry67.delete(0, tk.END)
            entry67.insert(0, f'{n}')
            entry67.config(foreground='red')
        elif (by,bx) == (0,2):
            entry68.delete(0, tk.END)
            entry68.insert(0, f'{n}')
            entry68.config(foreground='red')
        elif (by,bx) == (1,0):
            entry76.delete(0, tk.END)
            entry76.insert(0, f'{n}')
            entry76.config(foreground='red')
        elif (by,bx) == (1,1):
            entry77.delete(0, tk.END)
            entry77.insert(0, f'{n}')
            entry77.config(foreground='red')
        elif (by,bx) == (1,2):
            entry78.delete(0, tk.END)
            entry78.insert(0, f'{n}')
            entry78.config(foreground='red')
        elif (by,bx) == (2,0):
            entry86.delete(0, tk.END)
            entry86.insert(0, f'{n}')
            entry86.config(foreground='red')
        elif (by,bx) == (2,1):
            entry87.delete(0, tk.END)
            entry87.insert(0, f'{n}')
            entry87.config(foreground='red')
        elif (by,bx) == (2,2):
            entry88.delete(0, tk.END)
            entry88.insert(0, f'{n}')
            entry88.config(foreground='red')
def runmatrix():
    entry1 = [[entry00.get(),entry01.get(),entry02.get()],[entry10.get(),entry11.get(),entry12.get()],[entry20.get(),entry21.get(),entry22.get()]]
    entry2 = [[entry03.get(),entry04.get(),entry05.get()],[entry13.get(),entry14.get(),entry15.get()],[entry23.get(),entry24.get(),entry25.get()]]
    entry3 = [[entry06.get(),entry07.get(),entry08.get()],[entry16.get(),entry17.get(),entry18.get()],[entry26.get(),entry27.get(),entry28.get()]]
    entry4 = [[entry30.get(),entry31.get(),entry32.get()],[entry40.get(),entry41.get(),entry42.get()],[entry50.get(),entry51.get(),entry52.get()]]
    entry5 = [[entry33.get(),entry34.get(),entry35.get()],[entry43.get(),entry44.get(),entry45.get()],[entry53.get(),entry54.get(),entry55.get()]]
    entry6 = [[entry36.get(),entry37.get(),entry38.get()],[entry46.get(),entry47.get(),entry48.get()],[entry56.get(),entry57.get(),entry58.get()]]
    entry7 = [[entry60.get(),entry61.get(),entry62.get()],[entry70.get(),entry71.get(),entry72.get()],[entry80.get(),entry81.get(),entry82.get()]]
    entry8 = [[entry63.get(),entry64.get(),entry65.get()],[entry73.get(),entry74.get(),entry75.get()],[entry83.get(),entry84.get(),entry85.get()]]
    entry9 = [[entry66.get(),entry67.get(),entry68.get()],[entry76.get(),entry77.get(),entry78.get()],[entry86.get(),entry87.get(),entry88.get()]]
    entrymatrix = [[entry1,entry2,entry3],[entry4,entry5,entry6],[entry7,entry8,entry9]]
    for my in range(3):
        for mx in range(3):
            for by in range(3):
                for bx in range(3):
                    if entrymatrix[my][mx][by][bx].isdigit():
                        number = int(entrymatrix[my][mx][by][bx])
                        matrix[my][mx][by][bx] = number
                        setrow[my][by].add(number)
                        setcol[mx][bx].add(number)
                        setblo[my][mx].add(number)
    firststep(matrix)
def valid(matrix,number,position):
    for i in range(3):
        for j in range(3):
            if matrix[position[0]][i][position[2]][j] == number and (i, j) != (position[1], position[3]):#check row
                return False
            if matrix[i][position[1]][j][position[3]] == number and (i, j) != (position[0], position[2]):#check col
                return False
            if matrix[position[0]][position[1]][i][j] == number and (i, j) != (position[2], position[3]):#check block
                return False
    return True
def findempty(matrix):
    for my in range(3):
        for mx in range(3):
            for by in range(3):
                for bx in range(3):
                    if matrix[my][mx][by][bx] == 0:
                        return (my,mx,by,bx)
    return None
def backtrack(matrix):
    find = findempty(matrix)
    if not find:
        printboard(matrix)
        return True
    else:
        my, mx, by, bx = find

    for n in range(1,10):
        if valid(matrix, n, (my,mx,by,bx)):
            matrix[my][mx][by][bx] = n
            insert(n,my,mx,by,bx)
            if backtrack(matrix):
                return True
            matrix[my][mx][by][bx] = 0
    return False
def firststep(matrix):
    printboard(matrix)
    for my in range(3):
        for mx in range(3):
            for by in range(3):
                for bx in range(3):
                    if matrix[my][mx][by][bx] == 0:
                        setblockmastrix[my][mx][by][bx] = com(setrow[my][by].union(setcol[mx][bx]).union(setblo[my][mx]))
    while True:
        totalcheck = True
        while True:
            check1 = True
            for my in range(3):
                for mx in range(3):
                    for by in range(3):
                        for bx in range(3):
                            if matrix[my][mx][by][bx] == 0 and len(setblockmastrix[my][mx][by][bx]) == 1 :
                                number = min(setblockmastrix[my][mx][by][bx])
                                oneset = setblockmastrix[my][mx][by][bx]
                                matrix[my][mx][by][bx] = number
                                setrow[my][by] = setrow[my][by].union(oneset)
                                setcol[mx][bx] = setcol[mx][bx].union(oneset)
                                setblo[my][mx] = setblo[my][mx].union(oneset)
                                print(number,f'in {my},{mx},{by},{bx}')
                                insert(number,my,mx,by,bx)
                                check1 = False
                                totalcheck = False
                                for i in range(3):
                                    for j in range(3):
                                        setblockmastrix[i][mx][j][bx] = setblockmastrix[i][mx][j][bx] - oneset
                                        setblockmastrix[my][i][by][j] = setblockmastrix[my][i][by][j] - oneset
                                        setblockmastrix[my][mx][i][j] = setblockmastrix[my][mx][i][j] - oneset
            if check1:
                break
        while True:
            check2 = True
            for my in range(3):
                for mx in range(3):
                    count = [0,0,0,0,0,0,0,0,0]
                    for n in range(1,10):
                        for by in range(3):
                            for bx in range(3):
                                if matrix[my][mx][by][bx] == 0 and n in setblockmastrix[my][mx][by][bx]:
                                    count[n-1] += 1
                    for n in range(0,9):
                        if count[n] == 1:
                            number = n+1
                            for by in range(3):
                                for bx in range(3):
                                    if matrix[my][mx][by][bx] == 0 and number in setblockmastrix[my][mx][by][bx]:
                                        y=by
                                        x=bx
                            setblockmastrix[my][mx][y][x] = {number}
                            oneset = {number}
                            matrix[my][mx][y][x] = number
                            setrow[my][y] = setrow[my][y].union(oneset)
                            setcol[mx][x] = setcol[mx][x].union(oneset)
                            setblo[my][mx] = setblo[my][mx].union(oneset)
                            print(number,f'in {my},{mx},{y},{x}')
                            insert(number,my,mx,y,x)
                            check2 = False
                            totalcheck = False
                            for i in range(3):
                                for j in range(3):
                                    setblockmastrix[i][mx][j][x] = setblockmastrix[i][mx][j][x] - oneset
                                    setblockmastrix[my][i][y][j] = setblockmastrix[my][i][y][j] - oneset
                                    setblockmastrix[my][mx][i][j] = setblockmastrix[my][mx][i][j] - oneset
            if check2:
                break
        if totalcheck:
            break
    backtrack(matrix)
def printboard(matrix):
    print(' ',matrix[0][0][0][0],matrix[0][0][0][1],matrix[0][0][0][2],' | ',matrix[0][1][0][0],matrix[0][1][0][1],matrix[0][1][0][2],' | ',matrix[0][2][0][0],matrix[0][2][0][1],matrix[0][2][0][2])
    print(' ',matrix[0][0][1][0],matrix[0][0][1][1],matrix[0][0][1][2],' | ',matrix[0][1][1][0],matrix[0][1][1][1],matrix[0][1][1][2],' | ',matrix[0][2][1][0],matrix[0][2][1][1],matrix[0][2][1][2])
    print(' ',matrix[0][0][2][0],matrix[0][0][2][1],matrix[0][0][2][2],' | ',matrix[0][1][2][0],matrix[0][1][2][1],matrix[0][1][2][2],' | ',matrix[0][2][2][0],matrix[0][2][2][1],matrix[0][2][2][2])
    print('---------|---------|---------')
    print(' ',matrix[1][0][0][0],matrix[1][0][0][1],matrix[1][0][0][2],' | ',matrix[1][1][0][0],matrix[1][1][0][1],matrix[1][1][0][2],' | ',matrix[1][2][0][0],matrix[1][2][0][1],matrix[1][2][0][2])
    print(' ',matrix[1][0][1][0],matrix[1][0][1][1],matrix[1][0][1][2],' | ',matrix[1][1][1][0],matrix[1][1][1][1],matrix[1][1][1][2],' | ',matrix[1][2][1][0],matrix[1][2][1][1],matrix[1][2][1][2])
    print(' ',matrix[1][0][2][0],matrix[1][0][2][1],matrix[1][0][2][2],' | ',matrix[1][1][2][0],matrix[1][1][2][1],matrix[1][1][2][2],' | ',matrix[1][2][2][0],matrix[1][2][2][1],matrix[1][2][2][2])
    print('---------|---------|---------')
    print(' ',matrix[2][0][0][0],matrix[2][0][0][1],matrix[2][0][0][2],' | ',matrix[2][1][0][0],matrix[2][1][0][1],matrix[2][1][0][2],' | ',matrix[2][2][0][0],matrix[2][2][0][1],matrix[2][2][0][2])
    print(' ',matrix[2][0][1][0],matrix[2][0][1][1],matrix[2][0][1][2],' | ',matrix[2][1][1][0],matrix[2][1][1][1],matrix[2][1][1][2],' | ',matrix[2][2][1][0],matrix[2][2][1][1],matrix[2][2][1][2])
    print(' ',matrix[2][0][2][0],matrix[2][0][2][1],matrix[2][0][2][2],' | ',matrix[2][1][2][0],matrix[2][1][2][1],matrix[2][1][2][2],' | ',matrix[2][2][2][0],matrix[2][2][2][1],matrix[2][2][2][2])
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('400x350')
    U = {1,2,3,4,5,6,7,8,9}
    com = lambda set: U - set

    label0 = tk.Label(root, text = '',font=("calibri", 11),anchor=tk.W,justify=tk.LEFT,width=50).grid(row=0, column=0,columnspan=9,sticky=tk.W)
    entry00 = tk.Entry(root, width = 4, borderwidth = 2)
    entry00.grid(row=1, column=1,columnspan=2,sticky=tk.W)
    entry01 = tk.Entry(root, width = 4, borderwidth = 2)
    entry01.grid(row=1, column=1,columnspan=2)
    entry02 = tk.Entry(root, width = 4, borderwidth = 2)
    entry02.grid(row=1, column=1,columnspan=2,sticky=tk.E)
    entry10 = tk.Entry(root, width = 4, borderwidth = 2)
    entry10.grid(row=2, column=1,columnspan=2,sticky=tk.W)
    entry11 = tk.Entry(root, width = 4, borderwidth = 2)
    entry11.grid(row=2, column=1,columnspan=2)
    entry12 = tk.Entry(root, width = 4, borderwidth = 2)
    entry12.grid(row=2, column=1,columnspan=2,sticky=tk.E)
    entry20 = tk.Entry(root, width = 4, borderwidth = 2)
    entry20.grid(row=3, column=1,columnspan=2,sticky=tk.W)
    entry21 = tk.Entry(root, width = 4, borderwidth = 2)
    entry21.grid(row=3, column=1,columnspan=2)
    entry22 = tk.Entry(root, width = 4, borderwidth = 2)
    entry22.grid(row=3, column=1,columnspan=2,sticky=tk.E)

    entry03 = tk.Entry(root, width = 4, borderwidth = 2)
    entry03.grid(row=1, column=2,columnspan=2,sticky=tk.E)
    entry04 = tk.Entry(root, width = 4, borderwidth = 2)
    entry04.grid(row=1, column=4,columnspan=2,sticky=tk.W)
    entry05 = tk.Entry(root, width = 4, borderwidth = 2)
    entry05.grid(row=1, column=4,columnspan=2)
    entry13 = tk.Entry(root, width = 4, borderwidth = 2)
    entry13.grid(row=2, column=2,columnspan=2,sticky=tk.E)
    entry14 = tk.Entry(root, width = 4, borderwidth = 2)
    entry14.grid(row=2, column=4,columnspan=2,sticky=tk.W)
    entry15 = tk.Entry(root, width = 4, borderwidth = 2)
    entry15.grid(row=2, column=4,columnspan=2)
    entry23 = tk.Entry(root, width = 4, borderwidth = 2)
    entry23.grid(row=3, column=2,columnspan=2,sticky=tk.E)
    entry24 = tk.Entry(root, width = 4, borderwidth = 2)
    entry24.grid(row=3, column=4,columnspan=2,sticky=tk.W)
    entry25 = tk.Entry(root, width = 4, borderwidth = 2)
    entry25.grid(row=3, column=4,columnspan=2)

    entry06 = tk.Entry(root, width = 4, borderwidth = 2)
    entry06.grid(row=1, column=5,columnspan=2)
    entry07 = tk.Entry(root, width = 4, borderwidth = 2)
    entry07.grid(row=1, column=5,columnspan=2,sticky=tk.E)
    entry08 = tk.Entry(root, width = 4, borderwidth = 2)
    entry08.grid(row=1, column=7,columnspan=2,sticky=tk.W)
    entry16 = tk.Entry(root, width = 4, borderwidth = 2)
    entry16.grid(row=2, column=5,columnspan=2)
    entry17 = tk.Entry(root, width = 4, borderwidth = 2)
    entry17.grid(row=2, column=5,columnspan=2,sticky=tk.E)
    entry18 = tk.Entry(root, width = 4, borderwidth = 2)
    entry18.grid(row=2, column=7,columnspan=2,sticky=tk.W)
    entry26 = tk.Entry(root, width = 4, borderwidth = 2)
    entry26.grid(row=3, column=5,columnspan=2)
    entry27 = tk.Entry(root, width = 4, borderwidth = 2)
    entry27.grid(row=3, column=5,columnspan=2,sticky=tk.E)
    entry28 = tk.Entry(root, width = 4, borderwidth = 2)
    entry28.grid(row=3, column=7,columnspan=2,sticky=tk.W)

    label1 = tk.Label(root, text = '',font=("calibri", 5),anchor=tk.W,justify=tk.LEFT,width=50).grid(row=4, column=0,columnspan=9,sticky=tk.W)

    entry30 = tk.Entry(root, width = 4, borderwidth = 2)
    entry30.grid(row=5, column=1,columnspan=2,sticky=tk.W)
    entry31 = tk.Entry(root, width = 4, borderwidth = 2)
    entry31.grid(row=5, column=1,columnspan=2)
    entry32 = tk.Entry(root, width = 4, borderwidth = 2)
    entry32.grid(row=5, column=1,columnspan=2,sticky=tk.E)
    entry40 = tk.Entry(root, width = 4, borderwidth = 2)
    entry40.grid(row=6, column=1,columnspan=2,sticky=tk.W)
    entry41 = tk.Entry(root, width = 4, borderwidth = 2)
    entry41.grid(row=6, column=1,columnspan=2)
    entry42 = tk.Entry(root, width = 4, borderwidth = 2)
    entry42.grid(row=6, column=1,columnspan=2,sticky=tk.E)
    entry50 = tk.Entry(root, width = 4, borderwidth = 2)
    entry50.grid(row=7, column=1,columnspan=2,sticky=tk.W)
    entry51 = tk.Entry(root, width = 4, borderwidth = 2)
    entry51.grid(row=7, column=1,columnspan=2)
    entry52 = tk.Entry(root, width = 4, borderwidth = 2)
    entry52.grid(row=7, column=1,columnspan=2,sticky=tk.E)

    entry33 = tk.Entry(root, width = 4, borderwidth = 2)
    entry33.grid(row=5, column=2,columnspan=2,sticky=tk.E)
    entry34 = tk.Entry(root, width = 4, borderwidth = 2)
    entry34.grid(row=5, column=4,columnspan=2,sticky=tk.W)
    entry35 = tk.Entry(root, width = 4, borderwidth = 2)
    entry35.grid(row=5, column=4,columnspan=2)
    entry43 = tk.Entry(root, width = 4, borderwidth = 2)
    entry43.grid(row=6, column=2,columnspan=2,sticky=tk.E)
    entry44 = tk.Entry(root, width = 4, borderwidth = 2)
    entry44.grid(row=6, column=4,columnspan=2,sticky=tk.W)
    entry45 = tk.Entry(root, width = 4, borderwidth = 2)
    entry45.grid(row=6, column=4,columnspan=2)
    entry53 = tk.Entry(root, width = 4, borderwidth = 2)
    entry53.grid(row=7, column=2,columnspan=2,sticky=tk.E)
    entry54 = tk.Entry(root, width = 4, borderwidth = 2)
    entry54.grid(row=7, column=4,columnspan=2,sticky=tk.W)
    entry55 = tk.Entry(root, width = 4, borderwidth = 2)
    entry55.grid(row=7, column=4,columnspan=2)

    entry36 = tk.Entry(root, width = 4, borderwidth = 2)
    entry36.grid(row=5, column=5,columnspan=2)
    entry37 = tk.Entry(root, width = 4, borderwidth = 2)
    entry37.grid(row=5, column=5,columnspan=2,sticky=tk.E)
    entry38 = tk.Entry(root, width = 4, borderwidth = 2)
    entry38.grid(row=5, column=7,columnspan=2,sticky=tk.W)
    entry46 = tk.Entry(root, width = 4, borderwidth = 2)
    entry46.grid(row=6, column=5,columnspan=2)
    entry47 = tk.Entry(root, width = 4, borderwidth = 2)
    entry47.grid(row=6, column=5,columnspan=2,sticky=tk.E)
    entry48 = tk.Entry(root, width = 4, borderwidth = 2)
    entry48.grid(row=6, column=7,columnspan=2,sticky=tk.W)
    entry56 = tk.Entry(root, width = 4, borderwidth = 2)
    entry56.grid(row=7, column=5,columnspan=2)
    entry57 = tk.Entry(root, width = 4, borderwidth = 2)
    entry57.grid(row=7, column=5,columnspan=2,sticky=tk.E)
    entry58 = tk.Entry(root, width = 4, borderwidth = 2)
    entry58.grid(row=7, column=7,columnspan=2,sticky=tk.W)

    label2 = tk.Label(root, text = '',font=("calibri", 5),anchor=tk.W,justify=tk.LEFT,width=50).grid(row=8, column=0,columnspan=9,sticky=tk.W)

    entry60 = tk.Entry(root, width = 4, borderwidth = 2)
    entry60.grid(row=9, column=1,columnspan=2,sticky=tk.W)
    entry61 = tk.Entry(root, width = 4, borderwidth = 2)
    entry61.grid(row=9, column=1,columnspan=2)
    entry62 = tk.Entry(root, width = 4, borderwidth = 2)
    entry62.grid(row=9, column=1,columnspan=2,sticky=tk.E)
    entry70 = tk.Entry(root, width = 4, borderwidth = 2)
    entry70.grid(row=10, column=1,columnspan=2,sticky=tk.W)
    entry71 = tk.Entry(root, width = 4, borderwidth = 2)
    entry71.grid(row=10, column=1,columnspan=2)
    entry72 = tk.Entry(root, width = 4, borderwidth = 2)
    entry72.grid(row=10, column=1,columnspan=2,sticky=tk.E)
    entry80 = tk.Entry(root, width = 4, borderwidth = 2)
    entry80.grid(row=11, column=1,columnspan=2,sticky=tk.W)
    entry81 = tk.Entry(root, width = 4, borderwidth = 2)
    entry81.grid(row=11, column=1,columnspan=2)
    entry82 = tk.Entry(root, width = 4, borderwidth = 2)
    entry82.grid(row=11, column=1,columnspan=2,sticky=tk.E)

    entry63 = tk.Entry(root, width = 4, borderwidth = 2)
    entry63.grid(row=9, column=2,columnspan=2,sticky=tk.E)
    entry64 = tk.Entry(root, width = 4, borderwidth = 2)
    entry64.grid(row=9, column=4,columnspan=2,sticky=tk.W)
    entry65 = tk.Entry(root, width = 4, borderwidth = 2)
    entry65.grid(row=9, column=4,columnspan=2)
    entry73 = tk.Entry(root, width = 4, borderwidth = 2)
    entry73.grid(row=10, column=2,columnspan=2,sticky=tk.E)
    entry74 = tk.Entry(root, width = 4, borderwidth = 2)
    entry74.grid(row=10, column=4,columnspan=2,sticky=tk.W)
    entry75 = tk.Entry(root, width = 4, borderwidth = 2)
    entry75.grid(row=10, column=4,columnspan=2)
    entry83 = tk.Entry(root, width = 4, borderwidth = 2)
    entry83.grid(row=11, column=2,columnspan=2,sticky=tk.E)
    entry84 = tk.Entry(root, width = 4, borderwidth = 2)
    entry84.grid(row=11, column=4,columnspan=2,sticky=tk.W)
    entry85 = tk.Entry(root, width = 4, borderwidth = 2)
    entry85.grid(row=11, column=4,columnspan=2)

    entry66 = tk.Entry(root, width = 4, borderwidth = 2)
    entry66.grid(row=9, column=5,columnspan=2)
    entry67 = tk.Entry(root, width = 4, borderwidth = 2)
    entry67.grid(row=9, column=5,columnspan=2,sticky=tk.E)
    entry68 = tk.Entry(root, width = 4, borderwidth = 2)
    entry68.grid(row=9, column=7,columnspan=2,sticky=tk.W)
    entry76 = tk.Entry(root, width = 4, borderwidth = 2)
    entry76.grid(row=10, column=5,columnspan=2)
    entry77 = tk.Entry(root, width = 4, borderwidth = 2)
    entry77.grid(row=10, column=5,columnspan=2,sticky=tk.E)
    entry78 = tk.Entry(root, width = 4, borderwidth = 2)
    entry78.grid(row=10, column=7,columnspan=2,sticky=tk.W)
    entry86 = tk.Entry(root, width = 4, borderwidth = 2)
    entry86.grid(row=11, column=5,columnspan=2)
    entry87 = tk.Entry(root, width = 4, borderwidth = 2)
    entry87.grid(row=11, column=5,columnspan=2,sticky=tk.E)
    entry88 = tk.Entry(root, width = 4, borderwidth = 2)
    entry88.grid(row=11, column=7,columnspan=2,sticky=tk.W)

    label3 = tk.Label(root, text = '',font=("calibri", 5),anchor=tk.W,justify=tk.LEFT,width=50).grid(row=12, column=0,columnspan=9,sticky=tk.W)

    block1 = [[0,0,0],[0,0,0],[0,0,0]]
    block2 = [[0,0,0],[0,0,0],[0,0,0]]
    block3 = [[0,0,0],[0,0,0],[0,0,0]]
    block4 = [[0,0,0],[0,0,0],[0,0,0]]
    block5 = [[0,0,0],[0,0,0],[0,0,0]]
    block6 = [[0,0,0],[0,0,0],[0,0,0]]
    block7 = [[0,0,0],[0,0,0],[0,0,0]]
    block8 = [[0,0,0],[0,0,0],[0,0,0]]
    block9 = [[0,0,0],[0,0,0],[0,0,0]]

    matrix = [[block1,block2,block3],[block4,block5,block6],[block7,block8,block9]]

    setblock1 = [[set(),set(),set()],[set(),set(),set()],[set(),set(),set()]]
    setblock2 = [[set(),set(),set()],[set(),set(),set()],[set(),set(),set()]]
    setblock3 = [[set(),set(),set()],[set(),set(),set()],[set(),set(),set()]]
    setblock4 = [[set(),set(),set()],[set(),set(),set()],[set(),set(),set()]]
    setblock5 = [[set(),set(),set()],[set(),set(),set()],[set(),set(),set()]]
    setblock6 = [[set(),set(),set()],[set(),set(),set()],[set(),set(),set()]]
    setblock7 = [[set(),set(),set()],[set(),set(),set()],[set(),set(),set()]]
    setblock8 = [[set(),set(),set()],[set(),set(),set()],[set(),set(),set()]]
    setblock9 = [[set(),set(),set()],[set(),set(),set()],[set(),set(),set()]]
    setblockmastrix = [[setblock1,setblock2,setblock3],[setblock4,setblock5,setblock6],[setblock7,setblock8,setblock9]]

    setrow = [[set(),set(),set()],[set(),set(),set()],[set(),set(),set()]]
    setcol = [[set(),set(),set()],[set(),set(),set()],[set(),set(),set()]]
    setblo = [[set(),set(),set()],[set(),set(),set()],[set(),set(),set()]]

    run = tk.Button(root, text="RUN",anchor=tk.E, padx = 18.5, pady = 3, fg = "black", bg = "#E0E0E0", command=runmatrix)
    run.grid(row=13, column=3,padx=10, rowspan = 2,columnspan=3)

    root.mainloop()