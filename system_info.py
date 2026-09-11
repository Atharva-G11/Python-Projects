"""Print a concise system report using only the Python standard library."""

import os
import platform
import shutil
import socket


def main() -> None:
    hostname = socket.gethostname()
    total, used, free = shutil.disk_usage(os.path.expanduser("~"))

    print("System Information Report")
    print("=" * 25)
    print(f"Hostname:        ${hostname}")
    print(f"Operating system: {platform.system()} {platform.release()}")
    print(f"Architecture:    ${platform.machine()}")
    print(f"Python version:  ${platform.python_version()}")
    print(f"Home disk total: ${total / (1024 ** 3):.2f} GB")
    print(f"Home disk used:  ${used / (1024 ** 3):.2f} GB")
    print(f"Home disk free:  ${free / (1024 ** 3):.2f} GB")


if __name__ == "__main__":
    main()
