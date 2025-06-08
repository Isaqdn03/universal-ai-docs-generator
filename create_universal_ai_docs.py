#!/usr/bin/env python3
"""
Universal AI Agent Documentation Generator

Creates a comprehensive set of documents for AI-powered development projects.
Based on proven patterns from the Roofing Lead Generation project.

Usage: python create_universal_ai_docs.py [output_directory]
"""

import os
import sys
from pathlib import Path
from datetime import datetime


def create_directory_structure(base_path):
    """Create the directory structure for universal AI docs."""
    directories = [
        "universal-ai-docs",
        "universal-ai-docs/docs",
        "universal-ai-docs/.cursor",
        "universal-ai-docs/.cursor/rules", 
        "universal-ai-docs/templates",
        "universal-ai-docs/scripts"
    ]
    
    for dir_path in directories:
        full_path = base_path / dir_path
        full_path.mkdir(parents=True, exist_ok=True)
        print(f"✅ Created directory: {full_path}")
    
    return base_path / "universal-ai-docs"


def create_context_priming_template(output_dir):
    """Create universal CONTEXT_PRIMING.md template."""
    content = '''# PROJECT_CONTEXT_PRIMING.md

This file provides comprehensive context for AI coding agents working on this project.

## Project Identity

**Project Name:** [PROJECT_NAME]
**Primary Goal:** [MAIN_BUSINESS_OBJECTIVE]
**Target Market/Users:** [TARGET_AUDIENCE]
**Business Objective:** [SPECIFIC_MEASURABLE_GOALS]
**Timeline:** [PROJECT_DEADLINE_OR_MILESTONES]

## Core Business Logic

### [Primary Process/Workflow Name]
1. **[Step 1]** - [Description of first major step]
2. **[Step 2]** - [Description of second major step]
3. **[Step 3]** - [Description of third major step]
4. **[Step 4]** - [Description of fourth major step]
5. **[Step 5]** - [Description of final step]

### Key Success Metrics
- **[Metric 1]:** [Target Value] ([Context/Baseline])
- **[Metric 2]:** [Target Value] ([Context/Baseline])
- **[Metric 3]:** [Target Value] ([Context/Baseline])
- **[Metric 4]:** [Target Value] ([Context/Baseline])
- **[Metric 5]:** [Target Value] ([Context/Baseline])

## Technical Architecture

### Technology Stack
- **Frontend:** [Technology Choice] ([Reason for choice])
- **Backend:** [Technology Choice] ([Reason for choice])
- **Database:** [Technology Choice] ([Reason for choice])
- **[Key Integration]:** [Technology Choice] ([Reason for choice])
- **[Another Integration]:** [Technology Choice] ([Reason for choice])

### Core System Components
1. **[Component 1]** - [Description and responsibility]
2. **[Component 2]** - [Description and responsibility]
3. **[Component 3]** - [Description and responsibility]
4. **[Component 4]** - [Description and responsibility]
5. **[Component 5]** - [Description and responsibility]

### Data Sources
- **[Source 1]:** [Type of data and usage]
- **[Source 2]:** [Type of data and usage]
- **[Source 3]:** [Type of data and usage]

## Architectural Patterns

### [Primary Architecture Pattern - e.g., Vertical Slice Architecture]
[Brief description of why this pattern was chosen]

### Directory Structure
```
/src
  /[capability_1]      # [Description]
    - [Key files/responsibilities]
  /[capability_2]      # [Description]
    - [Key files/responsibilities]
  /[capability_3]      # [Description]
    - [Key files/responsibilities]
  /[shared_utilities]  # [Description]
    - [Key files/responsibilities]
```

## [Domain-Specific Requirements - e.g., Compliance/Regulatory]

### [Requirement Type 1]
- [Specific requirement]
- [Another requirement]
- [Implementation approach]

### [Requirement Type 2]
- [Specific requirement]
- [Another requirement]
- [Implementation approach]

### [Important Constraints]
- [Constraint 1 and impact]
- [Constraint 2 and impact]
- [Constraint 3 and impact]

## Development Workflow

### Task Management System
- Uses [Task Management Tool/Approach]
- [Number] structured tasks with clear dependencies
- [Priority approach] development approach
- Regular progress reviews and plan adjustments

### Current Development Status
- **Phase:** [Current phase description]
- **Next Priority:** [Next major milestone]
- **Status:** [Overall project status]

### Key Development Principles
1. **[Principle 1]** - [Why this matters for this project]
2. **[Principle 2]** - [Why this matters for this project]
3. **[Principle 3]** - [Why this matters for this project]
4. **[Principle 4]** - [Why this matters for this project]
5. **[Principle 5]** - [Why this matters for this project]

## Critical Context Points

### Business Context
- [Key business driver]
- [Competitive advantage approach]
- [Revenue/value model]
- [Important timeline constraints]

### Technical Context
- [Key technical decisions and reasoning]
- [Important integrations and dependencies]
- [Performance or scale requirements]
- [Security or compliance requirements]

### [Domain-Specific Context]
- [Industry-specific considerations]
- [Regulatory or legal requirements]
- [User experience requirements]
- [Integration requirements]

## Getting Started Instructions

When working on this codebase, always:

1. **Read these key files first:**
   - `PROJECT_CONTEXT_PRIMING.md` (this file) - Overall project context
   - `[Key Document 2]` - [Description]
   - `[Key Document 3]` - [Description]
   - `[Key Document 4]` - [Description]

2. **Understand the current status:**
   - Check [task tracking system/location]
   - Verify [domain requirements] for any feature
   - Ensure changes align with [architecture pattern] patterns

3. **Follow the development workflow:**
   - Use [task management approach]
   - Implement features as [architectural unit]
   - Include tests and documentation for each component
   - Validate all [external integrations/requirements] thoroughly

4. **Maintain focus on:**
   - [Key focus area 1]
   - [Key focus area 2]
   - [Key focus area 3]
   - [Key focus area 4]

---

## PROMPT FOR AI CODING AGENTS

To fully understand this codebase and its context, please read the following files in order:

1. **`PROJECT_CONTEXT_PRIMING.md`** - This file containing comprehensive project context
2. **`[Key Document 1]`** - [Description of what it contains]
3. **`[Key Document 2]`** - [Description of what it contains]
4. **`[Key Document 3]`** - [Description of what it contains]

After reading these files, you will understand:
- The business objectives and target market/users
- Technical architecture and technology choices
- [Domain-specific] requirements and constraints
- Current development status and next priorities
- Development patterns and best practices

Always refer back to these files when making decisions about implementation, architecture, or feature development. This is a [domain-focus] system where [key constraint] is as important as technical functionality.
'''
    
    file_path = output_dir / "docs" / "PROJECT_CONTEXT_PRIMING.md"
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"✅ Created: {file_path}")


