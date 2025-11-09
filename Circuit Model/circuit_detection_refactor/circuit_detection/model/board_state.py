"""
Board state container.

Will host logic currently created via:
    - `pieces.Board`
    - `add_pieces.initialize_board`
    - per-frame tracking in `valid_circuit.ipynb`
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class BoardState:
    """Placeholder representation of all pieces and hand history."""

    pieces: List[object] = field(default_factory=list)
    previous_data: List[dict] = field(default_factory=list)
    hand_history: Dict[str, list] = field(default_factory=dict)
    matrix_mapping: Optional[dict] = None


def initialise_board_state() -> BoardState:
    """Port of `add_pieces.initialize_board`."""
    raise NotImplementedError("To be implemented during refactor.")


