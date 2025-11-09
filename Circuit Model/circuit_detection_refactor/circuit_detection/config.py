"""
Centralised configuration for the refactored circuit detection package.

Consolidates values currently sprinkled across:
    - `process_frame.crop_frame` (crop window parameters)
    - `virtual_board_all.draws_pegs_on_rotated_board` (HSV thresholds)
    - `add_pieces.get_ports_location` (mask colours / thresholds)
    - `valid_circuit.ipynb` (YOLO weight path, frame cadence)
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class VideoConfig:
    """Camera / video parameters previously hard-coded in notebooks."""

    source: int | str = 0
    crop_x: int = 760
    crop_y: int = 250
    crop_width: int = 450
    crop_height: int = 500
    frame_rate: float = 5.0
    store_raw: bool = False


@dataclass(frozen=True)
class ModelConfig:
    """Paths and thresholds for YOLO + Mediapipe detectors."""

    yolo_weights: Path = Path("resources/models/best.pt")
    confidence: float = 0.3
    show_predictions: bool = True


@dataclass(frozen=True)
class HSVRange:
    """Convenience wrapper for HSV mask definitions."""

    lower: tuple[int, int, int]
    upper: tuple[int, int, int]


@dataclass(frozen=True)
class VisionConfig:
    """Aggregates HSV masks derived from the current heuristics."""

    board_mask: HSVRange = HSVRange((0, 0, 0), (255, 255, 50))
    fm_mask: HSVRange = HSVRange((0, 147, 106), (179, 255, 187))
    mc_mask: HSVRange = HSVRange((8, 57, 33), (88, 182, 168))
    led_mask: HSVRange = HSVRange((0, 0, 95), (91, 124, 209))


@dataclass(frozen=True)
class PathsConfig:
    """Filesystem layout for recorded artefacts."""

    root: Path = Path("circuit_detection_refactor")
    raw_videos: Path = root / "resources/data/videos/raw"
    cropped_videos: Path = root / "resources/data/videos/cropped"
    frames: Path = root / "resources/data/frames"


@dataclass(frozen=True)
class AppConfig:
    """Top-level configuration container."""

    video: VideoConfig = VideoConfig()
    model: ModelConfig = ModelConfig()
    vision: VisionConfig = VisionConfig()
    paths: PathsConfig = PathsConfig()


DEFAULT_CONFIG = AppConfig()


