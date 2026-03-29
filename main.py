from utils.keybinds_reader import read_keybinds
from textual.app import App, ComposeResult
from textual.widgets import DataTable
from textual.containers import Container
from os import getlogin

FILEPATH = f"/home/{getlogin()}/.config/sway/config"

class KeybindsApp(App):

    def compose(self) -> ComposeResult:
        yield Container(DataTable())

    def on_mount(self) -> None:
        table = self.query_one(DataTable)

        table.add_columns("Key", "Command")

        keybinds = read_keybinds(FILEPATH)

        for key, command in keybinds:
            table.add_row(key, command)

        table.cursor_type = "row"

if __name__ == "__main__":
    app = KeybindsApp()
    app.run()