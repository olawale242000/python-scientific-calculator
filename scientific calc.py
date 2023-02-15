'''
Graphic User Interface(GUI)Libraries
1. Tkinter
2. PYQT
3. Pytouch
4. Kivy
'''

import tkinter as tk

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULTS_FONT_STYLE = ("Arial",20)

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(1, 1)
        self.window.title("PY Calculator")

        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.creative_display()

    









        def run(self):
            self.window.mainloop()


if __name__ =="__main__":
    calc = Calculator()
    calc.run
