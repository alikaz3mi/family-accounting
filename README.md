# Family Accounting System

The **Family Accounting System** is designed to manage user registration, login, loan handling, payments, and group-based access control. This repository follows the **Clean Architecture** pattern, ensuring a modular, scalable, and maintainable codebase where business logic is decoupled from external layers such as databases and user interfaces.

## Features

### User Management
- **Registration**: Users can register via either Telegram or Streamlit, with the phone number as a mandatory identifier.
- **Login**: Users can log in using their phone number (as the username) via:
  - OTP (One-Time Password)
  - Password-based authentication

### Payment Handling
- **Loan Management**: Users can view and manage their loans, including a list of taken loans and payment schedules.
- **Transaction Tracking**: The system records and verifies transactions, allowing users to upload receipts (paper or internet-based) and correct transaction data. The system also extracts key information from the uploaded receipts using **OCR** (Optical Character Recognition).

### Group-Based Access Control
- **Group & GroupMember Management**: Users can be organized into groups, with the following levels of access:
  - **Owner**: Full control over the group.
  - **Administrator**: Can manage group members and tasks, with fewer privileges than the Owner.
  - **Ordinary Member**: Can only observe and view information within the group.
  
  Future access levels can be easily extended based on this flexible structure.

### OCR and Natural Language Processing

#### **OCR Integration**
The system utilizes OCR (Optical Character Recognition) to extract information from paper-based or digital receipts. This is done using:
- **EasyOCR**: A lightweight OCR solution used to scan and extract key transaction data from receipts, such as payment amounts, dates, and transaction IDs.
- **Langchain + OpenAI**: As a secondary solution, LLMs (Large Language Models) like GPT are used to enhance OCR results by interpreting complex receipt formats or unstructured data. This enables better handling of handwritten text or non-standard receipt layouts.

#### **Natural Language Processing (NLP) for User Interactions**
The system leverages **LLMs** to enable natural language processing for handling user requests. Users can ask questions or submit requests in natural language, and the system will:
- Process the requests, interpreting the intent (e.g., "What’s my loan balance?" or "Show me my last payment receipt").
- Extract relevant information from database entities (e.g., loans, transactions) using the LLMs' ability to parse and understand user queries.

This makes the system highly interactive and user-friendly, reducing the learning curve for non-technical users by allowing them to interact with the system as if they were conversing with a human.

## Clean Architecture

The system is built with **Clean Architecture** principles, meaning that the business logic is entirely decoupled from the infrastructure layer. The architecture is structured into layers:

```
family_accounting/
├── adapters                # Adapter layer (e.g., repositories)
├── entities                # Core entities for the system
├── frameworks              # Frameworks/technologies (e.g., FastAPI, PostgreSQL, etc.)
├── use_cases               # Business logic (e.g., login, registration)
│   └── interfaces          # Interfaces for dependency injection (e.g., repositories, services)
└── utils                   # Utility functions and configurations
    └── settings            # Configuration settings
```

### Entities
The core business logic entities include:
- **User**: Represents users of the system, holding information like phone number and access levels in groups.
- **Group & GroupMember**: Organize users into groups with defined roles (Owner, Admin, Member).
- **Loan**: Handles loan-related data such as loan amount, due date, and status.
- **Transaction**: Manages payment transactions and receipts, including OCR extraction and verification.
- **Authentication**: Handles user authentication methods (phone, OTP, password).

### Use Cases
Each use case focuses on a specific part of the business logic, such as user registration, login, or loan management. The use cases cannot directly access the adapter layer, and all dependencies (e.g., repositories, OTP services) are injected.

#### Registration Use Case
- Allows users to register via either Telegram or Streamlit.
- The phone number is required, and the system ensures no duplicate phone numbers are registered.
  
#### Login Use Case
- Users can log in using their phone number.
- Authentication can be done via an OTP code or password.
  
### Tools and Technologies
This project uses the following tools and libraries:
- **FastAPI**: Web framework for building APIs.
- **Python Telegram Bot**: Telegram bot integration.
- **Streamlit**: Frontend web framework for building web apps.
- **Pydantic**: Data validation and settings management using Python type hints.
- **Langchain**: For connecting to OpenAI and handling OCR tasks and natural language processing.
- **OpenAI GPT**: A large language model used to handle NLP-based user queries.
- **SQLAlchemy**: Object-relational mapper (ORM) for PostgreSQL.
- **Loguru**: Logging library for Python.
- **Pandas**: Data manipulation and analysis.
- **EasyOCR**: Optical Character Recognition (OCR) as a secondary option to OpenAI for extracting receipt data.
- **Redis**: Used for caching and message brokering.
- **Unittest**: Python's built-in testing framework.

## Installation

### Requirements
Ensure you have the following installed:
- **Python 3.9+**
- **PostgreSQL**
- **Redis**

### Step-by-Step Setup

1. **Clone the repository**
    ```bash
    git clone https://github.com/your-username/family_accounting.git
    cd family_accounting
    ```

2. **Create and activate a virtual environment**
    ```bash
    python -m venv env
    source env/bin/activate   # On Windows: env\Scripts\activate
    ```

3. **Install the dependencies**
    ```bash
    pip install -e .
    ```

4. **Setup environment variables**
    Create a `.env` file in the project root with the following variables:
    ```bash
    DATABASE_URL=postgresql://username:password@localhost/family_accounting
    REDIS_URL=redis://localhost:6379/0
    OPENAI_API_KEY=your_openai_api_key_here  # Needed for Langchain and OpenAI-based OCR/NLP
    ```

5. **Run migrations** (assuming you use Alembic for database migrations)
    ```bash
    alembic upgrade head
    ```

6. **Run the application**
    For FastAPI, you can start the application server using:
    ```bash
    uvicorn family_accounting.frameworks.api:app --reload
    ```

7. **Run tests**
    To ensure everything is working properly, run the unittests:
    ```bash
    python -m unittest discover -s tests
    ```

## Contribution

If you'd like to contribute, feel free to open an issue or submit a pull request. Please ensure your code follows the repository structure and is covered by tests.

## License

This project is licensed under the MIT License.

---

