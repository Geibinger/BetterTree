#!/bin/bash

# Variables
SCRIPT_NAME="bettertree"
INSTALL_DIR="$HOME/bin"
SCRIPT_SOURCE="bettertree.py"
SCRIPT_TARGET="$INSTALL_DIR/$SCRIPT_NAME"

# Detect the user's shell
USER_SHELL=$(basename "$SHELL")
case "$USER_SHELL" in
    bash)
        SHELL_RC="$HOME/.bashrc"
        ;;
    zsh)
        SHELL_RC="$HOME/.zshrc"
        ;;
    fish)
        SHELL_RC="$HOME/.config/fish/config.fish"
        ;;
    *)
        SHELL_RC="$HOME/.bashrc"
        ;;
esac

# Create ~/bin if it doesn't exist
if [ ! -d "$INSTALL_DIR" ]; then
    echo "Creating $INSTALL_DIR directory..."
    mkdir -p "$INSTALL_DIR"
    if [ $? -ne 0 ]; then
        echo "Error: Failed to create $INSTALL_DIR."
        exit 1
    fi
fi

# Check if the script source exists
if [ ! -f "$SCRIPT_SOURCE" ]; then
    echo "Error: $SCRIPT_SOURCE not found in the current directory."
    echo "Please ensure you run this install script from the directory containing $SCRIPT_SOURCE."
    exit 1
fi

# Copy the script to ~/bin
echo "Copying $SCRIPT_SOURCE to $SCRIPT_TARGET..."
cp "$SCRIPT_SOURCE" "$SCRIPT_TARGET"
if [ $? -ne 0 ]; then
    echo "Error: Failed to copy $SCRIPT_SOURCE to $INSTALL_DIR."
    exit 1
fi

# Make the script executable
echo "Making $SCRIPT_TARGET executable..."
chmod +x "$SCRIPT_TARGET"
if [ $? -ne 0 ]; then
    echo "Error: Failed to make $SCRIPT_TARGET executable."
    exit 1
fi

# Add ~/bin to PATH if it's not already
if [[ ":$PATH:" != *":$INSTALL_DIR:"* ]]; then
    echo "Adding $INSTALL_DIR to PATH in $SHELL_RC..."
    case "$USER_SHELL" in
        bash|zsh)
            echo "" >> "$SHELL_RC"
            echo "# Added by bettertree install script" >> "$SHELL_RC"
            echo "export PATH=\"\$HOME/bin:\$PATH\"" >> "$SHELL_RC"
            ;;
        fish)
            echo "" >> "$SHELL_RC"
            echo "# Added by bettertree install script" >> "$SHELL_RC"
            echo "set -gx PATH \$HOME/bin \$PATH" >> "$SHELL_RC"
            ;;
        *)
            echo "" >> "$SHELL_RC"
            echo "# Added by bettertree install script" >> "$SHELL_RC"
            echo "export PATH=\"\$HOME/bin:\$PATH\"" >> "$SHELL_RC"
            ;;
    esac
    echo "Please reload your shell or run 'source $SHELL_RC' to apply the changes."
else
    echo "$INSTALL_DIR is already in your PATH."
fi

echo "Installation complete! You can now run '$SCRIPT_NAME' from anywhere."
