from tkinter import ttk, PhotoImage
from Components.ComboBox import ComboBox


class PortPage(ttk.Frame):
    def __init__(self: object, parent: object) -> ttk.Frame:
        super().__init__(parent)

        # variables
        self.expand_icon = PhotoImage(file=r'Resources\\Icons\\expand.png')

        # ui
        ttk.Label(self, text='Setup page').pack(
            side='top', fill='x', pady=10, padx=10)

        # port panel

        self.port_panel: ttk.Frame = ttk.Frame(self)

        ttk.Label(self.port_panel, text="Port:").pack(side='left')

        ComboBox(self.port_panel, values=['1000', '2000', '3000'], image=self.expand_icon).pack(
            side='left', padx=(10, 0))

        self.port_panel.pack(side='top', pady=10, padx=10)
