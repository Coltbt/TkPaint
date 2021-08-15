import tkinter as tk
from vector2 import Vector2


class Canvas(tk.Canvas):

    def __init__(self, parent, **kwargs):
        tk.Canvas.__init__(self, parent, **kwargs)

        if 'bg' not in kwargs.keys():
            self.configure(bg='white')

        self._primary_color = 'black'
        self._secondary_color = 'white'
        self._pen_size = 5

        self.button = 1
        self.is_button_pressed = False

        self.__last_x, self.__last_y = None, None

        self.bind("<Button-1>", lambda event: self.event_manager(event, 1, True))
        self.bind("<ButtonRelease-1>", lambda event: self.event_manager(event, 1, False))

        self.bind("<Button-3>", lambda event: self.event_manager(event, 2, True))
        self.bind("<ButtonRelease-3>", lambda event: self.event_manager(event, 2, False))

        self.bind("<Motion>", self.event_manager)

    def draw(self, pos):

        color = self._primary_color if self.button == 1 else self._secondary_color

        if ((self.__last_x is None and self.__last_y is None) or
            (abs(self.__last_x - pos[0]) < 2 and abs(self.__last_y - pos[1]) < 2)):
            self.create_oval(pos[0] - self._pen_size/2, pos[1] - self._pen_size/2,
                             pos[0] + self._pen_size/2, pos[1] + self._pen_size/2,
                             fill=color, width=0)
        else:
            self.__interpolate(pos, color)

        self.__last_x, self.__last_y = pos[0], pos[1]

    def __interpolate(self, pos, color):
        vector = Vector2(pos[0] - self.__last_x, pos[1] - self.__last_y)
        direction = vector.normal()
        last_vector = Vector2(self.__last_x, self.__last_y)
        i = 0

        while i < vector.magnitude():
            x, y = last_vector.tuple()
            self.create_oval(x - self._pen_size/2, y - self._pen_size/2,
                             x + self._pen_size/2, y + self._pen_size/2,
                             fill=color, width=0)
            last_vector += direction
            i += 1

    def event_manager(self, event, button=None, state=False):

        if button:
            self.button = button
            self.is_button_pressed = state

        if self.is_button_pressed:
            self.draw((event.x, event.y))
        elif self.button == 1 or self.button == 3:
            self.__last_x, self.__last_y = None, None

    @property
    def primary_color(self):
        return self._primary_color

    @primary_color.setter
    def primary_color(self, value):
        self._primary_color = value

    @property
    def secondary_color(self):
        return self._secondary_color

    @secondary_color.setter
    def secondary_color(self, value):
        self._secondary_color = value

    @property
    def pen_size(self):
        return self._pen_size

    @pen_size.setter
    def pen_size(self, value):
        self._pen_size = value


if __name__ == "__main__":
    root = tk.Tk()
    c = Canvas(root)
    c.pack()
    root.mainloop()
