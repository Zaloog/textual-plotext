"""Provides a class that acts as a thin wrapper around Plottext.

Because (as of the time of writing) there doesn't seem to be a method of
getting a plotting object from Plottext, this class pulls a figure out from
inside Plotext and promotes it to the top level, so to speak, and then takes
care of adding in some of the utility methods that will bee needed.
"""

from __future__ import annotations

import plotext
from plotext._figure import _figure_class as Figure


class Plot(Figure):
    """A class that provides a Textual-friendly interface to Plotext."""

    @staticmethod
    def sin(periods=2, length=200, amplitude=1, phase=0, decay=0) -> list[float]:
        return plotext.sin(
            periods=periods,
            length=length,
            amplitude=amplitude,
            phase=phase,
            decay=decay,
        )