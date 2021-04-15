from tkinter import Tk, ttk, constants
from ui.login_view import LoginView
from ui.signin_view import SigninView
from ui.book_view import BookView
from ui.new_recipe_view import NewRecipeView
from ui.recipe_view import RecipeView


class UI:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._user = None

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
            self._show_book,
            self._show_signin
        )

        self._frame.pack()

    def _show_signin(self):
        self._destroy_current()

        self._frame = SigninView(
            self._root,
            self._show_login
        )

        self._frame.pack()

    def _show_book(self):
        self._destroy_current()

        self._frame = BookView(
            self._root,
            self._show_login,
            self._show_new_recipe,
            self._show_recipe
        )

        self._frame.pack()

    def _show_new_recipe(self):
        self._destroy_current()

        self._frame = NewRecipeView(
            self._root,
            self._show_book
        )

        self._frame.pack()

    def _show_recipe(self):
        self._destroy_current()

        self._frame = RecipeView(
            self._root,
            self._show_book
        )

        self._frame.pack()
