# config.py
import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Токен бота
BOT_TOKEN = os.getenv('BOT_TOKEN')

# ID администраторов (через запятую)
ADMIN_IDS = []
admin_ids_str = os.getenv('ADMIN_IDS', '')
if admin_ids_str:
    ADMIN_IDS = [int(x.strip()) for x in admin_ids_str.split(',') if x.strip()]

# Настройки бота
BOT_NAME = "Kosmo Astro Bot"
BOT_DESCRIPTION = "Астрологический бот для получения информации о планетах в знаках зодиака"
BOT_VERSION = "1.0.0"

# Настройки логирования
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Проверка токена
if not BOT_TOKEN or BOT_TOKEN == 'ВАШ_ТОКЕН_БОТА':
    raise ValueError("Токен бота не установлен! Укажите BOT_TOKEN в файле .env")

# Функция валидации конфигурации
def validate_config():
    """Проверка конфигурации при запуске"""
    print(f"✅ Конфигурация загружена: {BOT_NAME} v{BOT_VERSION}")
    print(f"📊 Администраторы: {ADMIN_IDS if ADMIN_IDS else 'не установлены'}")
    return True