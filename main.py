from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from math import *


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2
        self.pos = (225, 250)
        self.size_hint = (0.4, 0.2)
        self.var1 = TextInput(input_filter='float',
                              multiline=False,
                              background_color=(8/200, 136/200, 1, 1),
                              pos=(50, 50)
                              )
        self.add_widget(self.var1)
        self.var2 = TextInput(input_filter='float',
                              multiline=False,
                              background_color=(8 / 200, 136 / 200, 1, 1)
                              )
        self.add_widget(self.var2)
        self.var1.fbind('focus', self.foc1)
        self.var2.fbind('focus', self.foc2)

    def foc2(self, obj1, obj2):
        if self.var2.focus:
            self.var1.text = ""
            self.var2.text = ""
            self.var2.fbind('text', self.change1)
        else:
            self.var2.funbind('text', self.change1)

    def foc1(self, obj1, obj2):
        if self.var1.focus:
            self.var1.text = ""
            self.var2.text = ""
            self.var1.fbind('text', self.change2)
        else:
            self.var1.funbind('text', self.change2)

    def change1(self, obj1, obj2):
        try:
            self.var1.text = str(float(self.var2.text)/sqrt(5))
        except ValueError:
            self.var1.text = ""

    def change2(self, obj1, obj2):
        try:
            self.var2.text = str(float(self.var1.text)+1)
        except ValueError:
            self.var2.text = ""


class MainApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MainApp().run()
