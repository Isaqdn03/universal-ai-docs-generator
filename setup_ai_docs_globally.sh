#!/bin/bash
# Setup Universal AI Documentation Generator as Global Tool

echo "🚀 Installing Universal AI Documentation Generator globally..."

# Create a bin directory in home if it doesn't exist
mkdir -p ~/bin

# Copy the script to global bin
cp create_ai_docs.py ~/bin/create-ai-docs.py
chmod +x ~/bin/create-ai-docs.py

# Add to PATH if not already there (add to .bashrc or .zshrc)
if ! echo $PATH | grep -q "$HOME/bin"; then
    echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
    echo "Added ~/bin to PATH in .bashrc"
    echo "Run: source ~/.bashrc or restart terminal"
fi

echo ""
echo "✅ Universal AI Documentation Generator installed globally!"
echo ""
echo "Usage anywhere:"
echo "  create-ai-docs.py --direct           # Creates in current directory"
echo "  create-ai-docs.py /path/to/project   # Creates in specific directory"
echo ""
echo "🎉 Now you can run 'create-ai-docs.py --direct' from any project directory!" 