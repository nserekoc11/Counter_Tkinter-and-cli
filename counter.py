import tkinter as tk


class CounterApp:
    def __init__(self, root):
        self.root = root
        root.title("Counter App")
        root.geometry("300x200")
        root.resizable(False, False)

        greeting = tk.Label(root, text="Welcome to the Counter App!", font=("Arial", 12))
        greeting.pack(pady=10)

        self.count = 0
        self.label = tk.Label(root, text=str(self.count), font=("Arial", 24))
        self.label.pack(pady=10)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="+", width=4, command=self.increment).pack(side="left", padx=5)
        tk.Button(btn_frame, text="-", width=4, command=self.decrement).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Reset", width=6, command=self.reset).pack(side="left", padx=5)

    def increment(self):
        self.count += 1
        self._update_label()

    def decrement(self):
        self.count -= 1
        self._update_label()

    def reset(self):
        self.count = 0
        self._update_label()

    def _update_label(self):
        self.label.config(text=str(self.count))


if __name__ == "__main__":
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()