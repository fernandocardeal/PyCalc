import tkinter as tk

class Calculadora:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.Tela()
        self.root.mainloop()

    def Tela(self):
        self.root.configure(width=300, height=345, bg="#d3d3d3")
        self.root.title("Calculadora")
        self.root.resizable(False, False)

        self.Output()
        self.Botoes()

    def Output(self):
        self.out_frame = tk.Frame(self.root, width=300, height=75, bg="#ffffff")
        self.out_frame.place(x=0, y=5)

    def Botoes(self):
        self.limpar = tk.Button(self.root, text="C", width=5, height=2)
        self.limpar.place(x=5, y=90)
        self.left_par = tk.Button(self.root, text="(", width=5, height=2)
        self.left_par.place(x=77, y=90)
        self.right_par = tk.Button(self.root, text=")", width=5, height=2)
        self.right_par.place(x=149, y=90)

        self.add9 = tk.Button(self.root, text="9", width=5, height=2)
        self.add9.place(x=5, y=140)
        self.add8 = tk.Button(self.root, text="8", width=5, height=2)
        self.add8.place(x=77, y=140)
        self.add7 = tk.Button(self.root, text="7", width=5, height=2)
        self.add7.place(x=149, y=140)

        self.add6 = tk.Button(self.root, text="6", width=5, height=2)
        self.add6.place(x=5, y=190)
        self.add5 = tk.Button(self.root, text="5", width=5, height=2)
        self.add5.place(x=77, y=190)
        self.add4 = tk.Button(self.root, text="4", width=5, height=2)
        self.add4.place(x=149, y=190)


        self.add3 = tk.Button(self.root, text="3", width=5, height=2)
        self.add3.place(x=5, y=240)
        self.add2 = tk.Button(self.root, text="2", width=5, height=2)
        self.add2.place(x=77, y=240)
        self.add1 = tk.Button(self.root, text="1", width=5, height=2)
        self.add1.place(x=149, y=240)

        self.add0 = tk.Button(self.root, text="0", width=5, height=2)
        self.add0.place(x=5, y=290)
        self.float = tk.Button(self.root, text=".", width=5, height=2)
        self.float.place(x=77, y=290)
        self.equals = tk.Button(self.root, text="=", width=15, height=2)
        self.equals.place(x=149, y=290)

        self.sum = tk.Button(self.root, text="+", width=6, height=2)
        self.sum.place(x=221, y=90)
        self.sub = tk.Button(self.root, text="-", width=6, height=2)
        self.sub.place(x=221, y=140)
        self.div = tk.Button(self.root, text="/", width=6, height=2)
        self.div.place(x=221, y=190)
        self.mul = tk.Button(self.root, text="*", width=6, height=2)
        self.mul.place(x=221, y=240)

if __name__ == "__main__":
    Calculadora()
