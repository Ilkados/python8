import os
import site
import sys


def is_virtual_environment() -> bool:
    """
    Return True if the program is running inside a virtual environment.
    """
    return sys.prefix != sys.base_prefix


def get_environment_name() -> str:
    """
    Return the virtual environment folder name.
    Example:
        /home/user/project/matrix_env -> matrix_env
    """
    return os.path.basename(sys.prefix)


def get_package_path() -> str:
    """
    Return the main site-packages path for the current environment.
    If none is found, return a fallback message.
    """
    paths = site.getsitepackages()

    for path in paths:
        if "site-packages" in path:
            return path
    return "Package path not found"


def print_outside_environment() -> None:
    """
    Display information when running outside a virtual environment.
    """
    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print(r"matrix_env\Scripts\activate     # On Windows")
    print("Then run this program again.")


def print_inside_environment() -> None:
    """
    Display information when running inside a virtual environment.
    """
    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {get_environment_name()}")
    print(f"Environment Path: {sys.prefix}")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print("Package installation path:")
    print(get_package_path())


def main() -> None:
    """
    Main program entry point.
    """
    if is_virtual_environment():
        print_inside_environment()
    else:
        print_outside_environment()


if __name__ == "__main__":
    main()
