from canvas import *
from color_chooser import *


class App(tk.Tk):

    def __init__(self, width, height):
        tk.Tk.__init__(self)

        self.geometry(str(width) + "x" + str(height))
        self.title("Paint App")
        self.resizable(True, True)
        self.minsize(400, 300)
        self.iconbitmap('assets/icon.ico')

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.can = Canvas(self)
        self.can.grid(row=0, column=0, columnspan=2,sticky=tk.E+tk.W+tk.N+tk.S, padx=10, pady=5)

        self.slider = tk.Scale(self, orient='horizontal', from_=1, to=63,
                               resolution=1, tickinterval=10, label="Pen size",
                               command=self.set_size)
        self.slider.set(5)
        self.slider.grid(row=1, column=0, sticky=tk.E+tk.W, padx=20, pady=5)

        self.color_frame = tk.Frame(self, borderwidth=2, relief=tk.GROOVE)
        self.chooser1 = ColorChooser(self.color_frame, 'black', 'Primary color')
        self.chooser2 = ColorChooser(self.color_frame, 'white', 'Secondary color')
        self.chooser1.set_sensor(self.set_primary_color)
        self.chooser2.set_sensor(self.set_secondary_color)

        self.chooser1.grid()
        self.chooser2.grid()

        self.color_frame.grid(row=1, column=1, padx=10, pady=5)

    def set_size(self, size):
        self.can.pen_size = int(size)

    def set_primary_color(self):
        self.can.primary_color = self.chooser1.color

    def set_secondary_color(self):
        self.can.secondary_color = self.chooser2.color


if __name__ == '__main__':
    app = App(500, 500)
    app.mainloop()




