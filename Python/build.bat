@echo off
cd /d "%~dp0"

if not exist "Python\Crocofile.png" (
  echo ERRO: falta o arquivo Python\Crocofile.png
  pause
  exit /b 1
)
if not exist "Python\crocofile.icon" (
  echo ERRO: falta o arquivo Python\crocofile.ico
  pause
  exit /b 1
)

py -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt

set PLAYWRIGHT_BROWSERS_PATH=0
set PLAYWRIGHT_DOWNLOAD_CONNECTION_TIMEOUT=300000
playwright install chromium
if errorlevel 1 (
  echo.
  echo ERRO: nao foi possivel baixar o Chromium.
  echo Desligue a VPN, confira a internet e rode o build.bat de novo.
  pause
  exit /b 1
)

python -c "import playwright,os;print(os.path.dirname(playwright.__file__))" > pwdir.txt
set /p PWDIR=<pwdir.txt
del pwdir.txt

if not exist "%PWDIR%\driver\package\.local-browsers" (
  echo ERRO: o Chromium nao foi encontrado dentro do Playwright.
  pause
  exit /b 1
)

pyinstaller --noconsole --onedir --collect-all playwright ^
  --icon=Python\crocofile.ico ^
  --add-data "Python\Crocofile.png;." ^
  --add-data "%PWDIR%\driver\package\.local-browsers;playwright\driver\package\.local-browsers" ^
  --name Crocofile Python\interface.py
if errorlevel 1 (
  echo.
  echo ERRO ao gerar o executavel. Veja a mensagem acima.
  pause
  exit /b 1
)

echo.
echo PRONTO: dist\Crocofile\Crocofile.exe
pause


