echo off

rem ディレクトリ移動
cd %~dp0

rem 実行
call .venv\Scripts\activate.bat
python main.py

pause
