import tkinter as tk
import time

window = tk.Tk()

# Set gridsize for number of pixels in rows/columns
# Set pixelsize for actual size of individual pixel
gridsize = 64
pixelsize = 20

# Set all states to dead initially
states = [
    [0 for _ in range(gridsize)]
    for _ in range(gridsize)
]
# Create blank array for newstates
newstates = [
    [0 for _ in range(gridsize)]
    for _ in range(gridsize)
]

# function for toggling pixel
def togglepixel(row, col):
    rect = pixels[row][col]

    if states[row][col] == 0:
        canvas.itemconfig(rect, fill="white")
        states[row][col] = 1
    elif states[row][col] == 1:
        canvas.itemconfig(rect, fill="black")
        states[row][col] = 0

# Create canvas
canvas = tk.Canvas(window, width = gridsize*pixelsize, height= gridsize*pixelsize)
canvas.pack()

def click(event):
    row = event.y // pixelsize
    col = event.x // pixelsize

    togglepixel(row, col)

pixels = []

# fill grid
for y in range(gridsize):
    row = []
    for x in range(gridsize):
        rect = canvas.create_rectangle(
            x*pixelsize,
            y*pixelsize,
            (x+1)*pixelsize,
            (y+1)*pixelsize,
            fill="black",
            outline=""
        )
        row.append(rect)
    pixels.append(row)

def nextgen(row, col):
    state = states[row][col]
    surrcount = 0;
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            surrcount += states[row - 1 + j][col - 1 + i]
    # live rules:
    if state == 1:
        if surrcount < 2:
            newstates[row][col] = 0
        elif surrcount == 2 or surrcount == 3:
            newstates[row][col] = 1
        elif surrcount > 3:
            newstates[row][col] = 0
    elif state == 0:
        if surrcount == 3:
            newstates[row][col] = 1
        else:
            newstates[row][col] = 0

def reload():
    global states
    states = [row[:] for row in newstates]
    for i in range(gridsize):
        for j in range(gridsize):
            if states[i][j] == 1:
                canvas.itemconfig(pixels[i][j], fill = "white")
            elif states[i][j] == 0:
                canvas.itemconfig(pixels[i][j], fill = "black")

def updateall(event):
    for i in range(gridsize-2):
        for j in range(gridsize-2):
            nextgen(i+1,j+1)
    reload()

canvas.bind("<Button-1>", click)
window.bind("<space>", updateall)

window.mainloop()