def create_implementation_patterns(output_dir):
    """Create universal implementation patterns guide."""
    content = '''# Implementation Patterns and Methodology

## Core Implementation Philosophy

- **Start Simple, Iterate Smart** - Build working first, enhance to production-ready
- **Reuse Before Building** - Check existing utilities before creating new ones  
- **Progressive Enhancement** - Three-phase approach to avoid over-engineering
- **Question Complexity** - Ask "Is this really needed now?" before adding features

## Three-Phase Implementation Strategy

### Phase 1: Minimum Viable Implementation (30% effort)
- **Goal:** Get basic functionality working
- **Focus:** Core feature works end-to-end
- **Reuse:** Leverage existing utilities and patterns maximally
- **Testing:** Basic happy path tests only
- **Time Box:** Should achieve working prototype quickly

**Example Approach:**
```python
# ✅ DO: Start simple
def new_feature(input_data):
    """Simple implementation using existing patterns"""
    try:
        # Use existing utilities where possible
        processed_data = existing_utility.process(input_data)
        result = simple_implementation(processed_data)
        log_basic_usage("feature_used", {"success": True})
        return result
    except Exception as e:
        log_basic_usage("feature_error", {"error": str(e)})
        return None

# ❌ DON'T: Start with complex custom system
class ComplexFeatureManager:  # Custom when existing works
    def __init__(self):
        self._setup_enterprise_patterns()  # Over-engineering
```

### Phase 2: Business Requirements (40% effort)
- **Goal:** Add essential business and compliance features
- **Focus:** Security, error handling, business rules
- **Testing:** Expand to cover error cases and edge scenarios
- **Documentation:** Add business context and requirements

### Phase 3: Production Hardening (30% effort)
- **Goal:** Optimize for production reliability and performance
- **Focus:** Monitoring, advanced error handling, optimization
- **Testing:** Comprehensive test coverage including integration
- **Observability:** Add detailed logging and metrics

## Decision Framework

### When to Build Comprehensive Immediately:
- **Security-critical components** (authentication, encryption, compliance)
- **User-facing features** (UI components, API endpoints)
- **Components with high failure cost** (data integrity, backup systems)

### When to Iterate Progressively:
- **Internal tools and utilities** (development helpers, scripts)
- **Features with unclear requirements** (experimental functionality)
- **Components that can be safely enhanced later** (monitoring, optimization)

## Reuse-First Guidelines

### Check Before Building:
1. **Existing Utilities:** `src/utils/` or equivalent - Look for reusable components
2. **Core Patterns:** `src/core/` or equivalent - Established architectural patterns
3. **Standard Library:** Language built-ins and common packages
4. **Project Dependencies:** Already included packages in requirements

### Common Reusable Components Pattern:
- **Configuration:** Environment variables and config file patterns
- **Logging:** Structured logging and audit trail functions
- **Validation:** Input validation and data quality patterns
- **Database:** ORM models and session management
- **Authentication:** User verification and session patterns

## Implementation Anti-Patterns to Avoid

### Over-Engineering Indicators:
- **Custom solutions when standard library works** 
- **Multi-level abstractions for simple operations**
- **Complex configuration for straightforward tasks**
- **Premature optimization before basic functionality works**

### Scope Creep Signals:
- **Adding features before core is tested**
- **Building for hypothetical future requirements**
- **Creating frameworks instead of solving specific problems**
- **Perfect error handling before basic cases work**

## Quality Gates

### Phase 1 Completion Criteria:
- [ ] Core functionality works end-to-end
- [ ] Basic error handling prevents crashes
- [ ] Simple test demonstrates functionality
- [ ] Uses existing patterns/utilities where possible
- [ ] **Tests pass in activated virtual environment**

### Phase 2 Completion Criteria:
- [ ] Security requirements implemented
- [ ] Business rules and compliance handled
- [ ] Error cases properly managed
- [ ] Integration with existing systems
- [ ] **Expanded test suite covers error scenarios**

### Phase 3 Completion Criteria:
- [ ] Production monitoring and logging
- [ ] Performance optimized for expected load
- [ ] Comprehensive test coverage
- [ ] Documentation and operational guides
- [ ] **Full test suite passes with coverage report**

## Testing and Environment Management

### Virtual Environment Requirements
**ALWAYS activate the virtual environment before any development work:**

```bash
# Check if venv exists, create if needed
if [ ! -d "venv" ]; then
    python -m venv venv
    echo "Created new virtual environment"
fi

# Activate virtual environment (REQUIRED)
source venv/bin/activate  # Linux/Mac
# or
venv\\Scripts\\activate     # Windows

# Verify activation (should show project path)
which python
pip list  # Should show project dependencies
```

### Testing Workflow for Every Feature

**Before Starting Implementation:**
```bash
# 1. Activate environment
source venv/bin/activate

# 2. Install/update dependencies if needed
pip install -r requirements.txt

# 3. Run existing tests to ensure baseline
python -m pytest -v
```

**During Implementation (After Each Significant Change):**
```bash
# Run tests for the specific feature being developed
python -m pytest test_[feature_name].py -v

# For quick validation:
python test_[feature_name].py
```

**Before Marking Feature Complete:**
```bash
# 1. Run full test suite
python -m pytest -v

# 2. Run specific feature tests with coverage
python -m pytest test_[feature_name].py --cov=[module_name] --cov-report=term

# 3. Verify no import errors
python -c "from src.[module] import *; print('✅ Imports successful')"

# 4. Run integration tests if they exist
python -m pytest tests/integration/ -v
```

### Test Creation Standards

**Every feature MUST include:**
1. **Basic functionality test** - Core feature works
2. **Error handling test** - Graceful failure scenarios  
3. **Integration test** - Works with existing systems
4. **Edge case test** - Boundary conditions and unusual inputs

**Test File Naming:**
- `test_[feature_name].py` - Main test file
- `test_[feature_name]_integration.py` - Integration tests
- `test_[feature_name]_performance.py` - Performance tests

### Environment Troubleshooting

**Common Issues:**
```bash
# Wrong Python version
python --version  # Should match project requirements

# Missing dependencies
pip install -r requirements.txt

# Virtual environment not activated
which python  # Should point to venv/bin/python

# Module import errors
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

## Success Metrics

- **Time to working prototype:** < 30% of total implementation time
- **Reuse ratio:** > 50% of functionality leverages existing code
- **Code review question:** "Could this be simpler?"
- **Test progression:** Basic → Business → Comprehensive

## Project Context Integration

### Always Consider:
- **[Domain Requirements]:** [Specific requirements for your domain]
- **Business Criticality:** Impact on main business workflow
- **Human Oversight:** Requirements for manual review/approval
- **Data Security:** [Data protection requirements for your domain]

### Typical Implementation Priority:
1. **Core business function** ([main business capability])
2. **[Domain requirements]** ([specific compliance/security needs])  
3. **Automation and optimization** (scheduling, performance)
4. **Monitoring and reliability** (alerting, error recovery)

---

*Apply these patterns consistently across all project development for reliable, maintainable, and efficient code delivery.*
'''
    
    file_path = output_dir / ".cursor" / "rules" / "implementation_patterns.mdc"
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"✅ Created: {file_path}")


