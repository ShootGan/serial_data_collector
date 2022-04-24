from tkinter import Tk
from src.Components import View
from Pages.PortPage import PortPage
from Components.Debugger import Debugger


class MainWindow(Tk):
    """Main window init class"""

    def __init__(self):
        super().__init__()
        self.title("Serial data collector")
        self.geometry("400x400")
        self.minsize(400, 400)
        self.bind('<F12>', lambda _: Debugger(self))

        # apply custom layout
        View.Layout(self)
        # init theme
        self.theme: object = View.Theme(self)
        self.theme.apply('Dark')

        # init ui
        self.after(1, self.__init_ui)

    def __init_ui(self) -> None:
        self.port_page: PortPage = PortPage(self)
        self.port_page.place(x=0, y=0, relwidth=1, relheight=1)


if __name__ == "__main__":
    MainWindow().mainloop()
