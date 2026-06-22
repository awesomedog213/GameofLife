import tkinter as tk

window = tk.Tk()

# Set gridsize for number of pixels in rows/columns
# Set pixelsize for actual size of individual pixel
gridsize = 32
pixelsize = 15

# Set all states to dead initially
states = [
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

canvas.bind("<Button-1>", click)

window.mainloop()