def create_architecture_template(output_dir):
    """Create universal architecture overview template."""
    content = '''# [PROJECT_NAME] - Architecture Overview

**Version:** 1.0  
**Last Updated:** [DATE]  
**Document Type:** System Architecture Documentation

---

## 📋 Executive Summary

This document provides a comprehensive architectural overview of [PROJECT_NAME], a [project_description] system designed for [target_domain]. The system leverages [key_technologies] and [key_architectural_principle] as core architectural principles, following [architectural_pattern] patterns optimized for [optimization_goals].

---

## 🎯 Business Architecture

### Core Value Proposition
- **Target Market:** [target_users_or_market]
- **Business Goal:** [specific_measurable_business_goal]
- **Competitive Advantage:** [key_differentiator]
- **Timeline:** [project_timeline_or_deadline]
- **Success Metrics:**
  - [Metric 1]: [Target value]
  - [Metric 2]: [Target value]
  - [Metric 3]: [Target value]
  - [Metric 4]: [Target value]
  - [Metric 5]: [Target value]

### [Primary Business Process Name]
```
[Step 1] → [Step 2] → [Step 3] → [Step 4] → [Step 5]
```

#### Detailed Process Flow
1. **[Step 1]** - [Description of first major step]
2. **[Step 2]** - [Description of second major step]
3. **[Step 3]** - [Description of third major step]
4. **[Step 4]** - [Description of fourth major step]
5. **[Step 5]** - [Description of final step]

---

## 🏛️ Technical Architecture

### Architecture Pattern: [Primary Pattern Name]

**Core Principle:** [Description of architectural approach and why it was chosen]

#### [Pattern Name] Benefits
- ✅ **[Benefit 1]** - [Description]
- ✅ **[Benefit 2]** - [Description]
- ✅ **[Benefit 3]** - [Description]
- ✅ **[Benefit 4]** - [Description]
- ✅ **[Benefit 5]** - [Description]

#### Implementation Structure
```
/src/[main_source_dir]/
├── [capability_1]/     # [Description]
│   ├── [sub_component_1]/ # [Responsibility]
│   ├── [sub_component_2]/ # [Responsibility]
│   └── [sub_component_3]/ # [Responsibility]
├── [capability_2]/     # [Description]
│   ├── [sub_component_1]/ # [Responsibility]
│   ├── [sub_component_2]/ # [Responsibility]
│   └── [sub_component_3]/ # [Responsibility]
├── [capability_3]/     # [Description]
│   ├── [sub_component_1]/ # [Responsibility]
│   ├── [sub_component_2]/ # [Responsibility]
│   └── [sub_component_3]/ # [Responsibility]
└── [shared_utilities]/ # [Description]
    ├── [utility_type_1]/ # [Responsibility]
    ├── [utility_type_2]/ # [Responsibility]
    └── [utility_type_3]/ # [Responsibility]
```

### Technology Stack Analysis

| Layer | Technology | Rationale | Rating | Notes |
|-------|------------|-----------|---------|-------|
| **Frontend** | [Technology] | [Reason] | ⭐⭐⭐⭐ | [Context] |
| **Backend** | [Technology] | [Reason] | ⭐⭐⭐⭐⭐ | [Context] |
| **Database** | [Technology] | [Reason] | ⭐⭐⭐⭐ | [Context] |
| **[Key Integration]** | [Technology] | [Reason] | ⭐⭐⭐⭐⭐ | [Context] |
| **[Another Integration]** | [Technology] | [Reason] | ⭐⭐⭐⭐ | [Context] |

---

## 🔧 System Components Deep Dive

### 1. [Component Category 1]

#### [Component 1A]
- **[Integration Type]:** [Description]
- **[Key Feature]:** [Implementation approach]
- **[Key Feature]:** [Implementation approach]
- **[Key Feature]:** [Implementation approach]

#### [Component 1B]
- **[Key Feature]:** [Implementation approach]
- **[Key Feature]:** [Implementation approach]
- **[Key Feature]:** [Implementation approach]

### 2. [Component Category 2]

#### [Component 2A]
- **[Key Feature]:** [Implementation approach]
- **[Key Feature]:** [Implementation approach]
- **[Key Feature]:** [Implementation approach]

#### [Component 2B]
- **[Key Feature]:** [Implementation approach]
- **[Key Feature]:** [Implementation approach]
- **[Key Feature]:** [Implementation approach]

### 3. [Component Category 3]

#### [Component 3A]
- **[Key Feature]:** [Implementation approach]
- **[Key Feature]:** [Implementation approach]
- **[Key Feature]:** [Implementation approach]

---

## 📊 Data Architecture

### Database Schema Design

#### Core Entities
```sql
-- [Primary Entity] table
[primary_entities] (
    id UUID PRIMARY KEY,
    [field_1] VARCHAR([size]) NOT NULL,
    [field_2] VARCHAR([size]) NOT NULL,
    [field_3] DECIMAL([precision],[scale]),
    [field_4] DECIMAL([precision],[scale]),
    [field_5] INTEGER,
    [field_6] TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- [Secondary Entity] table
[secondary_entities] (
    id UUID PRIMARY KEY,
    [primary_entity]_id UUID REFERENCES [primary_entities](id),
    [field_1] VARCHAR([size]),
    [field_2] VARCHAR([size]),
    [field_3] TIMESTAMP,
    [field_4] VARCHAR([size]),
    [field_5] BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Data Flow Patterns
- **[Data Source 1]** → [Processing] → [Storage/Usage]
- **[Data Source 2]** → [Processing] → [Storage/Usage]
- **[Data Source 3]** → [Processing] → [Storage/Usage]

---

## 🔒 [Domain-Specific Requirements]

### [Requirement Category 1]
- **[Specific Requirement]:** [Implementation approach]
- **[Specific Requirement]:** [Implementation approach]
- **[Specific Requirement]:** [Implementation approach]

### [Requirement Category 2]
- **[Specific Requirement]:** [Implementation approach]
- **[Specific Requirement]:** [Implementation approach]
- **[Specific Requirement]:** [Implementation approach]

---

## 🚀 Development and Deployment

### Development Environment Setup
1. **[Setup Step 1]:** [Instructions]
2. **[Setup Step 2]:** [Instructions]
3. **[Setup Step 3]:** [Instructions]
4. **[Setup Step 4]:** [Instructions]

### Key Development Patterns
- **[Pattern 1]:** [Description and usage]
- **[Pattern 2]:** [Description and usage]
- **[Pattern 3]:** [Description and usage]

### Integration Points
- **[Integration 1]:** [How it connects and data flow]
- **[Integration 2]:** [How it connects and data flow]
- **[Integration 3]:** [How it connects and data flow]

---

## 📈 Performance and Scalability

### Performance Targets
- **[Metric 1]:** [Target] ([Context])
- **[Metric 2]:** [Target] ([Context])
- **[Metric 3]:** [Target] ([Context])

### Scalability Considerations
- **[Aspect 1]:** [Current limit] → [Scale target] ([Approach])
- **[Aspect 2]:** [Current limit] → [Scale target] ([Approach])
- **[Aspect 3]:** [Current limit] → [Scale target] ([Approach])

---

## 🛡️ Security and Reliability

### Security Measures
- **[Security Aspect 1]:** [Implementation]
- **[Security Aspect 2]:** [Implementation]
- **[Security Aspect 3]:** [Implementation]

### Reliability Patterns
- **[Reliability Feature 1]:** [Implementation]
- **[Reliability Feature 2]:** [Implementation]
- **[Reliability Feature 3]:** [Implementation]

---

## 📚 References and Resources

### Technical Documentation
- **[Resource 1]:** [Description and link]
- **[Resource 2]:** [Description and link]
- **[Resource 3]:** [Description and link]

### [Domain-Specific] Resources
- **[Resource 1]:** [Description and link]
- **[Resource 2]:** [Description and link]
- **[Resource 3]:** [Description and link]

---

*This architecture overview provides the foundation for understanding and extending [PROJECT_NAME]. All development should align with these architectural principles and patterns.*
'''
    
    file_path = output_dir / "docs" / "architecture_overview.md"
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"✅ Created: {file_path}")


