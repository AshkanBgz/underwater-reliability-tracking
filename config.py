"""Settings shared by every script. Change DATA_ROOT here if the dataset moves."""
from pathlib import Path

# The AquaticVision dataset stays outside the repo.
DATA_ROOT = Path("E:/AquaticVision")
CALIB_DIR = DATA_ROOT / "calibration"

# seq09 (turbid) is not available yet, see docs/NOTES.md
SEQUENCES = [f"seq{i:02d}" for i in range(1, 10)]

# Where scripts write their outputs (inside the repo).
REPO_ROOT = Path(__file__).resolve().parent
RESULTS_DIR = REPO_ROOT / "results"

# DAVIS346 sensor size
WIDTH, HEIGHT = 346, 260


def seq_dir(seq):
    return DATA_ROOT / seq
