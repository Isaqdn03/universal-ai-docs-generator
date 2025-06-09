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
        "universal-ai-docs/cursor",
        "universal-ai-docs/cursor/rules", 
        "universal-ai-docs/scripts"
    ]
    
    for dir_path in directories:
        full_path = base_path / dir_path
        full_path.mkdir(parents=True, exist_ok=True)
        print(f"✅ Created directory: {full_path}")
    
    return base_path / "universal-ai-docs"


def create_context_priming_template(output_dir):
    """Create ready-to-use AI agent context priming document."""
    content = '''# PROJECT_CONTEXT_PRIMING.md

This file provides comprehensive context for AI coding agents working on this project.

## 🎯 Project Development Context

**Development Philosophy:** Progressive enhancement with reuse-first principles  
**Primary Goal:** Build maintainable, scalable applications using proven patterns  
**Target Approach:** Three-phase implementation (MVP → Business Requirements → Production)  
**Success Criteria:** Working functionality first, then enhance systematically  

## 🏗️ Core Development Workflow

### Standard Feature Development Process
1. **Phase 1: MVP Implementation** - Get basic functionality working end-to-end
2. **Phase 2: Business Logic** - Add proper error handling, validation, business rules
3. **Phase 3: Production Ready** - Add monitoring, optimization, comprehensive testing
4. **Integration & Testing** - Ensure compatibility with existing components
5. **Documentation & Review** - Update docs and validate against architecture patterns

### Quality Gates for Each Phase
- **Phase 1:** Basic functionality works, uses existing patterns, simple tests pass
- **Phase 2:** Error handling implemented, business rules enforced, expanded test coverage
- **Phase 3:** Performance optimized, monitoring added, comprehensive tests, documentation complete

## 🔧 Technical Architecture Standards

### Recommended Technology Stack
- **Backend Framework:** Python/FastAPI, Node.js/Express, or Python/Django (choose based on team expertise)
- **Database:** PostgreSQL (primary), SQLite (development/simple projects), Redis (caching)
- **Frontend:** React, Vue.js, or modern vanilla JavaScript (web), React Native (mobile)
- **Authentication:** JWT tokens with proper validation and refresh mechanisms
- **Environment Management:** Environment variables for all configuration and secrets

### Core System Components Architecture
1. **API Layer** - RESTful endpoints with proper HTTP status codes and error handling
2. **Business Logic** - Core domain services with clear separation of concerns
3. **Data Access** - Repository pattern with database abstraction
4. **External Integrations** - Third-party API clients with retry logic and error handling
5. **Shared Utilities** - Common functions for validation, logging, authentication

### Standard Data Patterns
- **Input Validation** - Validate all inputs at API boundaries using schemas
- **Error Handling** - Structured error responses with meaningful messages
- **Logging** - Structured logging with correlation IDs for request tracing
- **Database Operations** - Use transactions for multi-step operations
- **Caching** - Cache frequently accessed data with appropriate TTL

## 🏛️ Architectural Patterns

### Primary Pattern: Modular Component Architecture
Organize code by feature/capability rather than technical layer for better maintainability and testing.

### Standard Directory Structure
```
src/
├── core/                    # Core business logic
│   ├── models/             # Data models and entities
│   ├── services/           # Business logic services
│   └── validators/         # Input validation
├── api/                    # API endpoints and routes
│   ├── routes/             # Route handlers
│   ├── middleware/         # Auth, logging, validation
│   └── schemas/            # Request/response schemas
├── data/                   # Data access layer
│   ├── repositories/       # Data access patterns
│   └── migrations/         # Database changes
├── integrations/           # External services
│   ├── third_party/        # External API clients
│   └── webhooks/          # Incoming webhooks
├── utils/                  # Shared utilities
│   ├── auth/              # Authentication helpers
│   ├── logging/           # Logging configuration
│   └── validation/        # Common validators
└── tests/                  # Test organization
    ├── unit/              # Unit tests
    ├── integration/       # Integration tests
    └── fixtures/          # Test data
```

## 🔒 Security & Quality Requirements

### Essential Security Standards
- **Authentication & Authorization** - Implement proper user verification and permission checking
- **Input Validation** - Sanitize and validate all user inputs at API boundaries
- **SQL Injection Prevention** - Use parameterized queries and ORM properly
- **Environment Security** - Store all secrets in environment variables, never in code
- **HTTPS/TLS** - Encrypt all data in transit, use secure communication protocols

### Code Quality Standards
- **Testing Requirements** - Unit tests for business logic, integration tests for APIs
- **Error Handling** - Graceful error handling with meaningful user messages
- **Logging** - Structured logging for debugging and monitoring
- **Code Review** - All code changes must be reviewed before deployment
- **Documentation** - Keep README and API documentation up to date

### Performance Requirements
- **API Response Time** - Target < 200ms for most endpoints
- **Database Queries** - Optimize queries to run < 100ms for simple operations
- **Error Rate** - Maintain < 1% error rate under normal load
- **Scalability** - Design components to handle growth without major rewrites

## 🚀 Development Workflow Standards

### Development Process
- **Feature Development** - Follow three-phase approach for all new features
- **Code Reviews** - All changes require review before merging to main branch
- **Testing Strategy** - Write tests during development, not as an afterthought
- **Documentation** - Update relevant docs with each feature or architectural change
- **Version Control** - Use clear commit messages and meaningful branch names

### Environment Management
- **Local Development** - Use virtual environments and local database instances
- **Environment Variables** - Store configuration in `.env` files (not committed)
- **Dependency Management** - Pin dependency versions in requirements files
- **Database Migrations** - Version control all database schema changes
- **Testing Data** - Use fixtures and factories for consistent test data

### Key Development Principles
1. **Reuse Before Building** - Check existing utilities and patterns before creating new ones
2. **Start Simple, Iterate** - Build working functionality first, then enhance systematically
3. **Test Throughout** - Write tests as you develop, not as a separate phase
4. **Document Context** - Keep architectural decisions and context up to date
5. **Performance Awareness** - Consider performance implications early, optimize systematically

## 🧠 Critical Context for AI Agents

### Development Context
- **Progressive Enhancement** - Always start with the simplest solution that works
- **Reuse-First Approach** - Leverage existing patterns, libraries, and utilities maximally
- **Quality Gates** - Each phase has clear completion criteria before moving forward
- **Maintainability Focus** - Code should be readable, testable, and easily modifiable

### Technical Decision Making
- **Choose Proven Technologies** - Prefer mature, well-documented technologies over cutting-edge
- **Optimize for Development Speed** - Early-stage projects prioritize rapid iteration
- **Plan for Scale** - Consider future growth without over-engineering current needs
- **Security by Design** - Build security considerations into every feature from the start

### Integration Patterns
- **External APIs** - Use standard HTTP clients with proper error handling and retries
- **Database Operations** - Leverage ORMs and connection pooling for reliability
- **Authentication** - Implement standard JWT token-based authentication
- **Logging & Monitoring** - Add structured logging to aid debugging and monitoring

## 📋 Getting Started Instructions

When working on this codebase, always:

1. **Read these key files first:**
   - `PROJECT_CONTEXT_PRIMING.md` (this file) - Overall development context and standards
   - `docs/architecture_overview.md` - Technical architecture patterns and guidelines
   - `cursor/rules/implementation_patterns.mdc` - Three-phase development methodology
   - `README.md` - Project overview and setup instructions

2. **Understand the development approach:**
   - Follow the three-phase implementation strategy for all features
   - Check existing utilities and patterns before building new functionality
   - Ensure all new code includes appropriate tests and error handling
   - Validate changes against architectural principles and quality standards

3. **Follow the established workflow:**
   - Set up local development environment with virtual environment
   - Implement features using the modular component architecture
   - Include unit tests and integration tests for each component
   - Update documentation and ensure changes align with project standards

4. **Maintain focus on:**
   - **Code Quality** - Readable, maintainable, and well-tested code
   - **Performance** - Efficient database queries and API responses
   - **Security** - Proper input validation and authentication
   - **User Experience** - Features that work reliably and intuitively

---

## 🤖 PROMPT FOR AI CODING AGENTS

To fully understand this project's development context and standards, please read the following files in order:

1. **`PROJECT_CONTEXT_PRIMING.md`** - This file containing comprehensive development context and standards
2. **`docs/architecture_overview.md`** - Technical architecture patterns, technology decisions, and implementation guidelines
3. **`cursor/rules/implementation_patterns.mdc`** - Three-phase development methodology and quality gates
4. **`README.md`** - Project overview, setup instructions, and key features

After reading these files, you will understand:
- **Development Philosophy** - Progressive enhancement and reuse-first principles
- **Technical Standards** - Architecture patterns, technology recommendations, and quality requirements
- **Implementation Strategy** - Three-phase approach with clear completion criteria for each phase
- **Code Quality Requirements** - Testing, security, performance, and documentation standards
- **Development Workflow** - How to structure code, manage environments, and integrate changes

Always refer back to these files when making decisions about implementation, architecture, or feature development. This project prioritizes maintainable, scalable code built with proven patterns and systematic quality gates.
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
    
    file_path = output_dir / "cursor" / "rules" / "implementation_patterns.mdc"
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"✅ Created: {file_path}")


def create_architecture_template(output_dir):
    """Create ready-to-use architecture overview document."""
    content = '''# Project Architecture Overview

