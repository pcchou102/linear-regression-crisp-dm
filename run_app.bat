@echo off
echo ===================================
echo  Linear Regression with CRISP-DM
echo  Streamlit Application Launcher
echo ===================================
echo.

echo Checking if Streamlit is installed...
pip show streamlit >nul 2>&1
if %errorlevel% neq 0 (
    echo Streamlit is not installed. Installing dependencies...
    pip install -r requirements.txt
    echo.
) else (
    echo Streamlit is already installed.
    echo.
)

echo Starting Streamlit application...
echo The app will open in your default browser.
echo Press Ctrl+C to stop the server.
echo.

streamlit run app.py

pause
