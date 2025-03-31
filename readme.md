# Order Processing System

## Overview
This modular Python-based system processes email orders, checks warehouse availability, and generates processing narratives using OpenAI's language model.

## Features
- Email order extraction
- Warehouse availability checking
- Automated task generation
- Modular system architecture

## Prerequisites
- Python 3.8+
- OpenAI API Key
- Access to sample email and warehouse CSV files

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/venturero/email_processing.git
cd email_processing

## Setup

### 1. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment
Create a `.env` file in the project root:

```bash
echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
```

## Project Structure

```bash
order_processing/
│
├── src/
│   ├── __init__.py
│   ├── order_extractor.py
│   ├── availability_checker.py
│   └── narrative_generator.py
│
├── data/
│   ├── emails.csv
│   └── warehouse.csv
│
├── utils/
│   └── config.py
│
├── main.py
└── requirements.txt
```

## Usage

```bash
python main.py
```

## Configuration

Modify `utils/config.py` to adjust:

```bash
# File paths
DATA_PATH = "data"

# Processing parameters
PROCESSING_SPEED = "fast"

# Deadline settings
DEADLINE = "2025-12-31"
```

## Error Handling

```bash
- Logs incomplete email data
- Provides default values
- Flags entries requiring manual review
```

## Limitations

```bash
- Relies on OpenAI for email parsing
- Limited to CSV file inputs
- Dependent on email structure consistency
```

## Future Improvements

```bash
- Multiple mailbox support
- Advanced sorting algorithms
- ERP/CRM integration
- Multilingual processing with deepl
```

## Troubleshooting

```bash
- Ensure OpenAI API key is valid
- Check CSV file formatting
- Verify Python and library versions
```

## Contributing

```bash
1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Create a pull request
```

## Contact

```bash
Semi Venturero
📧 Linkedin: https://www.linkedin.com/in/semi/
```

