import os
import shutil
import ctypes
from ctypes import wintypes
import subprocess
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
DRIVE = "C:\\"
TEMP_DIR = os.getenv('TEMP')
USER_DIR = os.path.expanduser('~')

# Shell32.dll function to get free space
def get_free_space(folder):
    free_bytes = ctypes.c_ulonglong(0)
    total_bytes = ctypes.c_ulonglong(0)
    total_free_bytes = ctypes.c_ulonglong(0)
    ctypes.windll.kernel32.GetDiskFreeSpaceExW(
        wintypes.LPCWSTR(folder),
        ctypes.byref(free_bytes),
        ctypes.byref(total_bytes),
        ctypes.byref(total_free_bytes),
    )
    return free_bytes.value

# Function to clear temporary files
def clear_temp_files():
    logging.info("Clearing temporary files...")
    try:
        for root, dirs, files in os.walk(TEMP_DIR):
            for name in files:
                file_path = os.path.join(root, name)
                try:
                    os.remove(file_path)
                    logging.info(f"Deleted file: {file_path}")
                except Exception as e:
                    logging.error(f"Failed to delete {file_path}: {str(e)}")
            for name in dirs:
                dir_path = os.path.join(root, name)
                try:
                    shutil.rmtree(dir_path)
                    logging.info(f"Deleted directory: {dir_path}")
                except Exception as e:
                    logging.error(f"Failed to delete {dir_path}: {str(e)}")
    except Exception as e:
        logging.error(f"Failed to clear temporary files: {str(e)}")

# Function to clear unused applications
def clear_unused_apps():
    logging.info("Clearing unused applications...")
    try:
        installed_apps = subprocess.check_output(
            ['wmic', 'product', 'get', 'name,', 'lastused'], shell=True
        ).decode()
        for app in installed_apps.split('\n')[1:]:
            if 'LastUsed=' in app:
                name, last_used = app.split('LastUsed=')
                if not last_used.strip():
                    logging.info(f"Uninstalling unused application: {name.strip()}")
                    subprocess.call(
                        f'msiexec /x "{name.strip()}" /quiet /norestart',
                        shell=True
                    )
    except Exception as e:
        logging.error(f"Failed to clear unused applications: {str(e)}")

# Main function
def main():
    logging.info("Starting SpaceSaver...")
    initial_free_space = get_free_space(DRIVE)
    logging.info(f"Initial free space: {initial_free_space / (1024**3):.2f} GB")

    clear_temp_files()
    clear_unused_apps()

    final_free_space = get_free_space(DRIVE)
    logging.info(f"Final free space: {final_free_space / (1024**3):.2f} GB")
    logging.info(f"Freed up space: {(final_free_space - initial_free_space) / (1024**3):.2f} GB")

if __name__ == "__main__":
    main()