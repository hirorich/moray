echo off

rem ディレクトリ移動
cd %~dp0

rem 実行
call .venv\Scripts\activate.bat
rem python test.py
python main.py

pause