def create_readme_template(output_dir):
    """Create universal README template."""
    content = '''# [PROJECT_NAME]

[Brief project description - what it does and why it's valuable]

## 🎯 Project Overview

This system [target_description], aiming to [measurable_goal] through:

- **[Key Capability 1]** - [Description]
- **[Key Capability 2]** - [Description]
- **[Key Capability 3]** - [Description]
- **[Key Capability 4]** - [Description]
- **[Key Capability 5]** - [Description]
- **[Key Capability 6]** - [Description]

## 🏗️ Architecture

### Technology Stack
- **Frontend:** [Technology] ([Reason])
- **Backend:** [Technology] ([Reason])
- **Database:** [Technology] ([Reason])
- **[Key Integration]:** [Technology] ([Reason])
- **[Another Integration]:** [Technology] ([Reason])

### Project Structure
```
├── src/
│   ├── [main_app_dir]/        # [Description]
│   │   ├── [app_file].py      # [Responsibility]
│   │   ├── [sub_dir]/         # [Responsibility]
│   │   └── [components]/      # [Responsibility]
│   ├── [capability_1]/        # [Description]
│   │   ├── [sub_component_1]/ # [Responsibility]
│   │   ├── [sub_component_2]/ # [Responsibility]
│   │   └── [sub_component_3]/ # [Responsibility]
│   ├── [capability_2]/        # [Description]
│   ├── [shared_utilities]/    # [Description]
│   └── tests/                 # Test suite
├── [data_dir]/                # [Description]
├── [config_dir]/              # [Description]
├── [automation_dir]/          # [Description]
└── docs/                      # Documentation
```

## 🚀 Quick Start

### Prerequisites
- [Language/Runtime] [version] or higher
- [Dependency manager]
- [Required service/tool 1]
- [Required service/tool 2]
- API keys for:
  - [Service 1]
  - [Service 2]
  - [Service 3]

### Installation

1. **Clone the repository:**
   ```bash
   git clone [repository-url]
   cd [project-directory]
   ```

2. **Create and activate virtual environment:**
   ```bash
   [venv_creation_command]
   [venv_activation_command]
   ```

3. **Install dependencies:**
   ```bash
   [dependency_install_command]
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and configuration
   ```

5. **Initialize the [database/system]:**
   ```bash
   [initialization_command]
   ```

6. **Run the application:**
   ```bash
   [run_command]
   ```

## 📋 Configuration

### Environment Variables
Copy `.env.example` to `.env` and configure:

- **[Service Category 1]:** [List of required variables]
- **[Service Category 2]:** [List of required variables]
- **[Service Category 3]:** [List of required variables]
- **[Company/System Info]:** [Required for domain requirements]

### Configuration Files
- `config/[environment1].yaml` - [Environment] settings
- `config/[environment2].yaml` - [Environment] settings

## 🔧 Development

### Running Tests
```bash
# Run all tests
[test_command]

# Run with coverage
[coverage_command]

# Run specific test types
[specific_test_command1]
[specific_test_command2]
```

### Code Formatting
```bash
# Format code
[format_command]

# Check linting
[lint_command]
```

### Pre-commit Hooks
```bash
# Install pre-commit hooks
[pre_commit_install]

# Run manually
[pre_commit_run]
```

## 📊 Key Features

### 1. [Feature Category 1]
- [Feature description]
- [Feature description]
- [Feature description]
- [Feature description]

### 2. [Feature Category 2]
- [Feature description]
- [Feature description]
- [Feature description]
- [Feature description]

### 3. [Feature Category 3]
- [Feature description]
- [Feature description]
- [Feature description]
- [Feature description]

### 4. [Feature Category 4]
- [Feature description]
- [Feature description]
- [Feature description]
- [Feature description]

## 📈 Success Metrics

- **[Metric 1]:** [Target] ([Context])
- **[Metric 2]:** [Target] ([Context])
- **[Metric 3]:** [Target] ([Context])
- **[Metric 4]:** [Target] ([Context])
- **[Metric 5]:** [Target] ([Context])

## 🔒 [Domain Requirements - e.g., Compliance & Legal]

This system is designed with [domain_focus] as a primary concern:

### [Requirement Category 1]
- [Specific requirement and implementation]
- [Specific requirement and implementation]
- [Specific requirement and implementation]
- [Specific requirement and implementation]

### [Requirement Category 2]
- [Specific requirement and implementation]
- [Specific requirement and implementation]
- [Specific requirement and implementation]
- [Specific requirement and implementation]

### [Important Constraints]
- [Constraint and handling approach]
- [Constraint and handling approach]
- [Constraint and handling approach]

## 📚 Documentation

- [API Documentation](docs/api_documentation.md)
- [Deployment Guide](docs/deployment_guide.md)
- [Architecture Overview](docs/architecture_overview.md)
- [Development Workflow](docs/development_workflow.md)

## 🤝 Contributing

1. Read the [Project Context](docs/PROJECT_CONTEXT_PRIMING.md)
2. Follow the [Implementation Patterns](.cursor/rules/implementation_patterns.mdc)
3. Ensure all tests pass
4. Verify [domain requirements] compliance
5. Submit pull request with clear description

## 📄 License

[License information]

---

**Remember:** This is a [domain_focus] system where [key_constraint] is as important as technical functionality.
'''
    
    file_path = output_dir / "README.md"
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"✅ Created: {file_path}")


