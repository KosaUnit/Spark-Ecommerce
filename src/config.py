from pathlib import Path

class Dirs:
    base_path = Path()  # assumes you run from notebooks/
    data_path = base_path / ".data"
