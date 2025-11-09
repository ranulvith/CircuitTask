# Refactored Circuit Detection Layout (Scaffold)

This folder mirrors a proposed modular layout for the existing
`Circuit Detection and Verification` project without touching the original
implementation. Each submodule points back to the legacy file(s) that will be
migrated here during the refactor.

## Package overview

- `circuit_detection/`
  - `config.py` – central configuration (camera, paths, HSV masks).
  - `pipeline.py` – orchestration loop replacing the notebook driver.
  - `video/` – frame acquisition and preprocessing (`store_as_video.py`,
    `process_frame.crop_frame`, notebook snippets).
  - `vision/` – deskewing, peg mapping, YOLO + hand detection wrappers
    (`virtual_board_all.py`, `process_frame.py`, `cvzone_hand.py`).
  - `model/` – board domain objects and update hooks (`pieces.py`,
    `connections.py`, `pieces_location.py`, `add_pieces.py`).
  - `skills/` – task definitions and evaluators (`tasks.py`, `all_tests.py`).
  - `ui/` – terminal logging and virtual board rendering (`printscreen.py`,
    `virtual_board_all.show_estimated_board`).
  - `notebooks/analysis|demos/` – slots for migrating exploratory notebooks.
- `resources/` – weights, static assets, sample data.
- `scripts/` – CLI entry points (run detection, crop calibration, reports).
- `tests/` – unit/integration test placeholders for the new architecture.

All Python files contain docstrings indicating their legacy source and are
otherwise empty scaffolding. Use this layout as a staging ground while the
original project continues to operate unchanged.


