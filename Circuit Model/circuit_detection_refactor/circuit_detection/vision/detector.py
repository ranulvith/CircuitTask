"""
Detection layer wrapping YOLO and Mediapipe.

Migrates logic from:
    - `virtual_board_all.draw_virtual_board_video` (YOLO usage)
    - `process_frame.process_frame_with_yolo`
    - `cvzone_hand.HandDetector`
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable

import numpy as np


@dataclass
class YoloDetection:
    """Mirrors the array returned by `process_frame.process_frame_with_yolo`."""

    bbox: np.ndarray  # shape: (N, 4) xyxy
    class_ids: np.ndarray  # shape: (N,)
    confidence: np.ndarray | None = None


def load_detectors() -> dict[str, Any]:
    """Placeholder for YOLO + hand detector initialisation."""
    raise NotImplementedError("Hook up ultralytics.YOLO and HandDetector here.")


def detect_pieces(frame: np.ndarray, detectors: dict[str, Any]) -> YoloDetection:
    """Return detections consistent with existing downstream expectations."""
    raise NotImplementedError("To be implemented during refactor.")


def detect_hands(frame: np.ndarray, detectors: dict[str, Any]) -> Iterable[Any]:
    """Thin wrapper over `HandDetector.findHands`."""
    raise NotImplementedError("To be implemented during refactor.")


