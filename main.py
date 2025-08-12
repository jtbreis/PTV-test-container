import tkinter as tk

def main():
    root = tk.Tk()
    root.title("PTV Test GUI")
    root.geometry("300x150")

    label = tk.Label(root, text="Setup is working!", font=("Arial", 16))
    label.pack(pady=40)

    root.mainloop()

if __name__ == "__main__":
    main()