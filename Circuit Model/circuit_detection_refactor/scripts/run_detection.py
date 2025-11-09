"""
CLI wrapper replacing the notebook entry point.

Example usage:
    python scripts/run_detection.py --task 1 --source raw_videos/raw_video_45.mp4
"""

from __future__ import annotations

import argparse
from dataclasses import replace

from circuit_detection import config, pipeline


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run circuit detection.")
    parser.add_argument("--task", type=int, default=1, help="Task id to verify.")
    parser.add_argument(
        "--source",
        default=config.DEFAULT_CONFIG.video.source,
        help="Camera index or video path.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    app_config = replace(
        config.DEFAULT_CONFIG,
        video=replace(config.DEFAULT_CONFIG.video, source=args.source),
    )
    pipeline.run_realtime_detection(app_config)


if __name__ == "__main__":
    main()