def create_usage_guide(output_dir):
    """Create usage guide for the universal templates."""
    content = '''# Universal AI Agent Documentation Templates

This directory contains proven templates for AI-powered development projects, extracted from successful real-world implementations.

## 🎯 Purpose

These templates provide a complete framework for:
- **AI Agent Context** - Comprehensive project understanding for LLMs
- **Implementation Methodology** - Proven three-phase development approach
- **Architecture Patterns** - Scalable, maintainable system design
- **Quality Assurance** - Testing and development workflows

## 📁 Template Files

### Core AI Agent Documents
1. **`docs/PROJECT_CONTEXT_PRIMING.md`** - Complete project context for AI agents
2. **`.cursor/rules/implementation_patterns.mdc`** - Development methodology and patterns
3. **`docs/architecture_overview.md`** - System architecture documentation template
4. **`README.md`** - Project overview and setup template

### Usage Instructions

#### 1. Copy Templates to Your Project
```bash
# Copy all templates
cp -r universal-ai-docs/* /path/to/your/project/

# Or copy specific templates
cp universal-ai-docs/docs/PROJECT_CONTEXT_PRIMING.md /path/to/your/project/docs/
cp universal-ai-docs/.cursor/rules/implementation_patterns.mdc /path/to/your/project/.cursor/rules/
```

#### 2. Customize for Your Project
Replace all placeholder values:
- `[PROJECT_NAME]` - Your project name
- `[target_description]` - Your project's purpose
- `[measurable_goal]` - Specific success metrics
- `[Technology]` - Your technology choices
- `[domain_focus]` - Your industry/domain (e.g., "compliance-focused", "performance-critical")

#### 3. Fill in Project-Specific Details
- Business objectives and success metrics
- Technology stack with rationale
- Architecture patterns and component structure
- Domain-specific requirements (compliance, security, etc.)
- Development workflow and quality gates

## 🚀 Quick Project Setup

For a new project:

1. **Initialize Project Structure:**
```bash
mkdir my-new-project
cd my-new-project
cp -r /path/to/universal-ai-docs/* .
```

2. **Customize Core Context:**
- Edit `docs/PROJECT_CONTEXT_PRIMING.md` with your project details
- Update `README.md` with your project information
- Modify `docs/architecture_overview.md` for your system design

3. **Set Up Development Environment:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\\Scripts\\activate  # Windows

pip install -r requirements.txt  # Create this file with your dependencies
```

4. **Initialize AI Agent Context:**
When working with AI agents, provide this prompt:

> "Please read the following files to understand this project:
> 1. `docs/PROJECT_CONTEXT_PRIMING.md` - Complete project context
> 2. `README.md` - Project overview and setup
> 3. `docs/architecture_overview.md` - System architecture
> 4. `.cursor/rules/implementation_patterns.mdc` - Development patterns
> 
> After reading these, you'll understand the business goals, technical architecture, and development approach."

## 🎨 Customization Patterns

### For Different Project Types

#### Business Applications
- Focus on compliance and regulatory requirements
- Emphasize human oversight and approval workflows
- Include audit trails and data protection

#### Developer Tools
- Emphasize ease of use and developer experience
- Focus on performance and reliability patterns
- Include extensive testing and documentation

#### Data/AI Projects
- Highlight data pipeline and model architecture
- Focus on experiment tracking and reproducibility
- Include data quality and validation patterns

#### Web Applications
- Emphasize scalability and user experience
- Focus on security and performance patterns
- Include deployment and monitoring approaches

## 📋 Implementation Methodology

These templates implement a proven **Three-Phase Approach**:

### Phase 1: Minimum Viable Implementation (30% effort)
- Get basic functionality working
- Use existing patterns and utilities
- Basic testing and validation

### Phase 2: Business Requirements (40% effort)
- Add security and compliance features
- Implement error handling and edge cases
- Expand testing coverage

### Phase 3: Production Hardening (30% effort)
- Add monitoring and observability
- Optimize performance and reliability
- Comprehensive testing and documentation

## 🔧 Development Best Practices

### Always Follow These Patterns:
1. **Virtual Environment First** - Always activate venv before development
2. **Reuse Before Building** - Check existing utilities before creating new ones
3. **Test Throughout** - Test after each significant change
4. **Document Context** - Keep AI agent context up to date
5. **Quality Gates** - Meet completion criteria for each phase

### Success Metrics:
- **Time to Working Prototype:** < 30% of total time
- **Reuse Ratio:** > 50% functionality uses existing patterns
- **Test Coverage:** Progressive (basic → comprehensive)
- **AI Agent Efficiency:** Clear context reduces development time

## 🎯 Benefits

Using these templates provides:
- **Faster Project Startup** - Proven patterns and structure
- **Better AI Agent Integration** - Comprehensive context framework
- **Higher Code Quality** - Built-in testing and quality patterns
- **Reduced Technical Debt** - Progressive enhancement methodology
- **Improved Maintainability** - Clear architecture and documentation

---

*These templates are battle-tested patterns extracted from successful AI-powered development projects. Adapt them to your specific needs while maintaining the core methodology.*
'''
    
    file_path = output_dir / "USAGE_GUIDE.md"
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"✅ Created: {file_path}")


