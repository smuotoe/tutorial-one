# Virtual Environments Hands-on Exercise

## Objective
In this exercise, you'll compare the setup speed and usage of traditional `venv` with the newer `uv` tool by creating two identical project environments. This hands-on comparison will help you understand the benefits and differences between these tools.

## Prerequisites
- Python 3.10 or higher installed
- `uv` installed <https://docs.astral.sh/uv/getting-started/installation/>
  - **Windows PowerShell**:
    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```
  - **macOS/Linux**:
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
  
- Access to a terminal or command prompt

## Part 1: Traditional venv Setup

### Creating the Environment
1. Open your terminal and create a new project directory:
   ```bash
   mkdir tutorial-one
   cd tutorial-one
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - **Windows PowerShell**:
     ```powershell
     .venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source .venv/bin/activate
     ```

### Installing Packages
4. Install common packages and measure the time:
   - **Windows PowerShell**:
     ```powershell
     Measure-Command { pip install pandas numpy matplotlib requests scikit-learn black}
     ```
   - **macOS/Linux**:
     ```bash
     time pip install pandas numpy matplotlib requests
     ```

5. Create a requirements file:
   ```bash
   pip freeze > requirements.txt
   ```

6. Deactivate the environment:
   ```bash
   deactivate
   ```

## Part 2: UV Setup

### Creating the Environment
1. Initialize a new Python project with UV:
   ```bash
   uv init
   ```

2. Create and activate the environment:
   ```bash
   uv venv
   ```

3. Activate the environment (same commands as venv above)

### Installing Packages
4. Install the same packages and measure time:
   - **Windows PowerShell**:
     ```powershell
     Measure-Command { uv add pandas numpy matplotlib requests scikit-learn black}
     ```
   - **macOS/Linux**:
     ```bash
     time uv add pandas numpy matplotlib requests
     ```
