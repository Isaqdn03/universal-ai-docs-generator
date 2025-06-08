#!/bin/bash
# Setup Universal AI Documentation Generator as Global Tool

# Create a bin directory in home if it doesn't exist
mkdir -p ~/bin

# Copy the script to global bin
cp create_universal_ai_docs.py ~/bin/create-ai-docs.py
chmod +x ~/bin/create-ai-docs.py

# Add to PATH if not already there (add to .bashrc or .zshrc)
if ! echo $PATH | grep -q "$HOME/bin"; then
    echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
    echo "Added ~/bin to PATH in .bashrc"
    echo "Run: source ~/.bashrc or restart terminal"
fi

echo "✅ Universal AI Documentation Generator installed globally!"
echo "Usage: create-ai-docs.py [target-directory]"
echo ""
echo "Examples:"
echo "  create-ai-docs.py                    # Creates in current directory"
echo "  create-ai-docs.py ~/my-new-project  # Creates in specific directory" 