"""Pytest tests for dashtest app"""

from dashtest.app import toggle_modal


def test_toggle_modal_callback() -> None:

    output_open = toggle_modal(1, None, True)
    assert output_open is False

    output_closed = toggle_modal(1, None, False)
    assert output_closed is True