def create_project_setup_script(output_dir):
    """Create a script to quickly set up new projects with these templates."""
    content = '''#!/usr/bin/env python3
"""
Quick Project Setup Script

Creates a new project using the universal AI agent templates.
Prompts for project-specific information and customizes templates accordingly.

Usage: python setup_new_project.py [project_name]
"""

import os
import sys
import shutil
from pathlib import Path
from datetime import datetime


def get_project_info():
    """Collect project information from user."""
    print("🚀 Universal AI Agent Project Setup")
    print("=" * 50)
    
    info = {}
    
    # Basic project info
    info['project_name'] = input("Project Name: ").strip()
    info['project_description'] = input("Brief Description: ").strip()
    info['target_audience'] = input("Target Users/Market: ").strip()
    info['main_goal'] = input("Main Business Objective: ").strip()
    
    # Technical choices
    print("\n📋 Technology Stack:")
    info['frontend_tech'] = input("Frontend Technology (e.g., React, Streamlit): ").strip()
    info['backend_tech'] = input("Backend Technology (e.g., Python, Node.js): ").strip()
    info['database_tech'] = input("Database Technology (e.g., PostgreSQL, SQLite): ").strip()
    
    # Architecture approach
    print("\n🏗️ Architecture:")
    info['architecture_pattern'] = input("Architecture Pattern (e.g., Vertical Slice, Microservices): ").strip()
    info['domain_focus'] = input("Domain Focus (e.g., compliance-focused, performance-critical): ").strip()
    
    # Project timeline
    info['timeline'] = input("\nProject Timeline/Deadline: ").strip()
    
    return info


def customize_template_file(file_path, replacements):
    """Replace placeholders in a template file."""
    if not file_path.exists():
        return
        
    with open(file_path, 'r') as f:
        content = f.read()
    
    for placeholder, value in replacements.items():
        content = content.replace(placeholder, value)
    
    with open(file_path, 'w') as f:
        f.write(content)


def setup_project(project_info, template_dir, output_dir):
    """Set up new project with customized templates."""
    project_dir = Path(output_dir) / project_info['project_name'].lower().replace(' ', '-')
    
    # Create project directory
    project_dir.mkdir(parents=True, exist_ok=True)
    print(f"📁 Created project directory: {project_dir}")
    
    # Copy template files
    template_path = Path(template_dir)
    for item in template_path.rglob('*'):
        if item.is_file() and not item.name.startswith('.git'):
            relative_path = item.relative_to(template_path)
            target_path = project_dir / relative_path
            target_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, target_path)
    
    # Prepare replacements
    replacements = {
        '[PROJECT_NAME]': project_info['project_name'],
        '[project_description]': project_info['project_description'],
        '[target_description]': project_info['target_audience'],
        '[measurable_goal]': project_info['main_goal'],
        '[Technology]': f"{project_info['frontend_tech']}, {project_info['backend_tech']}, {project_info['database_tech']}",
        '[architectural_pattern]': project_info['architecture_pattern'],
        '[domain_focus]': project_info['domain_focus'],
        '[project_timeline_or_deadline]': project_info['timeline'],
        '[DATE]': datetime.now().strftime('%Y-%m-%d'),
    }
    
    # Customize key files
    key_files = [
        'docs/PROJECT_CONTEXT_PRIMING.md',
        'README.md',
        'docs/architecture_overview.md'
    ]
    
    for file_path in key_files:
        full_path = project_dir / file_path
        if full_path.exists():
            customize_template_file(full_path, replacements)
            print(f"✅ Customized: {file_path}")
    
    print("\n🎉 Project '{project_info['project_name']}' created successfully!")
    print(f"📍 Location: {project_dir}")
    print("\n📋 Next Steps:")
    print("1. cd into the project directory")
    print("2. Create virtual environment: python -m venv venv")
    print("3. Activate virtual environment: source venv/bin/activate")
    print("4. Create requirements.txt with your dependencies")
    print("5. Read USAGE_GUIDE.md for detailed instructions")
    print("6. Customize docs/PROJECT_CONTEXT_PRIMING.md with more details")


def main():
    """Main setup function."""
    if len(sys.argv) > 1:
        project_name = sys.argv[1]
        # Use provided project name and ask for other details
        project_info = get_project_info()
        project_info['project_name'] = project_name
    else:
        project_info = get_project_info()
    
    # Assume templates are in the same directory as this script
    template_dir = Path(__file__).parent
    output_dir = Path.cwd()
    
    setup_project(project_info, template_dir, output_dir)


if __name__ == "__main__":
    main()
'''
    
    file_path = output_dir / "scripts" / "setup_new_project.py"
    with open(file_path, 'w') as f:
        f.write(content)
    
    # Make it executable
    os.chmod(file_path, 0o755)
    print(f"✅ Created: {file_path}")


