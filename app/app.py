"""dashtest

just a test
"""

import dash
from dash import Input, Output, State

from dashtest.layout import THEME
from dashtest.utils import generate_layout

# ----------------- Initialize App --------------------------

app = dash.Dash(__name__, external_stylesheets=[THEME], use_pages=True, pages_folder="")
app.title = "dashtest"
server = app.server

# ----------------- Page Registry ---------------------------

dash.register_page("dashtest", path="/", layout=generate_layout())

# ----------------- Layout ----------------------------------

app.layout = dash.page_container

# ------------------ Callbacks ------------------------------


@app.callback(
    Output("modal", "is_open"),
    [Input("dropdown-button", "n_clicks"), Input("close-button", "n_clicks")],
    [State("modal", "is_open")],
)  # type: ignore[misc]
def toggle_modal(n1: int, n2: int, is_open: bool) -> bool:
    """Toggle the visibility of the 'About' modal."""
    if n1 or n2:
        return not is_open
    return is_open
