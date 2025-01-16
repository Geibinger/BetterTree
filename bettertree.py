#!/usr/bin/env python3

import os
import sys
import argparse

from colorama import init, Fore, Style
init(autoreset=True)

# Load excluded directories/files from environment variables or use default values
DEFAULT_EXCLUDED_DIRECTORIES = "node_modules,.git,__pycache__,venv,dist,build,.idea,.vscode"
DEFAULT_EXCLUDED_FILES = "package-lock.json,yarn.lock,.DS_Store,.env"

EXCLUDED_DIRECTORIES = set(
    os.getenv("EXCLUDED_DIRECTORIES", DEFAULT_EXCLUDED_DIRECTORIES).split(",")
)
EXCLUDED_FILES = set(
    os.getenv("EXCLUDED_FILES", DEFAULT_EXCLUDED_FILES).split(",")
)

def is_text_file(file_path):
    """
    Heuristic to check if a file is a text file.
    Reads the first 1024 bytes and checks for non-text characters.
    """
    try:
        with open(file_path, 'rb') as f:
            chunk = f.read(1024)
            if b'\0' in chunk:
                return False
            # Check if the chunk can be decoded as UTF-8
            try:
                chunk.decode('utf-8')
                return True
            except UnicodeDecodeError:
                return False
    except Exception:
        return False

def print_structure(start_path, indent="", max_size=10*1024, max_lines=1000, allowed_extensions=None):
    """
    Recursively prints the directory structure and file contents.

    Parameters:
    - start_path: Directory to start from.
    - indent: Current indentation level.
    - max_size: Maximum file size in bytes to display content.
    - max_lines: Maximum number of lines to display from a file.
    - allowed_extensions: A set of file extensions to display. If None or empty, display all text files.
    """
    try:
        entries = sorted(os.listdir(start_path))
    except PermissionError:
        print(f"{indent}[Permission Denied]: {start_path}")
        return

    for index, entry in enumerate(entries):
        path = os.path.join(start_path, entry)
        is_last = (index == len(entries) - 1)
        connector = "└── " if is_last else "├── "

        # Optional color for directories vs. files
        if os.path.isdir(path):
            connector = f"{Fore.GREEN}{connector}{Style.RESET_ALL}"
        else:
            connector = f"{Fore.BLUE}{connector}{Style.RESET_ALL}"

        print(f"{indent}{connector}{entry}")

        # Skip if directory is in the excluded set
        if os.path.isdir(path):
            if entry in EXCLUDED_DIRECTORIES:
                print(f"{indent}{'    ' if is_last else '│   '}[Skipped {entry} directory]")
                continue
            extension = "    " if is_last else "│   "
            print_structure(
                path,
                indent + extension,
                max_size,
                max_lines,
                allowed_extensions=allowed_extensions
            )
        elif os.path.isfile(path):
            # Skip if file is in the excluded set
            if entry in EXCLUDED_FILES:
                print(f"{indent + ('    ' if is_last else '│   ')}[Skipped {entry} file]")
                continue

            # If specific extensions are provided, check if this file matches
            if allowed_extensions:
                _, ext = os.path.splitext(entry.lower())
                if ext not in allowed_extensions:
                    print(f"{indent + ('    ' if is_last else '│   ')}[Skipped {entry} - extension not in allowed list]")
                    continue

            # Check if it's a text file
            if is_text_file(path):
                file_size = os.path.getsize(path)
                if file_size <= max_size:
                    print_file_content(
                        path,
                        indent + ("    " if is_last else "│   "),
                        max_lines
                    )
                else:
                    print(f"{indent + ('    ' if is_last else '│   ')}[Skipped {entry} - size {file_size} bytes exceeds limit]")
            else:
                print(f"{indent + ('    ' if is_last else '│   ')}[Skipped {entry} - binary file]")

def print_file_content(file_path, indent, max_lines):
    """
    Prints the content of a file with indentation.

    Parameters:
    - file_path: Path to the file.
    - indent: Indentation string.
    - max_lines: Maximum number of lines to print.
    """
    print(f"{indent}Contents of {os.path.basename(file_path)}:")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                if i >= max_lines:
                    print(f"{indent}    ... [Truncated after {max_lines} lines]")
                    break
                print(f"{indent}    {line.rstrip()}")
    except (UnicodeDecodeError, PermissionError, IsADirectoryError):
        print(f"{indent}    [Cannot display content]")

def parse_arguments():
    """
    Parses command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Print directory structure and file contents with size and line limits.")
    parser.add_argument(
        "directory",
        nargs="?",
        default=os.getcwd(),
        help="Directory to start from (default: current directory)"
    )
    parser.add_argument(
        "-s", "--size",
        type=int,
        default=10,
        help="Maximum file size to display (in KB, default: 10)"
    )
    parser.add_argument(
        "-l", "--lines",
        type=int,
        default=1000,
        help="Maximum number of lines to display from each file (default: 1000)"
    )
    parser.add_argument(
        "-e", "--extensions",
        nargs="*",
        default=[],
        help="Specify one or more file extensions (e.g. -e .py .txt) to display. If omitted, all text files are displayed."
    )
    return parser.parse_args()

def main():
    args = parse_arguments()
    start_directory = os.path.abspath(args.directory)
    max_size = args.size * 1024  # Convert KB to bytes
    max_lines = args.lines

    # Normalize and store allowed extensions in a set (in lowercase)
    if args.extensions:
        allowed_extensions = {
            ext.lower() if ext.startswith('.') else f".{ext.lower()}"
            for ext in args.extensions
        }
    else:
        allowed_extensions = None  # Means "no restriction by extension"

    print(f"{Fore.MAGENTA}Directory structure and contents of: {start_directory}{Style.RESET_ALL}\n")
    print_structure(start_directory, max_size=max_size, max_lines=max_lines, allowed_extensions=allowed_extensions)

if __name__ == "__main__":
    main()
