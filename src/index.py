from tkinter import Tk
from ui.ui_view import UI

def main():
    window = Tk()
    window.title("Cookbook app")

    ui = UI(window)
    ui.start()

    window.mainloop()

if __name__ == "__main__":
    main()