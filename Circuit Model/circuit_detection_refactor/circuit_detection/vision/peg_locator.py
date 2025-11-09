"""
Peg-grid mapping utilities.

Consolidates:
    - `virtual_board_all.get_edges`
    - `virtual_board_all.get_board_mask`
    - `virtual_board_all.get_pegs`
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple

import cv2
import numpy as np

from ..config import HSVRange, VisionConfig, DEFAULT_CONFIG
from .deskew import compute_board_angle, rotate


@dataclass
class PegLayout:
    """Represents the transformed frame plus peg coordinate mapping."""

    matrix_to_real: Dict[Tuple[int, int], np.ndarray]
    rotated_frame: np.ndarray
    overlay: np.ndarray
    angle: float


def mask_board(frame: np.ndarray, hsv_range: HSVRange) -> np.ndarray:
    """HSV masking identical to `virtual_board_all.get_board_mask`."""
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array(hsv_range.lower)
    upper = np.array(hsv_range.upper)
    return cv2.inRange(img_hsv, lower, upper)


def find_board_edges(mask: np.ndarray) -> tuple[int, int, int, int]:
    """Returns (x1, x2, y1, y2) like the original function."""
    image_array = np.array(mask)
    non_zero = np.nonzero(image_array)
    min_row, min_column = np.min(non_zero, axis=1)
    max_row, max_column = np.max(non_zero, axis=1)
    return min_column, max_column, max_row, min_row


def compute_pegs(
    frame: np.ndarray,
    vision_config: VisionConfig = DEFAULT_CONFIG.vision,
    draw_edges: bool = False,
) -> PegLayout:
    """High-level port of `virtual_board_all.draws_pegs_on_rotated_board`."""
    board_mask = mask_board(frame, vision_config.board_mask)
    angle = compute_board_angle(board_mask)
    mask_rotated = rotate(board_mask, angle)
    frame_rotated = rotate(frame, angle)
    x1, x2, y1, y2 = find_board_edges(mask_rotated)

    matrix_to_real: Dict[Tuple[int, int], np.ndarray] = {}
    dist_from_edge = [(x2 - x1) / 13, (y2 - y1) / 15]
    board_width = x2 - x1 - 2 * dist_from_edge[0]
    board_height = y2 - y1 - 2 * dist_from_edge[1]
    horizontal_interval = board_width / 12
    vertical_interval = board_height / 14
    overlay = frame_rotated.copy()

    for i in range(0, 13):
        for j in range(0, 15):
            coord = np.array(
                [
                    x1 + int(horizontal_interval * i + dist_from_edge[0]),
                    y1 + int(vertical_interval * j + dist_from_edge[1]),
                ]
            )
            matrix_to_real[i, j] = coord
            cv2.circle(overlay, coord, 2, (200, 200, 200), -1)

    if draw_edges:
        cv2.rectangle(overlay, (x1, y1), (x2, y2), (0, 255, 0), 3)

    return PegLayout(
        matrix_to_real=matrix_to_real,
        rotated_frame=frame_rotated,
        overlay=overlay,
        angle=angle,
    )


