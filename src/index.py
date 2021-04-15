from tkinter import Tk
from ui.ui_view import UI


def main():
    window = Tk()
    window.title("Cookbook app")

    ui_window = UI(window)
    ui_window.start()

    window.mainloop()


if __name__ == "__main__":
    main()
