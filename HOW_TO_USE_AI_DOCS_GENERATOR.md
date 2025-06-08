# How to Use the Universal AI Documentation Generator

This guide shows you exactly how to use the AI documentation generator for any new project.

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

### **Step 2: Generate AI Documentation Templates**
```bash
# Generate templates in current directory
create-ai-docs.py .

# Or specify a different directory
create-ai-docs.py ~/path/to/your-project
```

### **Step 3: Copy Templates to Your Project Root**
```bash
# Copy all templates to project root
cp -r universal-ai-docs/* .

# Remove the temporary directory
rm -rf universal-ai-docs/

# Your project now has:
# ├── docs/
# │   ├── PROJECT_CONTEXT_PRIMING.md
# │   └── architecture_overview.md
# ├── .cursor/rules/
# │   └── implementation_patterns.mdc
# ├── README.md
# ├── USAGE_GUIDE.md
# └── scripts/
#     └── setup_new_project.py
```

### **Step 4: Customize for Your Project**
Edit these key files with your project details:

1. **`docs/PROJECT_CONTEXT_PRIMING.md`** (MOST IMPORTANT)
2. **`README.md`**
3. **`docs/architecture_overview.md`**

Replace all placeholders like `[PROJECT_NAME]`, `[target_description]`, etc.

## 📋 **Complete Workflow Example**

Let's create a "Smart Recipe App" project:

```bash
# 1. Create project
mkdir ~/smart-recipe-app
cd ~/smart-recipe-app

# 2. Generate AI docs
create-ai-docs.py .

# 3. Copy templates  
cp -r universal-ai-docs/* .
rm -rf universal-ai-docs/

# 4. Initialize development environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or: venv\Scripts\activate  # Windows

# 5. Create basic project structure
mkdir -p src/{core,utils,tests}
touch requirements.txt

# 6. Customize PROJECT_CONTEXT_PRIMING.md
```

Edit `docs/PROJECT_CONTEXT_PRIMING.md`:
```markdown
**Project Name:** Smart Recipe App
**Primary Goal:** Help users discover and create personalized recipes using AI
**Target Market/Users:** Home cooks aged 25-45 who want meal planning assistance
**Business Objective:** Achieve 80% user recipe completion rate with 90% satisfaction
**Timeline:** 12-week MVP, 24-week full launch

### Core Business Logic

### Recipe Discovery & Creation Workflow
1. **User Preferences** - Collect dietary restrictions, skill level, available time
2. **Ingredient Analysis** - Scan pantry via camera or manual input
3. **AI Recipe Generation** - Create personalized recipes based on preferences and ingredients  
4. **Interactive Cooking** - Step-by-step guidance with timers and tips
5. **Learning & Optimization** - Track success/failures to improve recommendations

### Technology Stack
- **Frontend:** React Native (Cross-platform mobile app)
- **Backend:** Python FastAPI (Rapid development and AI integration)
- **Database:** PostgreSQL (Complex recipe relationships)
- **AI Integration:** OpenAI API (Recipe generation and ingredient analysis)
- **Image Processing:** Google Vision API (Ingredient recognition)
```

## 🤖 **AI Agent Integration**

Once you've customized the templates, onboard any AI coding agent with this prompt:

> **"Please read these files to understand this Smart Recipe App project:**
> **1. `docs/PROJECT_CONTEXT_PRIMING.md` - Complete project context**
> **2. `README.md` - Project overview and setup** 
> **3. `docs/architecture_overview.md` - System architecture**
> **4. `.cursor/rules/implementation_patterns.mdc` - Development patterns**
> 
> **This is a user-experience-focused system where personalization and recipe accuracy are as important as technical functionality. Please help me implement the ingredient recognition feature using the three-phase approach."**

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

- [ ] `docs/PROJECT_CONTEXT_PRIMING.md` customized with your project details
- [ ] Virtual environment created and activated
- [ ] `requirements.txt` with your dependencies
- [ ] Basic project structure (`src/`, `tests/`)
- [ ] All placeholder values `[LIKE_THIS]` replaced with real information
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
1. `create-ai-docs.py .`
2. Customize PROJECT_CONTEXT_PRIMING.md
3. Brief the AI agent
4. Start building with three-phase approach

*This systematic approach will save hours on every project and dramatically improve your AI agent collaboration effectiveness.* 