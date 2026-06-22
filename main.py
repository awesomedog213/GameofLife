import tkinter as tk

root = tk.Tk()
root.title("John Conway's Game of Life")
root.geometry("300x150")

label = tk.Label(root, text="Hello, World!", font=("Arial", 16))
label.pack(pady=20)

root.mainloop()
