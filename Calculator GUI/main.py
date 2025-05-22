import tkinter as tk

def btn_click(item):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(item))

def btn_clear():
    entry.delete(0, tk.END)

def btn_equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Main window
root = tk.Tk()
root.title("Smart GUI Calculator")
root.geometry("300x400")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 20), borderwidth=2, relief="groove", justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

# Button layout
btn_frame = tk.Frame(root)
btn_frame.pack()

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

for row in buttons:
    row_frame = tk.Frame(btn_frame)
    row_frame.pack(expand=True, fill="both")
    for btn_text in row:
        btn = tk.Button(
            row_frame,
            text=btn_text,
            font=("Monospace", 18),
            relief="ridge",
            border=2,
            command=lambda b=btn_text: (
                btn_clear() if b == 'C' else
                btn_equal() if b == '=' else
                btn_click(b)
            )
        )
        btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)

root.mainloop()
