"""Data model for a single science image and its associated metadata."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING, Any

import numpy as np

if TYPE_CHECKING:
    from astropy.wcs import WCS
    from numpy.typing import NDArray


@dataclass
class STimage:
    """One two-dimensional science image with metadata needed for matching.

    Parameters
    ----------
    data
        Calibrated two-dimensional pixel data.
    source_path
        Optional path from which the image was loaded.
    filter_name
        Telescope filter or bandpass identifier.
    wcs
        Optional Astropy world-coordinate system for the image.
    metadata
        Additional image metadata, for example FITS header values.
    psf
        Optional point-spread-function model or image. Its representation is
        intentionally left open until PSF extraction is implemented.
    """

    data: NDArray[np.floating[Any]]
    source_path: Path | None = None
    filter_name: str | None = None
    wcs: WCS | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
    psf: NDArray[np.floating[Any]] | None = None

    def __post_init__(self) -> None:
        """Validate data invariant and normalize an optional source path."""
        self.data = np.asarray(self.data)
        if self.data.ndim != 2:
            message = "STimage data must be a two-dimensional array."
            raise ValueError(message)

        if self.source_path is not None:
            self.source_path = Path(self.source_path)

    @property
    def shape(self) -> tuple[int, int]:
        """Return the pixel-array shape as ``(rows, columns)``."""
        return self.data.shape

    def extract_psf(self) -> None:
        """Extract and store a PSF model for this image.

        This method is a placeholder for a future PSF-extraction strategy.
        """
        raise NotImplementedError