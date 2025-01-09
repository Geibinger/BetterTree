#!/bin/bash

# Variables
SCRIPT_NAME="bettertree"
INSTALL_DIR="$HOME/bin"
SCRIPT_SOURCE="bettertree.py"
SCRIPT_TARGET="$INSTALL_DIR/$SCRIPT_NAME"

# Create ~/bin if it doesn't exist
if [ ! -d "$INSTALL_DIR" ]; then
    echo "Creating $INSTALL_DIR directory..."
    mkdir -p "$INSTALL_DIR"
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

# Make the script executable
echo "Making $SCRIPT_TARGET executable..."
chmod +x "$SCRIPT_TARGET"

# Add ~/bin to PATH if it's not already
if [[ ":$PATH:" != *":$INSTALL_DIR:"* ]]; then
    echo "Adding $INSTALL_DIR to PATH in ~/.bashrc..."
    echo "" >> ~/.bashrc
    echo "# Added by bettertree install script" >> ~/.bashrc
    echo "export PATH=\"\$HOME/bin:\$PATH\"" >> ~/.bashrc
    echo "Please reload your shell or run 'source ~/.bashrc' to apply the changes."
fi

echo "Installation complete! You can now run '$SCRIPT_NAME' from anywhere."