def main():
    """Main function to generate all universal AI documentation."""
    print("🚀 Generating Universal AI Agent Documentation Templates")
    print("=" * 60)
    
    # Determine output directory
    if len(sys.argv) > 1:
        output_base = Path(sys.argv[1])
    else:
        output_base = Path.cwd()
    
    # Create directory structure
    output_dir = create_directory_structure(output_base)
    
    print("\n📝 Creating universal templates...")
    
    # Create all template files
    create_context_priming_template(output_dir)
    create_implementation_patterns(output_dir)
    create_architecture_template(output_dir)
    create_readme_template(output_dir)
    create_usage_guide(output_dir)
    create_project_setup_script(output_dir)
    
    print("\n🎉 Universal AI Agent Documentation Created Successfully!")
    print(f"📍 Location: {output_dir}")
    print("\n📚 Template Files Created:")
    print("  • docs/PROJECT_CONTEXT_PRIMING.md - AI agent context template")
    print("  • .cursor/rules/implementation_patterns.mdc - Development methodology")
    print("  • docs/architecture_overview.md - Architecture documentation template")
    print("  • README.md - Project overview template")
    print("  • USAGE_GUIDE.md - How to use these templates")
    print("  • scripts/setup_new_project.py - Quick project setup script")
    
    print("\n🚀 Quick Start:")
    print("  1. Read USAGE_GUIDE.md for detailed instructions")
    print("  2. Copy templates to your new project")
    print("  3. Customize placeholders with your project details")
    print("  4. Use PROJECT_CONTEXT_PRIMING.md to brief AI agents")
    
    print("\n✨ These templates will accelerate your AI-powered development projects!")


if __name__ == "__main__":
    main() 