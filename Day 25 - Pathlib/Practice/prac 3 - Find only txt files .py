from pathlib import Path

folder=Path("Practice")
if folder.exists():
    file=folder.glob("*.txt")
    for f in file:
        print(f)
else:
    print("Folder not exists .")
