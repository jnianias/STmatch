"""Tests for the STimage data model."""

import numpy as np

from stmatch import STimage


def test_creates_image_with_data_and_default_metadata() -> None:
    """An STimage retains its data and initializes optional fields safely."""
    data = np.zeros((20, 30), dtype=float)

    image = STimage(data=data)

    assert image.shape == (20, 30)
    assert image.data is data
    assert image.metadata == {}
    assert image.psf is None