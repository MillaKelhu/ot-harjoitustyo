from tkinter import Tk, ttk, constants, Toplevel
from ui.login_view import LoginView
from ui.signin_view import SigninView
from ui.book_view import BookView
from ui.new_recipe_view import NewRecipeView
from ui.recipe_view import RecipeView
from ui.modify_recipe_view import ModifyRecipeView
from ui.confirmation_view import ConfirmationWindow


class UI:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._topframe = None
        self._user = None

        self._destroy_current_top()

    def start(self):
        self._destroy_current_top()
        self._show_login()

    def _destroy_current(self):
        if self._frame:
            self._frame.destroy()

        self._frame = None

    def _destroy_current_top(self):
        if self._topframe:
            self._topframe.destroy()

        self._topframe = None


    def _show_login(self):
        self._destroy_current()
        self._destroy_current_top()

        self._frame = LoginView(
            self._root,
            self._show_book,
            self._show_signin
        )

        self._frame.pack()

    def _show_signin(self):
        self._destroy_current()
        self._destroy_current_top()

        self._frame = SigninView(
            self._root,
            self._show_login
        )

        self._frame.pack()

    def _show_book(self):
        self._destroy_current()
        self._destroy_current_top()

        self._frame = BookView(
            self._root,
            self._show_login,
            self._show_new_recipe,
            self._show_recipe
        )

        self._frame.pack()

    def _show_new_recipe(self):
        self._destroy_current()
        self._destroy_current_top()

        self._frame = NewRecipeView(
            self._root,
            self._show_book
        )

        self._frame.pack()

    def _show_recipe(self):
        self._destroy_current()
        self._destroy_current_top()

        self._frame = RecipeView(
            self._root,
            self._show_book,
            self._show_modify_recipe,
            self._show_confirmation_window
        )

        self._frame.pack()

    def _show_modify_recipe(self):
        self._destroy_current()
        self._destroy_current_top()

        self._frame = ModifyRecipeView(
            self._root,
            self._show_recipe
        )

        self._frame.pack()

    def _show_confirmation_window(self):
        self._destroy_current_top()

        self._topframe = ConfirmationWindow(
            self._show_book
        )

        self._topframe.show()