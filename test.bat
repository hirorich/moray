echo off

rem �f�B���N�g���ړ�
cd %~dp0

rem ���s
call .venv\Scripts\activate.bat
python test.py

pause
