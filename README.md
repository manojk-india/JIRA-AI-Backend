# JIRA-AI-Backend

The **JIRA-AI-Backend** is a Python-based backend system designed to enhance JIRA workflows using AI-powered tools. It leverages machine learning models, data processing pipelines, and custom scripts to automate and analyze JIRA-related tasks.

---

## Features

- **AI-Powered Query Analysis**:
  - Uses LLMs (Large Language Models) like `sambanova/DeepSeek-R1-Distill-Llama-70B` to analyze and process user queries.
  - Extracts actionable insights from user inputs.

- **Data Generation**:
  - Generates synthetic JIRA-like data for testing and analysis.
  - Supports multiple boards, sprints, and issue types.

- **Custom Database Integration**:
  - Includes modules for interacting with custom databases (`crew1_db`, `crew3_db`, etc.).

- **Vector Database Support**:
  - Stores and retrieves queries using vector databases for efficient similarity searches.


---

## Folder Structure

    JIRA-AI-Backendd/ 
    │ 
    ├── .env # Environment variables 
    ├── .gitignore # Git ignore file 
    ├── README.md # Project documentation 
    ├── requirements.txt # Python dependencies 
    ├── crew_test.py # Main script for testing Crew AI functionality 
    ├── crew1_db.py # Database module for Crew 1 
    ├── crew3_db.py # Database module for Crew 3 
    ├── crew4_db.py # Database module for Crew 4 
    ├── FIASS_Helper.py # Helper functions for vector database operations 
    ├── tester.py # Script for testing various functionalities 
    |
    ├── generated_files/ # Folder for generated data and outputs 
    │    ├── checkpoint.txt # Checkpoint file 
    │    ├── l2_board.csv # CSV file with board data 
    │    ├── new_custom.csv # Custom CSV file 
    │    ├── leave_calender.csv. #CSV file contaning leave data 
    |    ├── membership.csv  # CSV file containing Registry data.
    |
    ├── generator_files/ # Folder for data generation scripts 
    │    ├── calender.py # Script for calendar-related data 
    │    ├── data_gen.py # Script for generating synthetic JIRA data 
    │    ├── l2.py # Script for level-2 data processing 
    │    ├── membership.py # Script for membership-related data 




---

## Installation

### Prerequisites
- Python 3.10 or higher
- `pip` (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/JIRA-AI-Backend.git
   cd JIRA-AI-Backend
2. Create a virtual environment:
   ```
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate

3. Install dependencies:
   ```
   pip install -r requirements.txt

4. Set up the environment variables:
   Create a .env file in the root directory.
   Add the required variables (e.g., API keys, database credentials).

## Usage
1. Generate Synthetic Data
    Use `data_gen.py`, `l2.py`, `calender.py` and `membership.py` to generate JIRA-like data:
   ```
   python generator_files/data_gen.py
   python generator_files/l2.py
   python generator_files/calender.py
   python generator_files/ membership.py
2. Run the main script
   ```
   python crew_test.py
