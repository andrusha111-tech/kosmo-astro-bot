@echo off
echo ========================================
echo    Запуск Kosmo Astro Bot
echo ========================================

REM Проверяем наличие виртуального окружения
if not exist "venv\Scripts\activate.bat" (
    echo Создание виртуального окружения...
    python -m venv venv
)

REM Активируем окружение
call venv\Scripts\activate.bat

REM Проверяем зависимости
if not exist "requirements.txt" (
    echo Файл requirements.txt не найден!
    pause
    exit /b 1
)

echo Проверка зависимостей...
pip install -r requirements.txt

echo Запуск бота...
python bot.py

pause