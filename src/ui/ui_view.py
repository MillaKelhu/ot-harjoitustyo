from tkinter import Tk, ttk, constants
from ui.login_view import LoginView
from ui.signin_view import SigninView
from ui.book_view import BookView

class UI:
    def __init__(self, root):
        self._root = root
        self._frame = None

    def start(self):
        self._show_login()

    def _destroy_current(self):
        if self._frame:
            self._frame.destroy()

        self._frame = None

    def _show_login(self):
        self._destroy_current()

        self._frame = LoginView(
            self._root,
            self._show_book_view,
            self._show_signin_view
        )

        self._frame.pack()

    def _show_book_view(self):
        self._destroy_current()

        self._frame = BookView(
            self._root,
            self._show_login
        )

    def _show_signin_view(self):
        self._destroy_current()

        self._frame = SigninView(
            self._root,
            self._show_login
        )

if __name__ == "__main__":
    window = Tk()
    window.title("UI test")

    ui = UI(window)
    ui.start()

    window.mainloop()
