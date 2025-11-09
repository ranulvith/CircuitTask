"""
Deskew logic extracted from `virtual_board_all.py`.

Functions will be migrated here:
    - `whatAngle`
    - `tilt`
    - HSV-based board masking
"""

from __future__ import annotations

import cv2
import numpy as np


def compute_board_angle(board_mask: np.ndarray) -> float:
    """Copy of `virtual_board_all.whatAngle`."""
    coords = np.column_stack(np.where(board_mask > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    return angle


def rotate(image: np.ndarray, angle: float) -> np.ndarray:
    """Copy of `virtual_board_all.tilt`."""
    height, width = image.shape[:2]
    center = (width // 2, height // 2)
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(
        image,
        matrix,
        (width, height),
        flags=cv2.INTER_CUBIC,
        borderMode=cv2.BORDER_REPLICATE,
    )