**Document Type:** System Architecture & Development Guide  
**Purpose:** Provide AI coding agents with comprehensive technical context

---

## 🎯 Development Philosophy

This project follows **progressive enhancement** and **reuse-first principles**:

- **Start Simple, Iterate Smart** - Build working functionality first, enhance gradually
- **Reuse Before Building** - Leverage existing patterns, libraries, and utilities
- **Three-Phase Implementation** - MVP → Business Requirements → Production Hardening
- **Quality Gates** - Clear completion criteria for each development phase

---

## 🏛️ Technical Architecture Patterns

### Primary Architecture: Modular Component Structure

**Core Principle:** Organize code by capability/feature rather than technical layer, enabling independent development and testing of each feature.

#### Key Benefits
- ✅ **Independent Development** - Features can be built and tested in isolation
- ✅ **Clear Ownership** - Each module has well-defined responsibilities
- ✅ **Easy Testing** - Components have clear boundaries and interfaces
- ✅ **Scalable Growth** - New features don't impact existing functionality
- ✅ **Reusable Components** - Shared utilities prevent code duplication

#### Standard Directory Structure
```
src/
├── core/                    # Core business logic and domain models
│   ├── models/             # Data models and business entities
│   ├── services/           # Business logic services
│   └── validators/         # Input validation and business rules
├── api/                    # API layer (REST/GraphQL endpoints)
│   ├── routes/             # Route handlers and controllers
│   ├── middleware/         # Authentication, logging, validation
│   └── schemas/            # Request/response schemas
├── data/                   # Data access layer
│   ├── repositories/       # Data access patterns
│   ├── migrations/         # Database schema changes
│   └── seeders/           # Test and initial data
├── integrations/           # External service integrations
│   ├── third_party/        # External API clients
│   ├── webhooks/          # Incoming webhook handlers
│   └── notifications/      # Email, SMS, push notifications
├── utils/                  # Shared utilities and helpers
│   ├── auth/              # Authentication utilities
│   ├── logging/           # Logging and monitoring
│   ├── validation/        # Common validation functions
│   └── helpers/           # General utility functions
└── tests/                  # Test suite organization
    ├── unit/              # Unit tests by component
    ├── integration/       # Integration tests
    └── fixtures/          # Test data and mocks
```

