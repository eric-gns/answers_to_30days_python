# ==============================================================================
# 30 DAYS OF PYTHON - DAY 23: VIRTUAL ENVIRONMENTS (venv)
# TERMINAL COMMAND COMPILATION (WINDOWS 11 / POWERSHELL)
# ==============================================================================

# ------------------------------------------------------------------------------
# STEP 1: CREATE A VIRTUAL ENVIRONMENT
# Creates an isolated Python environment folder named 'venv' inside project directory
# ------------------------------------------------------------------------------
#python -m venv venv

# ------------------------------------------------------------------------------
# STEP 2: CONFIGURE POWERSHELL EXECUTION POLICY
# Permits local script execution for the current user account to fix PSSecurityException
# ------------------------------------------------------------------------------
#Get-ExecutionPolicy
#Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# ------------------------------------------------------------------------------
# STEP 3: ACTIVATE THE VIRTUAL ENVIRONMENT
# Switches terminal prompt to operate inside the isolated bubble (adds (venv) prefix)
# ------------------------------------------------------------------------------
#.\venv\Scripts\Activate.ps1

# ------------------------------------------------------------------------------
# STEP 4: PACKAGE MANAGEMENT & DEPENDENCY EXPORT
# Check clean slate, install initial package, and freeze state to requirements.txt
# ------------------------------------------------------------------------------
#pip list
#pip install requests
#pip freeze > requirements.txt

# ------------------------------------------------------------------------------
# STEP 5: DEACTIVATE ENVIRONMENT
# Return terminal back to system global Python installation
# ------------------------------------------------------------------------------
#deactivate

# ==============================================================================
# DAY 23 PRACTICAL CHALLENGE: DATA & WEB STACK ENVIRONMENT SETUP
# ==============================================================================

# 1. Create a custom named virtual environment
#python -m venv my_env

# 2. Activate custom environment
#.\my_env\Scripts\Activate.ps1

# 3. Install target libraries (including package typo correction: panda -> pandas)
#pip install flask numpy panda
#pip uninstall panda -y
#pip install pandas

# 4. Generate final production requirements file
#pip freeze > requirements.txt

# 5. Exit environment
#deactivate