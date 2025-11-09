"""
Frame preprocessing helpers.

This module houses logic previously implemented in
`Circuit Detection and Verification/process_frame.py::crop_frame`.
It trims the incoming frame to the board region that will be analysed for
pieces, while keeping a slightly wider crop for hand detection. The board crop
is also rotated 90 degrees clockwise to align with the downstream coordinate
system, exactly like the legacy implementation.
"""

from __future__ import annotations

from dataclasses import dataclass

import cv2
import numpy as np

from ..config import VideoConfig


@dataclass
class CroppedFrame:
    """
    Container for preprocessed views of a camera frame.

    Attributes:
        board: The rotated crop used for piece verification.
        hand:  A slightly wider crop (unrotated) used for hand detection.
    """

    board: np.ndarray
    hand: np.ndarray


def crop(frame: np.ndarray, config: VideoConfig) -> CroppedFrame:
    """
    Crop the incoming frame into board and hand views.

    Args:
        frame: Raw BGR frame from the camera / video.
        config: Parameters describing the crop window.

    Returns:
        CroppedFrame: rotated board crop + extended hand crop.

    This is a direct translation of the original `crop_frame` helper so that
    existing behaviour remains unchanged during the refactor.
    """
    x, y = config.crop_x, config.crop_y
    w, h = config.crop_width, config.crop_height

    board = frame[y : y + h, x : x + w]
    hand = frame[y : y + h, x : x + w + 150]

    board = cv2.rotate(board, cv2.ROTATE_90_CLOCKWISE)

    return CroppedFrame(board=board, hand=hand)