---

## 🔧 Technology Decision Framework

### Backend Technology Selection
**Primary Considerations:**
- **Development Speed** - Framework productivity and ecosystem
- **Community Support** - Documentation, libraries, and help available
- **Deployment Simplicity** - Easy to deploy and maintain
- **Integration Capabilities** - Works well with common services and APIs

**Common Successful Patterns:**
- **Python/FastAPI** - Excellent for AI/ML integration, rapid development
- **Node.js/Express** - Great for API development, JavaScript ecosystem
- **Python/Django** - Full-featured for complex business applications
- **Go/Gin** - High performance, simple deployment

### Database Selection Guidelines
**For Most Projects:** PostgreSQL (Reliable, feature-rich, good performance)
**For Simple Projects:** SQLite (Zero configuration, file-based)
**For Analytics:** PostgreSQL + TimescaleDB (Time-series capabilities)
**For High Scale:** PostgreSQL + Redis (Caching and session storage)

### Frontend Considerations
**Web Applications:** React, Vue.js, or modern vanilla JavaScript
**Mobile:** React Native (cross-platform) or native iOS/Android
**Admin Dashboards:** React + Ant Design or Vue + Vuetify
**Simple UIs:** Server-side rendering with Tailwind CSS

---

## 📊 Data Architecture Patterns

