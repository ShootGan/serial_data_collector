from tkinter import Tk
from Components import View


class MainWindow(Tk):
    """Main window init class"""

    def __init__(self):
        super().__init__()
        self.title("Serial data collector")
        self.geometry("400x400")

        # apply custom layout
        View.Layout(self)

        # init ui
        self.after(1, self.__init_ui)

    def __init_ui(self) -> None:
        pass


if __name__ == "__main__":
    MainWindow().mainloop()
