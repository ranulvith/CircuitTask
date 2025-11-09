"""
End-to-end orchestration logic for the refactored application.

Intended to absorb the procedural loop inside `valid_circuit.ipynb`:
    1. Acquire frames (camera or video file).
    2. Crop / rotate board view, skip frames with detected hands.
    3. Run YOLO to detect hardware pieces.
    4. Update board state (`add_pieces`) and compute observation vector (`all_tests`).
    5. Render optional diagnostic views.

Each stage will move into dedicated modules (`video`, `vision`, `model`, `skills`).
The functions below only provide scaffolding and reference the original modules.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .config import AppConfig, DEFAULT_CONFIG


@dataclass
class DetectionResult:
    """
    Placeholder container mirroring what `process_frame.process_frame_with_yolo`
    currently returns (matrix, data list, raw detection array).
    """

    matrix: object
    data: list[dict]
    detections: object


def initialise_pipeline(config: AppConfig = DEFAULT_CONFIG) -> None:
    """
    Set up resources required by the runtime loop.

    In the existing code this corresponds to:
        - loading YOLO weights (`virtual_board_all.YOLO`)
        - constructing `HandDetector`
        - calling `add_pieces.initialize_board`
    """


def acquire_frames(config: AppConfig) -> Iterable[object]:
    """
    Yield frames from camera/video.

    This will wrap the logic in:
        - `store_as_video.store_video`
        - `process_frame.crop_frame`
    """
    raise NotImplementedError("Frame acquisition will be implemented during refactor.")


def process_frame(frame: object, config: AppConfig) -> DetectionResult:
    """
    Run the vision stack on the provided frame.

    Bridges `virtual_board_all.draws_pegs_on_rotated_board` and
    `process_frame.process_frame_with_yolo`.
    """
    raise NotImplementedError("Vision processing to be migrated from existing modules.")


def update_board_state(result: DetectionResult) -> None:
    """
    Update the domain model using detections.

    This is currently handled by `add_pieces.add_new_piece` and friends.
    """
    raise NotImplementedError("Board state updates will be delegated to new model layer.")


def evaluate_skills() -> list[int]:
    """
    Recompute the observation vector (see `all_tests.update_skills`).
    """
    raise NotImplementedError("Skill evaluation hooks to be wired during refactor.")


def run_realtime_detection(config: AppConfig = DEFAULT_CONFIG) -> None:
    """
    Entry point mirroring the `while True` loop in `valid_circuit.ipynb`.

    Args:
        config: configuration overrides (camera source, model paths, etc.).
    """
    initialise_pipeline(config)
    for frame in acquire_frames(config):
        result = process_frame(frame, config)
        update_board_state(result)
        evaluate_skills()


