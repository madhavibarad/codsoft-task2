import tkinter as tk
from tkinter import messagebox
import threading
import time

def animate_result(text):
    result_canvas.itemconfig(result_text, text="")
    for i in range(len(text) + 1):
        result_canvas.itemconfig(result_text, text=text[:i])
        time.sleep(0.04)

def show_result(result_text_str):
    threading.Thread(target=animate_result, args=(result_text_str,), daemon=True).start()

def calculate():
    try:
        num1 = float(entry1.get().strip())
        num2 = float(entry2.get().strip())
        operation = operator.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        else:
            show_result(" Invalid Operation")
            return

        show_result(f" {result:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", " Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", " Cannot divide by zero.")

root = tk.Tk()
root.title(" Galaxy Calculator")
root.geometry("360x430")
root.configure(bg="#120F2F")  

LABEL_STYLE = {"bg": "#120F2F", "fg": "#D16BA5", "font": ("Courier New", 12, "bold")}
ENTRY_STYLE = {"bg": "#231942", "fg": "#FEE440", "font": ("Courier New", 14),
               "insertbackground": "#FEE440", "relief": tk.FLAT}

tk.Label(root, text=" Galaxy Neon Calculator ", font=("Courier New", 16, "bold"),
         fg="#9F86C0", bg="#120F2F").pack(pady=15)

tk.Label(root, text="Enter First Number:", **LABEL_STYLE).pack(pady=4)
entry1 = tk.Entry(root, **ENTRY_STYLE)
entry1.pack(pady=4)

tk.Label(root, text="Enter Second Number:", **LABEL_STYLE).pack(pady=4)
entry2 = tk.Entry(root, **ENTRY_STYLE)
entry2.pack(pady=4)
tk.Label(root, text="Select Operation:", **LABEL_STYLE).pack(pady=4)
operator = tk.StringVar(value="+")
dropdown = tk.OptionMenu(root, operator, "+", "-", "*", "/")
dropdown.config(bg="#231942", fg="#FEE440", font=("Courier New", 12),
                activebackground="#D16BA5", bd=0)
dropdown["menu"].config(bg="#3E1F47", fg="white", font=("Courier New", 11))
dropdown.pack(pady=4)

def on_btn_hover(e): e.widget.config(bg="#FEE440", fg="#231942")
def on_btn_leave(e): e.widget.config(bg="#D16BA5", fg="#120F2F")

calc_btn = tk.Button(root, text="Calculate", command=calculate,
                     bg="#D16BA5", fg="#120F2F", font=("Courier New", 12, "bold"),
                     relief=tk.FLAT, width=20)
calc_btn.pack(pady=15)
calc_btn.bind("<Enter>", on_btn_hover)
calc_btn.bind("<Leave>", on_btn_leave)

result_canvas = tk.Canvas(root, width=320, height=50, bg="#120F2F", bd=0, highlightthickness=0)
result_canvas.pack(pady=10)
result_canvas.create_rectangle(0, 0, 320, 50, fill="#231942", outline="#FEE440", width=2)
result_text = result_canvas.create_text(160, 25, text="Result will appear here", fill="#FEE440",
                                        font=("Courier New", 14, "bold"))

root.mainloop()
