"""
High-level package for the refactored circuit detection and verification stack.

The modules here reorganize the original `Circuit Detection and Verification`
codebase into clearer layers (video I/O, vision, domain model, skills, UI).
Import `pipeline.run_realtime_detection` as the main entry point.
"""

from .pipeline import run_realtime_detection  # noqa: F401


