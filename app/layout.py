"""Layout elements for dashtest"""

import dash_bootstrap_components as dbc
from dash import html

THEME = dbc.themes.MORPH

SIZING = {"xs": {"size": 12}, "sm": {"size": 10}, "md": {"size": 8}, "lg": {"size": 6}}

PADDING = "py-3"

FOOTER = dbc.Row(
    dbc.Col(
        dbc.CardFooter(
            dbc.Row(
                children=[
                    dbc.Col(
                        html.P(
                            children=[
                                "Visit ",
                                html.A(
                                    "dashtest",
                                    href="",
                                    className="card-text",
                                ),
                            ],
                            className="card-text",
                        ),
                    ),
                    dbc.Col(
                        html.P(
                            children=[
                                "Designed by ",
                                html.A(
                                    "Micky",
                                    href="https://example.com",
                                    className="card-text",
                                ),
                            ],
                            className="card-text text-right",
                        ),
                    ),
                ],
                justify="between",
            )
        )
    ),
    class_name=PADDING,
)

MODAL = html.Div(
    [
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("About")),
                dbc.ModalBody("just a test"),
                dbc.ModalFooter(
                    dbc.Button(
                        "Close", id="close-button", className="ms-auto", n_clicks=0
                    )
                ),
            ],
            id="modal",
            is_open=False,
        ),
    ]
)
