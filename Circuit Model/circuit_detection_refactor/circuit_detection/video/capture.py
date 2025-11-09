"""
Frame acquisition layer.

Consolidates responsibilities currently spread across:
    - `store_as_video.store_video`
    - `valid_circuit.ipynb` loop (cv2.VideoCapture management)
    - `choose_frame_size.ipynb` when operating on prerecorded footage
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator

import cv2

from ..config import AppConfig


@dataclass
class FrameSource:
    """Descriptor for where frames originate (camera index or file path)."""

    source: int | str
    store_raw: bool
    store_path: Path | None = None


def open_capture(frame_source: FrameSource) -> cv2.VideoCapture:
    """Return an OpenCV capture object mirroring the notebook setup."""
    return cv2.VideoCapture(frame_source.source)


def iterate_frames(capture: cv2.VideoCapture) -> Iterator[tuple[bool, object]]:
    """Yield `(ret, frame)` tuples exactly like `cap.read()`."""
    while True:
        yield capture.read()


def acquire(config: AppConfig) -> Iterable[object]:
    """
    High-level generator that other modules will consume.

    Handles optional raw-video recording and ensures symmetry with
    `store_as_video.store_video`.
    """
    raise NotImplementedError("To be implemented during refactor.")


