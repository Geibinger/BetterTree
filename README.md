# BetterTree

Heyho party people! This is a simple tool to help you share your project structure with a certain AI chatbot. I found that during chats,
it forgot the project structure midway through, and I had to describe it all over again. Similar to the `tree` command, this tool lists
directories and files recursively, but also displays the content of files up to a certain size and line limit.

## Installation

An installation script is provided to automate the process. The script will install the `bettertree` command to your `~/.local/bin` directory
and add it to your `~/.bashrc` file.

### Requirements

- Python 3.x

### Steps

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/Geibinger/BetterTree.git
    cd BetterTree
    ```

2. **Make the Install Script Executable:**
   ```bash
   chmod +x install.sh
   ```

3. **Run the Install Script:**
   ```bash
   ./install.sh
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

- `-e`, `--extensions`: Specify one or more file extensions to display (e.g., `-e .py .txt`).  
  *Default:* All text files  
  *Example:* `-e .py .md`

### Configuration

You can exclude specific directories and files by setting environment variables:

- `EXCLUDED_DIRECTORIES`: Comma-separated list of directories to exclude.  
  *Default:* `node_modules,.git,__pycache__,venv,dist,build,.idea,.vscode`

- `EXCLUDED_FILES`: Comma-separated list of files to exclude.  
  *Default:* `package-lock.json,yarn.lock,.DS_Store,.env`

*Example:*  
```bash
export EXCLUDED_DIRECTORIES="node_modules,.git,venv,build,logs"
export EXCLUDED_FILES="package-lock.json,.env,.log"
```

## Examples

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

- **Only display Python files:**
  ```bash
  bettertree -e .py
  ```

- **Only display Python and Markdown files with custom exclusions:**
  ```bash
  export EXCLUDED_DIRECTORIES="node_modules,.git,venv,build,logs"
  export EXCLUDED_FILES="package-lock.json,.env,.log"
  bettertree -e .py .md
  ```