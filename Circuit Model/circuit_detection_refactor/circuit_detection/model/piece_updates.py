"""
Piece add/remove/change handlers.

Encompasses the functionality in `add_pieces.py`:
    - size correction
    - port detection (LED/MC/FM)
    - board connection updates
    - change detection vs previous frame
"""


def detect_changes(*args, **kwargs):
    raise NotImplementedError("Port `add_pieces.check_changes` here.")


def add_new_piece(*args, **kwargs):
    raise NotImplementedError("Port `add_pieces.add_new_piece` here.")


def find_person_id(*args, **kwargs):
    raise NotImplementedError("Port `add_pieces.find_person_id` here.")


