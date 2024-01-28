# 🚀 Project Setup Guide

This guide outlines the steps to set up the project environment, install dependencies, and configure version control.

## Project Setup Steps:

1. **Create GitHub Repository:**
   - Go to [GitHub](https://github.com/) and log in to your account.
   - Click on the "+" sign in the top-right corner and select "New repository".
   - Enter the repository name as "datafun-03-analytics2" and add a brief description.
   - Choose the appropriate visibility (public/private) and other settings.
   - Click "Create repository" to finalize.

2. **Clone Repository:**
   - Open Git Bash or your preferred terminal.
   - Navigate to the directory where you want to store the project.
   - Use the `git clone` command to clone the repository to your local machine:
     ```
     git clone https://github.com/YourUsername/datafun-03-analytics2.git
     ```

3. **Create Virtual Environment:**
   - Navigate into the project directory:
     ```
     cd datafun-03-analytics2
     ```
   - Create a Python virtual environment named `.venv`:
     ```
     python -m venv .venv
     ```

4. **Activate Virtual Environment:**
   - Activate the virtual environment:
     - On Windows:
       ```
       .venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```
       source .venv/bin/activate
       ```

5. **Install Dependencies:**
   - Install the required Python packages using pip:
     ```
     pip install -r requirements.txt
     ```

6. **Set Up .gitignore:**
   - Create a `.gitignore` file in the project root directory.
   - Add the following lines to exclude unnecessary files and folders:
     ```
     .venv/
     .vscode/
     __pycache__/
     *.pyc
     ```

7. **Commit and Push Changes:**
   - Add the changes to the staging area:
     ```
     git add .
     ```
   - Commit the changes with a descriptive message:
     ```
     git commit -m "Initial project setup"
     ```
   - Push the changes to the GitHub repository:
     ```
     git push origin main
     ```

Congratulations! Your project environment is now set up and ready for development.
