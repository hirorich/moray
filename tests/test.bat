echo off
rem ディレクトリ移動
cd %~dp0
cd ..\

rem 実行
call .venv\Scripts\activate.bat
python -m tests
echo %errorlevel%

pause
