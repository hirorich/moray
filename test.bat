echo off

rem �f�B���N�g���ړ�
cd %~dp0

rem ���s
call .venv\Scripts\activate.bat
rem python test.py
python main.py

pause
