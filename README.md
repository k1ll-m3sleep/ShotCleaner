# shotCleaner

a lightweight Python utility that automatically removes screenshots older than a specified number of days.

## features

- automatically deletes old screenshots
- configurable screenshot folder
- configurable retention period
- displays cleanup statistics
- lightweight and fast
- designed for Windows

## configuration

open `ShotCleaner.py` and edit:

```python
SCREENSHOTS_FOLDER = Path(r"C:\Users\YourName\Pictures\Screenshots")
DELETE_AFTER_DAYS = 7
```

## build

```bash
python -m PyInstaller --onefile ShotCleaner.py
```

## automatic execution

the program is intended to be used with **Windows Task Scheduler**.

my triggers:

- At system startup
- Every day at 22:00

## example output

```text

checked files : 39
deleted files : 3
freed space   : 142.53 MB
elapsed time  : 0.0042 sec

program will close in 30 seconds...
```
## future updates
├── Multiple folders
├── Moving files to the Recycle Bin to the deletion location
├── Automatically deleting the Recycle Bin

## license

MIT License
