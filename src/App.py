from tkinter import Tk, ttk


class MainWindow(Tk):
    """Main window init class"""

    def __init__(self):
        super().__init__()
        self.title("Serial data collector")
        self.geometry("400x400")
        self.after(1, self.init_ui)

    def init_ui(self) -> None:
        self.combobox = ttk.Combobox(self)
        self.combobox.pack(anchor="center", expand=True)


if __name__ == "__main__":
    MainWindow().mainloop()
