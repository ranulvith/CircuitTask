from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT / "circuit_detection_refactor"))

from circuit_detection.video import frame_preprocess  # noqa: E402
from circuit_detection.config import VideoConfig  # noqa: E402


def test_crop_returns_expected_shapes():
    config = VideoConfig(
        source=0,
        crop_x=10,
        crop_y=5,
        crop_width=20,
        crop_height=15,
    )

    # create dummy frame with distinct dimensions
    frame = np.random.randint(0, 255, size=(40, 60, 3), dtype=np.uint8)

    result = frame_preprocess.crop(frame, config)

    assert result.board.shape == (20, 15, 3)  # rotated -> (width, height)
    assert result.hand.shape == (15, 35, 3)

    # ensure rotation took effect (compare first column vs original slice)
    original_crop = frame[5 : 5 + 15, 10 : 10 + 20]
    rotated_back = np.rot90(result.board, k=3)  # reverse clockwise rotation
    np.testing.assert_array_equal(rotated_back, original_crop)