### Standard Database Schema Approach
```sql
-- Common entity pattern with audit fields
CREATE TABLE entities (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(50) DEFAULT 'active',
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by UUID REFERENCES users(id),
    updated_by UUID REFERENCES users(id)
);

-- Relationship pattern
CREATE TABLE entity_relationships (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    parent_id UUID REFERENCES entities(id) ON DELETE CASCADE,
    child_id UUID REFERENCES entities(id) ON DELETE CASCADE,
    relationship_type VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(parent_id, child_id, relationship_type)
);
```

### Data Flow Patterns
- **Input Validation** → **Business Logic** → **Data Persistence** → **Response**
- **External APIs** → **Data Transformation** → **Local Storage** → **Application Use**
- **User Actions** → **Event Logging** → **Analytics Processing** → **Insights**

---

## 🚀 Development Workflow

### Phase 1: Minimum Viable Implementation (30% effort)
**Goal:** Get basic functionality working end-to-end

**Standards:**
- Core feature works with happy path
- Basic error handling (no crashes)
- Simple test demonstrates functionality
- Uses existing utilities where possible

**Example Approach:**
```python
def new_feature(data):
    """Phase 1: Simple, working implementation"""
    try:
        # Use existing validation
        validated_data = existing_validator.validate(data)
        
        # Simple implementation
        result = process_data(validated_data)
        
        # Basic logging
        logger.info(f"Feature used successfully: {result.id}")
        return result
    except Exception as e:
        logger.error(f"Feature error: {str(e)}")
        return None
```

### Phase 2: Business Requirements (40% effort)
**Goal:** Add essential business features and error handling

**Standards:**
- Proper error handling and edge cases
- Business rules and validation
- Integration with existing systems
- Expanded test coverage

### Phase 3: Production Hardening (30% effort)
**Goal:** Optimize for production reliability and monitoring

**Standards:**
- Performance optimization
- Comprehensive monitoring and alerting
- Full test coverage including integration tests
- Documentation and operational guides

---

## 🔒 Security & Reliability Standards

### Essential Security Measures
- **Authentication & Authorization** - Secure user verification and permission checking
- **Input Validation** - Sanitize and validate all user inputs
- **SQL Injection Prevention** - Use parameterized queries and ORMs properly
- **Environment Variables** - Store secrets in environment variables, never in code
- **HTTPS Everywhere** - Encrypt all data in transit

### Reliability Patterns
- **Graceful Error Handling** - Return meaningful errors, log for debugging
- **Health Checks** - Endpoints to verify system status
- **Database Migrations** - Version-controlled database schema changes
- **Backup Strategy** - Regular automated backups with restore testing
- **Monitoring & Alerting** - Track key metrics and alert on issues

---

## 🛠️ Common Integration Patterns

### External API Integration
```python
# Standard pattern for external API calls
class ExternalAPIClient:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url
        
    def make_request(self, endpoint, data=None):
        try:
            response = requests.post(
                f"{self.base_url}/{endpoint}",
                headers={"Authorization": f"Bearer {self.api_key}"},
                json=data,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {str(e)}")
            raise
```

### Database Connection Pattern
```python
# Use connection pooling and context managers
from contextlib import contextmanager

@contextmanager
def get_db_session():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
```

---

## 📈 Performance Guidelines

### Standard Performance Targets
- **API Response Time:** < 200ms for most endpoints
- **Database Queries:** < 100ms for simple queries
- **Page Load Time:** < 2 seconds for web interfaces
- **Error Rate:** < 1% under normal load

### Optimization Strategies
- **Database Indexing** - Index frequently queried columns
- **Caching** - Use Redis for session data and frequently accessed data
- **Pagination** - Limit result sets to reasonable sizes (50-100 items)
- **Async Processing** - Use background jobs for heavy operations

