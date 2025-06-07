# Challange C2S

Project developed as part of the technical test of the company Contact2Sale aimed at using LLM to understand the natural language of customers when asking for information about cars that are in our database generated with Faker.

**Note:** This setup is tailored for Linux (Ubuntu).

## Installation

Follow these steps to install and configure the project with this repository:

1. **Clone This Project**
   ```bash
   git clone https://github.com/melo-gustavo/c2s_llm_challenge.git
   ```

2. **Install Virtual Environment**
    1. Create a folder and initialize your ".venv":
      ```bash
      python3 -m venv .venv
      ```

3. **Install Dependencies of Project**
    1. Open your IDE

    2. Open the terminal

    3. Run command
      ```bash
      pip install -r requirements.txt
      ```

   3. Await install libs

4. **Install Docker Your Machine**
    1. Open your terminal

    2. Steps by install Docker
     ```bash
     https://docs.docker.com/engine/install/
     ```

5. **Run Docker and Up Postgres**
    1. Open your terminal

    2. Run command
     ```bash
     docker compose up -d
     ```

    3. Await download and install Postgres

6. **Run the Project**
    1. Open your terminal

    2. Run command
     ```bash
     python3 main.py
     ```
    3. After running main it creates the database, runs alembic and populates the database
