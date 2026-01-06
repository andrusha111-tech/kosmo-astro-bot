#!/bin/bash

echo "========================================"
echo "   Запуск Kosmo Astro Bot"
echo "========================================"

# Проверяем наличие виртуального окружения
if [ ! -d "venv" ]; then
    echo "Создание виртуального окружения..."
    python3 -m venv venv
fi

# Активируем окружение
source venv/bin/activate

# Проверяем зависимости
if [ ! -f "requirements.txt" ]; then
    echo "Файл requirements.txt не найден!"
    exit 1
fi

echo "Проверка зависимостей..."
pip install -r requirements.txt

echo "Запуск бота..."
python bot.py