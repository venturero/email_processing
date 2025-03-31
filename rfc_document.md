# RFC: Modular Order Processing System

## Meta
- **RFC Name**: Modular Order Processing System
- **RFC ID**: OPS-001
- **Start Date**: 2024-03-31
- **Owner**: Semi Venturero
- **Current Status**: DONE

## Summary
A modular Python-based order processing system that extracts order details from emails, checks warehouse availability, and generates processing narratives using OpenAI's language model.

## Motivation
The current order processing workflow is monolithic and lacks:
- Modularity
- Easy maintenance
- Clear separation of concerns
- Scalability for future enhancements

### Objectives:
- Improve code structure
- Enable easier testing and modification
- Create a flexible system for order processing
- Reduce complexity of the existing implementation

## General Design
### Data Source:
- Sample Excel/CSV files used instead of direct email script
- Reference: gmail_to_csv.py for advanced email extraction

### Components:

#### 1. Order Extractor
- Information Retrieval Approach:
  * Exclusively uses OpenAI's language model
  * Prompt-based extraction of order details
  * Standardized extraction prompt for consistent results
  * Handles varied email structures through AI's contextual understanding
  * Extracts key information:
    - Product name
    - Quantity
    - Potential additional details

#### 2. Availability Checker
**Prioritization Details:**
- Availability Levels:
  * Full Stock: Quantity >= Ordered Amount
  * Partial Stock: 0 < Quantity < Ordered Amount
  * No Stock: Quantity = 0

**Prioritization Criteria:**
- Priority 1: Full stock orders
- Priority 2: Partial stock orders
- Priority 3: No stock orders

**Additional Possible Sorting Factors:**
- Order timestamp (not implemented)
- Customer importance (not implemented)
- Previous order history (not implemented)

#### 3. Narrative Generator
**Roles and Responsibilities:**
- Production Engineer: Manage production tasks for insufficient stock (used)
- Warehouse Manager: Handle inventory locking and stock management (used)
- Sales Development Representative (SDR): Customer communication (used)
- Logistics Coordinator: Shipment and delivery coordination (used)
- Account Manager: High-level customer relationship management (not used)
- VP of Sales: Strategic oversight (not used)

### Workflow:
- Input: Email dataset from Excel/CSV
- Process: 
  a. Extract order details
  b. Check product availability
  c. Generate processing narratives
     * Assign tasks based on:
       - Order priority
       - Worker specialization
- Output: Detailed order processing instructions

## Errors
### Handling Incomplete/Missing Email Data:
**Missing/Incomplete Fields:**
- Product name
- Quantity
- Company name
- Contact information
- Pricing details

**Mitigation Strategies:**
- Default value assignment
- Partial data processing
- Flagging for manual review
- Logging incomplete entries

## Evaluation
**Acceptance Criteria:**
- Correct task assignment
- Accurate prioritization
- Comprehensive narrative generation
- Minimal manual intervention required
- High precision in order processing

## Documentation
- README.md with setup instructions
- Inline code comments
- Function and module docstrings

## Language Specifics
Platform: Check requirements.txt

## Questions

### 1. Scalability:
- Handling multiple mailboxes
- Prioritization of email sources
- Scaling for high email volumes
- Potential cloud storage integration (AWS S3)

### 2. Optimization:
**Advanced Sorting Algorithms:**
- Multi-criteria sorting (used)
- Weighted prioritization methods (not used)
- Dynamic sorting based on multiple parameters (not used)
- Machine learning-based prioritization (not used)

### 3. System Integration:
- ERP/CRM API integration (possible)
- Secure API key management via .env (used)
- Customizable integration logic (used)

### 4. Multilingual Support:
- Current: OpenAI for translation
- Future: DeepL API for enhanced accuracy
- Language detection mechanisms

## Changelog
- 2024-03-31: v.01

## Signoff
| Language | Representative     | Date
Python   | Semi Venturero | 2024-03-31
