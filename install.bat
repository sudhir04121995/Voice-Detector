@echo off
echo Installing required packages for AI Voice Detector...
echo ===================================================

call venv\Scripts\activate.bat

pip install fastapi==0.104.1
pip install uvicorn==0.24.0
pip install python-multipart==0.0.6
pip install aiofiles==23.2.1
pip install jinja2==3.1.3
pip install pydantic==2.5.0

echo.
echo ===================================================
echo ✅ All packages installed successfully!
echo.
echo 📋 Next steps:
echo 1. Run: python app.py
echo 2. Open browser to: http://localhost:8000
echo ===================================================
pause