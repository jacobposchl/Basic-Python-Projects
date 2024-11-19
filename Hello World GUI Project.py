print("Hello World")
import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Hello World GUI")

    label = tk.Label(root, text = "Hello World")
    label.pack(padx = 20, pady = 20)

    root.mainloop()


if __name__ == "__main__":
    main()