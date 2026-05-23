#tkinte

import tkinter as tk
from tkinter import filedialog as fd, messagebox as mb

root = tk.Tk()
root.title("Text Editor")
root.geometry("800x600")

text = tk.Text(
    root,
    wrap = tk.WORD,
    font = ("Helvetica", 13)
)

text.pack(expand=True, fill=tk.BOTH)

# CREATE NEW FILE
def newFile():
    text.delete(1.0, tk.END)

# OPEN FILE
def openFile():
    file_path = fd.askopenfilename(
        defaultextension = ".txt",
        filetypes = [("Text Files", "*.txt")]
    )

    if file_path:
        with open(file_path, "r") as file:
            text.delete(1.0, tk.END)
            data = file.read()
            text.insert(tk.END, data)

# SAVE FILE
def saveFile():
    file_path = fd.asksaveasfilename(
        defaultextension = ".txt",
        filetypes = [("Text Files", "*.txt")]
    )

    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))

    mb.showinfo("Info", "File Saved Successfully")


# MENU
mainmenu = tk.Menu(root)
root.config(menu = mainmenu)

file_menu = tk.Menu(mainmenu)

mainmenu.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "New File", command = newFile)
file_menu.add_command(label = "Open File", command = openFile)
file_menu.add_command(label = "Save File", command = saveFile)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = root.quit)

root.mainloop()