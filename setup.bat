@echo off

python --version 3>NUL

if errorlevel 1 (
    echo Python is not installed.
    echo Press any key to exit.
    pause >nul
    exit
)

echo Installing dependencies...
pip install -r requirements.txt

if not exist .env (
    echo Copying .env file.
    copy .env.example .env
    echo Please set the token and save the file to run Scarecrow.
    notepad .env
)

echo Scarecrow is running!
python main.py

pause >nul