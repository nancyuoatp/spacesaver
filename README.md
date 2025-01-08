# SpaceSaver

SpaceSaver is a Python-based utility designed to automatically detect and clear unused files and applications, freeing up space on Windows devices. This program targets temporary files and rarely used applications, helping you maintain a cleaner and more efficient system.

## Features

- **Clear Temporary Files**: Automatically deletes files in the system's temporary directory.
- **Uninstall Unused Applications**: Identifies and uninstalls applications that haven't been used recently.
- **Space Monitoring**: Reports the amount of space freed after cleaning.

## Requirements

- Windows Operating System
- Python 3.x
- Administrative privileges to uninstall applications and delete system files

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/SpaceSaver.git
   ```

2. Navigate to the project directory:
   ```bash
   cd SpaceSaver
   ```

3. Install any required Python packages. This script uses standard libraries, so no additional packages are necessary.

## Usage

Run the script using Python:

```bash
python SpaceSaver.py
```

The program will log its actions and display the amount of space freed.

## Notes

- Ensure you run this script with administrative privileges to allow it to uninstall applications and delete system files.
- Use this script at your own risk. Always ensure you have backups of important data before running cleanup utilities.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This project uses Windows Management Instrumentation (WMI) for application management.
- Thanks to the open-source community for helpful resources and tools.