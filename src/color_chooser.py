import tkinter as tk
from tkinter import colorchooser


class ColorChooser(tk.Frame):

    def __init__(self, parent, color, text, **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)

        self._color = color
        self.sensor = None

        self.button = tk.Button(self, text=text, width=20, command=self.change_color)
        self.button.grid(row=0, column=0, padx=10, pady=2)

        self.indicator = tk.Canvas(self, height=23, width=23, bg=self._color, relief='ridge', borderwidth=1)
        self.indicator.grid(row=0, column=1, padx=10, pady=2)

    def set_sensor(self, func):
        self.sensor = func

    def change_color(self):
        self._color = colorchooser.askcolor(title="Choose a color")[1]
        self.indicator.configure(bg=self._color)

        if self.sensor:
            self.sensor()

    @property
    def color(self):
        return self._color


if __name__ == '__main__':
    root = tk.Tk()
    c = ColorChooser(root, 'white', "Primary color")
    c.pack()
    root.mainloop()

