# keyboards.py
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Основное меню
def get_main_menu():
    keyboard = [
        [KeyboardButton("🌌 Астрология"), KeyboardButton("⚡ Быстрые прогнозы")],
        [KeyboardButton("ℹ️ О боте"), KeyboardButton("📚 Помощь")],
        [KeyboardButton("🎯 Примеры запросов")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)

# Меню планет
def get_planets_keyboard():
    planets = [
        ["🌞 Солнце", "🌙 Луна", "☿ Меркурий"],
        ["♀ Венера", "♂ Марс", "♃ Юпитер"],
        ["♄ Сатурн", "♅ Уран", "♆ Нептун"],
        ["♇ Плутон", "⛎ Северный узел", "🧿 Южный узел"],
        ["🌑 Лилит", "✨ Селена"],
        ["🔙 Назад в меню"]
    ]
    return ReplyKeyboardMarkup(planets, resize_keyboard=True)

# Меню знаков зодиака
def get_zodiac_keyboard():
    zodiacs = [
        ["♈ Овен", "♉ Телец", "♊ Близнецы"],
        ["♋ Рак", "♌ Лев", "♍ Дева"],
        ["♎ Весы", "♏ Скорпион", "♐ Стрелец"],
        ["♑ Козерог", "♒ Водолей", "♓ Рыбы"],
        ["🔙 Назад к планетам"]
    ]
    return ReplyKeyboardMarkup(zodiacs, resize_keyboard=True)

# Клавиатура для выбора типа информации (Венера)
def get_venus_info_types_keyboard():
    keyboard = [
        [KeyboardButton("💖 Удовольствие")],
        [KeyboardButton("💄 Стратегия привлекательности")],
        [KeyboardButton("👩 Привлекательные женщины")],
        [KeyboardButton("💌 Язык любви")],
        [KeyboardButton("🔙 Назад к знакам")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# Клавиатура для выбора типа информации (Марс)
def get_mars_info_types_keyboard():
    keyboard = [
        [KeyboardButton("⚡ Эффективность")],
        [KeyboardButton("💪 Привлекательный мужчина")],
        [KeyboardButton("🎯 Мужская стратегия")],
        [KeyboardButton("🔙 Назад к знакам")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# Быстрый выбор для популярных запросов
def get_quick_astro_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Юпитер в Деве", callback_data="quick_jupiter_virgo"),
            InlineKeyboardButton("Солнце во Льве", callback_data="quick_sun_leo")
        ],
        [
            InlineKeyboardButton("Венера в Овне (удовольствие)", callback_data="quick_venus_aries_pleasure"),
            InlineKeyboardButton("Марс в Тельце (эффективность)", callback_data="quick_mars_taurus_efficiency")
        ],
        [
            InlineKeyboardButton("Луна в Раке", callback_data="quick_moon_cancer"),
            InlineKeyboardButton("Сатурн в Козероге", callback_data="quick_saturn_capricorn")
        ],
        [
            InlineKeyboardButton("Северный узел в Стрельце", callback_data="quick_north_node_sagittarius"),
            InlineKeyboardButton("Лилит в Скорпионе", callback_data="quick_lilith_scorpio")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

# Клавиатура с примерами запросов
def get_examples_keyboard():
    keyboard = [
        [KeyboardButton("💫 Юпитер в Деве")],
        [KeyboardButton("❤️ Венера в Овне удовольствие")],
        [KeyboardButton("⚡ Марс в Тельце эффективность")],
        [KeyboardButton("🌞 Солнце во Льве")],
        [KeyboardButton("🌙 Луна в Раке")],
        [KeyboardButton("🔙 Назад в меню")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# Быстрое меню после получения результата
def get_after_result_keyboard():
    keyboard = [
        [KeyboardButton("🔄 Новый запрос"), KeyboardButton("📋 Другие варианты")],
        [KeyboardButton("📊 Похожие прогнозы"), KeyboardButton("🔙 В главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# Клавиатура "Назад"
def get_back_keyboard():
    back_button = [[KeyboardButton("🔙 Назад")]]
    return ReplyKeyboardMarkup(back_button, resize_keyboard=True)

# Клавиатура только с кнопкой "В главное меню"
def get_home_keyboard():
    home_button = [[KeyboardButton("🏠 В главное меню")]]
    return ReplyKeyboardMarkup(home_button, resize_keyboard=True)

# Кнопка "Назад" для текущего контекста
def get_context_back_keyboard(context_type="знакам"):
    """Возвращает клавиатуру "Назад" с указанием контекста"""
    back_button = [[KeyboardButton(f"🔙 Назад к {context_type}")]]
    return ReplyKeyboardMarkup(back_button, resize_keyboard=True)

# Инлайн клавиатура для быстрого перехода
def get_inline_examples():
    keyboard = [
        [
            InlineKeyboardButton("Юпитер", callback_data="example_jupiter"),
            InlineKeyboardButton("Венера", callback_data="example_venus"),
            InlineKeyboardButton("Марс", callback_data="example_mars")
        ],
        [
            InlineKeyboardButton("Солнце", callback_data="example_sun"),
            InlineKeyboardButton("Луна", callback_data="example_moon"),
            InlineKeyboardButton("Сатурн", callback_data="example_saturn")
        ],
        [
            InlineKeyboardButton("Скрыть", callback_data="hide_examples")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

# Клавиатура для администратора
def get_admin_keyboard():
    keyboard = [
        [KeyboardButton("📊 Статистика"), KeyboardButton("👥 Пользователи")],
        [KeyboardButton("📢 Рассылка"), KeyboardButton("⚙️ Настройки")],
        [KeyboardButton("🏠 В главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# Универсальная функция для получения клавиатуры типа информации
def get_info_type_keyboard(planet_name):
    """
    Возвращает клавиатуру с типами информации для указанной планеты
    
    Args:
        planet_name (str): Название планеты (venus, mars и т.д.)
    
    Returns:
        ReplyKeyboardMarkup: Клавиатура с типами информации
    """
    planet_name = planet_name.lower()
    
    if planet_name == "венера":
        return get_venus_info_types_keyboard()
    elif planet_name == "марс":
        return get_mars_info_types_keyboard()
    else:
        # Для планет без типов информации - возвращаем обычную клавиатуру
        return get_back_keyboard()

# Функция для преобразования типа информации в кнопку
def info_type_to_button(info_type):
    """
    Преобразует внутреннее название типа информации в читаемый текст для кнопки
    
    Args:
        info_type (str): Внутреннее название типа (удовольствие, стратегия_привлекательности и т.д.)
    
    Returns:
        str: Текст для кнопки
    """
    type_map = {
        "удовольствие": "💖 Удовольствие",
        "стратегия_привлекательности": "💄 Стратегия привлекательности",
        "привлекательные_женщины": "👩 Привлекательные женщины",
        "язык_любви": "💌 Язык любви",
        "эффективность": "⚡ Эффективность",
        "привлекательный_мужчина": "💪 Привлекательный мужчина",
        "мужская_стратегия": "🎯 Мужская стратегия"
    }
    return type_map.get(info_type, info_type.replace('_', ' ').title())

# Функция для преобразования текста кнопки в внутреннее название типа
def button_to_info_type(button_text):
    """
    Преобразует текст кнопки во внутреннее название типа информации
    
    Args:
        button_text (str): Текст кнопки
    
    Returns:
        str: Внутреннее название типа
    """
    type_map = {
        "💖 удовольствие": "удовольствие",
        "💄 стратегия привлекательности": "стратегия_привлекательности",
        "👩 привлекательные женщины": "привлекательные_женщины",
        "💌 язык любви": "язык_любви",
        "⚡ эффективность": "эффективность",
        "💪 привлекательный мужчина": "привлекательный_мужчина",
        "🎯 мужская стратегия": "мужская_стратегия"
    }
    
    # Удаляем эмодзи и лишние пробелы
    clean_text = ' '.join(button_text.split()[1:]).lower() if ' ' in button_text else button_text.lower()
    return type_map.get(clean_text, clean_text.replace(' ', '_'))

# Клавиатура для подтверждения действий
def get_confirmation_keyboard():
    keyboard = [
        [KeyboardButton("✅ Да"), KeyboardButton("❌ Нет")],
        [KeyboardButton("🔙 Отмена")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# Клавиатура для оценки прогноза
def get_rating_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("⭐", callback_data="rate_1"),
            InlineKeyboardButton("⭐⭐", callback_data="rate_2"),
            InlineKeyboardButton("⭐⭐⭐", callback_data="rate_3"),
            InlineKeyboardButton("⭐⭐⭐⭐", callback_data="rate_4"),
            InlineKeyboardButton("⭐⭐⭐⭐⭐", callback_data="rate_5")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)