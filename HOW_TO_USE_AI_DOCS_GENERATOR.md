# How to Use the Universal AI Documentation Generator

This guide shows you exactly how to use the AI documentation generator for any new project.

## 📦 Installation Options

### **🚀 Option 1: Global Installation (Recommended)**
Install once, use anywhere:
```bash
# 1. Download this repository
git clone https://github.com/your-repo/universal-ai-docs-generator.git
cd universal-ai-docs-generator

# 2. Install globally
./setup_ai_docs_globally.sh

# 3. Use from any project directory
cd ~/my-new-project
create-ai-docs.py --direct
```

### **⚡ Option 2: One-Time Download & Run**
```bash
# Download and run directly (no installation)
curl -sSL https://raw.githubusercontent.com/your-repo/universal-ai-docs-generator/main/create_ai_docs.py > create_ai_docs.py
chmod +x create_ai_docs.py
./create_ai_docs.py --direct
```

### **📁 Option 3: Local Copy**
```bash
# Copy script to your project and run
cp /path/to/downloaded/create_ai_docs.py .
./create_ai_docs.py --direct
```

## 🚀 Quick Start (Global Command)

After running the setup, you now have a global `create-ai-docs.py` command available anywhere:

### **Step 1: Start Your New Project**
```bash
# Create your new project directory
mkdir ~/my-new-awesome-project
cd ~/my-new-awesome-project

# Initialize git (optional)
git init
```

### **Step 2: Generate AI Documentation (Choose One)**

**🚀 Option A: One Command (Recommended)**
```bash
# Create everything directly in current directory - DONE!
./create_ai_docs.py --direct
# OR: python3 create_ai_docs.py --direct
```

**🔄 Option B: Traditional (Generate + Copy)**
```bash
# Generate templates in subdirectory 
python3 create_ai_docs.py .

# Copy all templates to project root
cp -r universal-ai-docs/* .

# Remove the temporary directory
rm -rf universal-ai-docs/
```

Both create this structure:
```
# Your project now has:
# ├── docs/
# │   ├── PROJECT_CONTEXT_PRIMING.md
# │   └── architecture_overview.md
# ├── cursor/rules/
# │   └── implementation_patterns.mdc
# ├── README.md
# ├── USAGE_GUIDE.md
# └── scripts/
#     └── setup_new_project.py
```

### **Step 3: Start Using Immediately**
The core files are ready to use without customization:

1. **Ready-to-Use Files:**
   - **`docs/PROJECT_CONTEXT_PRIMING.md`** - Use directly with AI agents ✅
   - **`docs/architecture_overview.md`** - Complete architecture guide ✅  
   - **`cursor/rules/implementation_patterns.mdc`** - Development methodology ✅

2. **Customize Only README.md:**
   - Replace placeholders like `[PROJECT_NAME]`, `[target_description]`, etc.

## 📋 **Complete Workflow Example**

Let's create a new project:

```bash
# 1. Create project
mkdir ~/my-new-project
cd ~/my-new-project

# 2. Generate everything with ONE command
./create_ai_docs.py --direct

# 3. Initialize development environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or: venv\Scripts\activate  # Windows

# 4. Create basic project structure
mkdir -p src/{core,utils,tests}
touch requirements.txt

# 5. Ready to start coding! All documentation is complete and ready.
```

The generated `docs/PROJECT_CONTEXT_PRIMING.md` contains comprehensive development standards and is ready to use immediately with any AI agent. No customization needed!

## 🤖 **AI Agent Integration**

Onboard any AI coding agent immediately with this prompt:

> **"Please read these files to understand this project:**
> **1. `docs/PROJECT_CONTEXT_PRIMING.md` - Complete project context**
> **2. `README.md` - Project overview and setup** 
> **3. `docs/architecture_overview.md` - System architecture**
> **4. `cursor/rules/implementation_patterns.mdc` - Development patterns**
> 
> **These files contain complete development standards and architecture guidance. Please help me implement features using the three-phase approach described in the methodology."**

## 🛠️ **Development Workflow**

Follow the three-phase approach from `implementation_patterns.mdc`:

### **Phase 1: Minimum Viable Implementation (30% effort)**
```python
# Basic ingredient recognition
def recognize_ingredients(image_path):
    # Simple text-based input for now
    ingredients = input("Enter ingredients separated by commas: ").split(',')
    return [ingredient.strip() for ingredient in ingredients]
```

### **Phase 2: Business Requirements (40% effort)**  
```python
# Add image processing and validation
def recognize_ingredients_with_vision(image_path):
    # Integrate with Google Vision API
    vision_result = vision_api.detect_text(image_path)
    ingredients = extract_food_items(vision_result)
    
    # Validate against known ingredient database
    validated = validate_ingredients(ingredients)
    return validated
```

### **Phase 3: Production Hardening (30% effort)**
```python
# Add AI enhancement and monitoring
async def smart_ingredient_recognition(image_path, user_preferences):
    # Multiple recognition sources
    vision_result = await vision_api.analyze(image_path)
    ai_enhancement = await openai_api.enhance_ingredient_list(vision_result)
    
    # User feedback loop
    confidence_score = calculate_confidence(vision_result, ai_enhancement)
    
    # Monitoring and analytics
    logger.info('Ingredient recognition', {
        'user_id': user_preferences.user_id,
        'confidence': confidence_score,
        'ingredients_found': len(ai_enhancement)
    })
    
    return ai_enhancement
```

## 📁 **Alternative Setup Methods**

### **Method 1: Copy Script Manually**
```bash
# Copy the generator script to your project
cp /path/to/original/create_universal_ai_docs.py .

# Run locally
python create_universal_ai_docs.py
```

### **Method 2: Git Submodule (Advanced)**
```bash
# Add as submodule for updates
git submodule add https://github.com/your-repo/universal-ai-docs.git docs-generator

# Generate templates
python docs-generator/create_universal_ai_docs.py .
```

### **Method 3: Package Installation (Future)**
```bash
# Future: Install as Python package
pip install universal-ai-docs

# Use as command
universal-ai-docs init .
```

## ✅ **Success Checklist**

After setup, verify you have:

- [ ] `docs/PROJECT_CONTEXT_PRIMING.md` ready to use (no customization needed)
- [ ] Virtual environment created and activated
- [ ] `requirements.txt` with your dependencies
- [ ] Basic project structure (`src/`, `tests/`)
- [ ] `README.md` customized with your project information
- [ ] AI agent successfully understands project context when given the prompt
- [ ] First feature implemented using three-phase approach

## 🎯 **Benefits You'll See**

Using this systematic approach:

- ✅ **30-60 minutes** from idea to working development environment
- ✅ **Immediate AI agent productivity** with comprehensive context
- ✅ **Consistent quality** across all your projects
- ✅ **Reduced over-engineering** with progressive methodology
- ✅ **Built-in best practices** for testing, documentation, architecture

## 🔄 **Keeping Templates Updated**

To get updates to the templates:

```bash
# Re-run the generator to get latest templates
create-ai-docs.py latest-templates

# Compare with your current setup
diff -r latest-templates/universal-ai-docs/ your-project/

# Merge improvements manually
```

---

**You now have a complete toolkit for efficient AI-powered development!** 🚀

Every new project starts with:
1. `./create_ai_docs.py --direct`
2. Start coding immediately!
3. Brief the AI agent
4. Start building with three-phase approach

*This systematic approach will save hours on every project and dramatically improve your AI agent collaboration effectiveness.* 