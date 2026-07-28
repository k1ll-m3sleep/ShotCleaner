from pathlib import Path
from datetime import datetime, timedelta
import time
from colorama import just_fix_windows_console, Fore, Style
just_fix_windows_console()

# --- settings
SCREENSHOTS_FOLDER = Path(r"C:\Users\ruh7r\Pictures\Screenshots")
DELETE_AFTER_DAYS = 7


# --- main
def delete_old_screenshots():
    """deletes screenshots older than the specified number of days."""

    start_time = time.perf_counter()

    checked_files = 0
    freed_space = 0
    deleted_files = 0

    if not SCREENSHOTS_FOLDER.exists():
        print(Fore.RED + f"_folder not found: {SCREENSHOTS_FOLDER}{Fore.RESET}")
        return

    current_time = datetime.now()

    print(Fore.GREEN + f"\n_folder validation:\n{SCREENSHOTS_FOLDER}\n{Fore.RESET}")

    for file in SCREENSHOTS_FOLDER.iterdir():

        if not file.is_file():
            continue

        checked_files += 1

        file_date = datetime.fromtimestamp(file.stat().st_mtime)
        file_age = current_time - file_date

        if file_age > timedelta(days=DELETE_AFTER_DAYS):
            try:
                file_size = file.stat().st_size
                freed_space += file_size

                file.unlink()

                deleted_files += 1
                print(Fore.GREEN + f"_[remotely] {file.name}{Fore.RESET}")

            except Exception as error:
                print(Fore.RED + f"_[error] {file.name}: {error}{Fore.RESET}")

        else:
            print(Fore.YELLOW + f"_[not remotely] {file.name}{Fore.RESET}")

    end_time = time.perf_counter()
    elapsed = end_time - start_time

    freed_space_mb = freed_space / (1024 * 1024)

    print("\n_==============================")
    print(Fore.CYAN + f"_checked files : {checked_files}")
    print(Fore.RED + f"_deleted files : {deleted_files}")
    print(Fore.MAGENTA + f"_freed space   : {freed_space_mb:.2f} MB")
    print(f"_elapsed time  : {elapsed:.4f} sec{Fore.RESET}")
    print("_==============================")
    print()

    for i in range(30, 0, -1):
        print(f"\rprogram will close in {Fore.RED}{i:2d}{Fore.RESET} seconds", end="", flush=True)
        time.sleep(1)

if __name__ == "__main__":
    delete_old_screenshots()

    #thx))) for downld <3