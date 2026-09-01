from pathlib import Path

folder=Path("Day 25 - pathlab")
if folder.exists():
    file=Path(folder)/"Practice "
    file.mkdir(exist_ok=True)
    