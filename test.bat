echo off

call .venv\Scripts\activate.bat
python -m tests
echo %errorlevel%

pause
