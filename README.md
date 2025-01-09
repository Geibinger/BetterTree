# BetterTree

BetterTree is a command-line tool for displaying directory structures and file contents. It skips large files and specified directories to keep the output manageable.

## Features

- Lists directories and files recursively.
- Shows file contents up to a set size and number of lines.
- Excludes certain directories and files.
- Can be run from any location.

## Installation

### Requirements

- Python 3.x

### Steps

1. **Download the Scripts:**
   - Ensure you have both `bettertree.py` and `install_bettertree.sh` in the same directory.

2. **Make the Install Script Executable:**
   ```bash
   chmod +x install_bettertree.sh
   ```

3. **Run the Install Script:**
   ```bash
   ./install_bettertree.sh
   ```

4. **Reload Your Shell Configuration:**
   ```bash
   source ~/.bashrc
   ```
   *Alternatively, open a new terminal window.*

## Usage

Run `bettertree` from the command line.

```bash
bettertree [directory] [options]
```

### Arguments

- `directory`: (Optional) The path to start from. Defaults to the current directory.

### Options

- `-s`, `--size`: Maximum file size to display content, in KB.  
  *Default:* 10 KB  
  *Example:* `-s 5`

- `-l`, `--lines`: Maximum number of lines to display from each file.  
  *Default:* 1000 lines  
  *Example:* `-l 500`

- `-d`, `--depth`: Maximum directory depth to traverse.  
  *Default:* No limit  
  *Example:* `-d 2`

### Examples

- **Show the current directory with default limits:**
  ```bash
  bettertree
  ```

- **Show a specific directory with a maximum file size of 5 KB and 500 lines per file:**
  ```bash
  bettertree /path/to/project -s 5 -l 500
  ```

- **Limit the directory traversal to 2 levels deep:**
  ```bash
  bettertree -d 2
  ```