import tkinter as tk

# Function to handle button clicks
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

# Create main window
root = tk.Tk()
root.title("Modern Calculator")
root.geometry("400x500")
root.resizable(False, False)
root.configure(bg="#1e1e1e")  # dark background

# Screen
screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font=("Helvetica", 24), bd=0, bg="#333", fg="#fff", justify="right")
entry.pack(fill="both", ipadx=8, pady=20, padx=10)

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

# Create buttons
for row in buttons:
    frame = tk.Frame(root, bg="#1e1e1e")
    frame.pack(expand=True, fill="both")
    for button in row:
        b = tk.Button(frame, text=button, font=("Helvetica", 20), bd=0, bg="#444", fg="#fff", relief="ridge", height=2, width=5)
        b.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        b.bind("<Button-1>", click)

root.mainloop()