---

## 🧪 Testing Strategy

### Test Coverage Requirements
- **Unit Tests:** Core business logic functions
- **Integration Tests:** API endpoints and database operations
- **End-to-End Tests:** Critical user workflows

### Testing Patterns
```python
# Standard test structure
def test_feature_success_case():
    # Arrange
    test_data = create_test_data()
    
    # Act
    result = feature_function(test_data)
    
    # Assert
    assert result is not None
    assert result.status == "success"
    
def test_feature_error_handling():
    # Test error cases
    with pytest.raises(ValidationError):
        feature_function(invalid_data)
```

---

## 📚 Development Resources

### Essential Documentation
- **API Documentation** - OpenAPI/Swagger for all endpoints
- **Database Schema** - ERD and table documentation
- **Deployment Guide** - Step-by-step deployment instructions
- **Environment Setup** - Local development environment guide

### Code Quality Tools
- **Linting** - Consistent code style (pylint, eslint)
- **Formatting** - Automated code formatting (black, prettier)
- **Type Checking** - Static type analysis (mypy, TypeScript)
- **Security Scanning** - Dependency vulnerability checking

---

*This architecture guide provides proven patterns for building maintainable, scalable applications. Adapt these patterns to your specific project needs while maintaining the core principles of simplicity, reusability, and progressive enhancement.*
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
2. Follow the [Implementation Patterns](cursor/rules/implementation_patterns.mdc)
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
    content = '''# Universal AI Agent Documentation Suite

This directory contains proven documentation and templates for AI-powered development projects, extracted from successful real-world implementations.

## 🎯 Purpose

These documents provide a complete framework for:
- **AI Agent Context** - Comprehensive project understanding for LLMs
- **Implementation Methodology** - Proven three-phase development approach
- **Architecture Patterns** - Scalable, maintainable system design
- **Quality Assurance** - Testing and development workflows

## 📁 Documentation Files

### Core AI Agent Documents (Ready to Use)
1. **`docs/PROJECT_CONTEXT_PRIMING.md`** - Complete project context for AI agents ✅ Ready
2. **`cursor/rules/implementation_patterns.mdc`** - Development methodology and patterns ✅ Ready
3. **`docs/architecture_overview.md`** - Complete system architecture guide ✅ Ready
4. **`README.md`** - Project overview template (requires customization)

### Usage Instructions

#### 1. Copy Files to Your Project
```bash
# Copy all files
cp -r universal-ai-docs/* /path/to/your/project/

# Or copy specific files
cp universal-ai-docs/docs/PROJECT_CONTEXT_PRIMING.md /path/to/your/project/docs/
cp universal-ai-docs/cursor/rules/implementation_patterns.mdc /path/to/your/project/cursor/rules/
```

#### 2. Start Using Immediately
The core documentation files are ready to use without any customization:
- **`PROJECT_CONTEXT_PRIMING.md`** - Use directly with AI agents
- **`architecture_overview.md`** - Complete architecture guidance
- **`implementation_patterns.mdc`** - Development methodology

#### 3. Customize Only What's Needed
Only the `README.md` requires project-specific customization:
- `[PROJECT_NAME]` - Your project name
- `[target_description]` - Your project's purpose
- `[measurable_goal]` - Specific success metrics
- `[Technology]` - Your technology choices

#### 4. Fill in Project-Specific Details
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
> 4. `cursor/rules/implementation_patterns.mdc` - Development patterns
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

These documents implement a proven **Three-Phase Approach**:

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

Using these documents provides:
- **Faster Project Startup** - Proven patterns and structure
- **Better AI Agent Integration** - Comprehensive context framework
- **Higher Code Quality** - Built-in testing and quality patterns
- **Reduced Technical Debt** - Progressive enhancement methodology
- **Improved Maintainability** - Clear architecture and documentation

---

*These documents are battle-tested patterns extracted from successful AI-powered development projects. The core files are ready to use immediately, with only the README requiring project customization.*
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
    print("\\n📋 Technology Stack:")
    info['frontend_tech'] = input("Frontend Technology (e.g., React, Streamlit): ").strip()
    info['backend_tech'] = input("Backend Technology (e.g., Python, Node.js): ").strip()
    info['database_tech'] = input("Database Technology (e.g., PostgreSQL, SQLite): ").strip()
    
    # Architecture approach
    print("\\n🏗️ Architecture:")
    info['architecture_pattern'] = input("Architecture Pattern (e.g., Vertical Slice, Microservices): ").strip()
    info['domain_focus'] = input("Domain Focus (e.g., compliance-focused, performance-critical): ").strip()
    
    # Project timeline
    info['timeline'] = input("\\nProject Timeline/Deadline: ").strip()
    
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
    
    print("\\n🎉 Project '{project_info['project_name']}' created successfully!")
    print(f"📍 Location: {project_dir}")
    print("\\n📋 Next Steps:")
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
    # Check for help
    if any(arg in ['--help', '-h', 'help'] for arg in sys.argv[1:]):
        print("🚀 Universal AI Agent Documentation Generator")
        print("=" * 50)
        print("\nUsage:")
        print("  ./create_ai_docs.py [directory] [options]")
        print("  python3 create_ai_docs.py [directory] [options]")
        print("\nOptions:")
        print("  --direct, --here, -d    Create files directly in target directory")
        print("  --help, -h              Show this help message")
        print("\nExamples:")
        print("  ./create_ai_docs.py --direct")
        print("  python3 create_ai_docs.py --direct")
        print("    → Creates files directly in current directory")
        print("  ./create_ai_docs.py /path/to/project --direct")
        print("    → Creates files directly in specified directory")
        print("  python3 create_ai_docs.py .")
        print("    → Creates universal-ai-docs/ subdirectory (traditional mode)")
        return
    
    print("🚀 Generating Universal AI Agent Documentation")
    print("=" * 60)
    
    # Parse command line arguments
    direct_mode = False
    output_base = Path.cwd()
    
    for arg in sys.argv[1:]:
        if arg in ['--direct', '--here', '-d']:
            direct_mode = True
        elif not arg.startswith('-'):
            output_base = Path(arg)
    
    # Create directory structure
    if direct_mode:
        print("📁 Direct mode: Creating files in current directory")
        output_dir = output_base
        # Create necessary subdirectories directly
        (output_dir / "docs").mkdir(parents=True, exist_ok=True)
        (output_dir / "cursor" / "rules").mkdir(parents=True, exist_ok=True)
        (output_dir / "scripts").mkdir(parents=True, exist_ok=True)
    else:
        print("📁 Standard mode: Creating files in universal-ai-docs/ subdirectory")
        output_dir = create_directory_structure(output_base)
    
    print("\n📝 Creating universal documentation...")
    
    # Create all template files
    create_context_priming_template(output_dir)
    create_implementation_patterns(output_dir)
    create_architecture_template(output_dir)
    create_readme_template(output_dir)
    create_usage_guide(output_dir)
    create_project_setup_script(output_dir)
    
    print("\n🎉 Universal AI Agent Documentation Created Successfully!")
    print(f"📍 Location: {output_dir}")
    print("\n📚 Documentation Files Created:")
    print("  • docs/PROJECT_CONTEXT_PRIMING.md - Ready-to-use AI agent context")
    print("  • cursor/rules/implementation_patterns.mdc - Development methodology")
    print("  • docs/architecture_overview.md - Complete architecture guide")
    print("  • README.md - Project overview template")
    print("  • USAGE_GUIDE.md - How to use these documents")
    print("  • scripts/setup_new_project.py - Quick project setup script")
    
    if direct_mode:
        print("\n🚀 Ready to go!")
        print("  • Files created directly in your project")
        print("  • Start using PROJECT_CONTEXT_PRIMING.md with AI agents immediately")
        print("  • Customize README.md with your project details")
    else:
        print("\n🚀 Quick Start:")
        print("  1. Copy files: cp -r universal-ai-docs/* .")
        print("  2. Clean up: rm -rf universal-ai-docs/")
        print("  3. Start using PROJECT_CONTEXT_PRIMING.md with AI agents")
        print("  4. Customize README.md with your project details")
    
    print("\n✨ These documents will accelerate your AI-powered development projects!")


if __name__ == "__main__":
    main() 