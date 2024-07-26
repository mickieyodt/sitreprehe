import tkinter as tk

root = tk.Tk()
label1 = tk.Label(root, text='Label', bg='green')
label2 = tk.Label(root, text='Label2', bg='red')

# Using expand and fill options
label1.pack(expand=True, fill=tk.Y)
label2.pack(fill=tk.BOTH)

root.mainloop()
