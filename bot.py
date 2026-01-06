# bot.py
import logging
from telegram import Update
from telegram.ext import (
    Application, 
    CommandHandler, 
    MessageHandler, 
    CallbackQueryHandler,
    ConversationHandler,
    filters,
    ContextTypes
)

from config import BOT_TOKEN, BOT_NAME
from keyboards import (
    get_main_menu, 
    get_planets_keyboard, 
    get_zodiac_keyboard,
    get_venus_info_types_keyboard,
    get_mars_info_types_keyboard,
    get_quick_astro_keyboard,
    get_examples_keyboard,
    get_home_keyboard,
    button_to_info_type
)
from data import get_astro_text

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Состояния для ConversationHandler
CHOOSING_PLANET, CHOOSING_ZODIAC, CHOOSING_INFO_TYPE = range(3)

# ========== КОМАНДЫ И ОБРАБОТЧИКИ ==========
# Команда /start
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    user = update.effective_user
    welcome_text = f"""🌟 Добро пожаловать, {user.first_name}!
    
Я - {BOT_NAME}, ваш астрологический помощник.
    
Я помогу вам узнать:
• Удачу по Юпитеру
• Идеального партнера по Солнцу
• Кармические задачи по узлам
• И многое другое!
    
Выберите действие в меню ниже 👇"""
    
    await update.message.reply_text(
        welcome_text,
        reply_markup=get_main_menu()
    )

# Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /help"""
    help_text = """📚 *Помощь по использованию бота*
    
*Доступные команды:*
/start - Запустить бота
/help - Эта справка
/astrology - Перейти к астрологии
/quick - Быстрые прогнозы
    
*Как использовать:*
1. Нажмите "🌌 Астрология"
2. Выберите планету
3. Выберите знак зодиака
4. Для Венеры и Марса выберите тип информации
5. Получите информацию!
    
*Примеры запросов:*
• "Юпитер в Деве"
• "Венера в Овне удовольствие"
• "Марс в Тельце эффективность"
• "Солнце во Льве"
    
Также можно писать запросы текстом!"""
    
    await update.message.reply_text(
        help_text,
        parse_mode='Markdown'
    )

# Быстрые прогнозы
async def quick_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Быстрые популярные прогнозы"""
    text = "✨ *Популярные астрологические положения:*"
    await update.message.reply_text(
        text,
        parse_mode='Markdown',
        reply_markup=get_quick_astro_keyboard()
    )

# Примеры запросов
async def examples_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Примеры запросов"""
    text = "📝 *Примеры запросов:*\n\nВыберите пример ниже или напишите свой запрос в формате:\n\"Планета в Знаке\""
    await update.message.reply_text(
        text,
        parse_mode='Markdown',
        reply_markup=get_examples_keyboard()
    )

# О боте
async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Информация о боте"""
    about_text = f"""{BOT_NAME}
    
Астрологический бот на основе классической астрологии.
    
Функции:
• Анализ планет в знаках
• Кармические задачи
• Совместимость
• Личностный рост
    
Данные:
• Юпитер: Удача в знаках
• Солнце: Идеальный партнер
• Венера: 4 типа информации
• Марс: 3 типа информации
• Луна: Образ жены
• Узлы: Кармические задачи
    
Версия: 1.0
Разработчик: Kosmo Team"""
    await update.message.reply_text(about_text)

# Начало астрологического диалога
async def astrology_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Начинаем процесс выбора астрологической информации"""
    await update.message.reply_text(
        "🌠 Выберите планету:",
        reply_markup=get_planets_keyboard()
    )
    return CHOOSING_PLANET

# Выбор планеты
async def choose_planet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Пользователь выбрал планету"""
    text = update.message.text.lower()
    
    # Определяем планету по тексту
    planet_map = {
        "🌞 солнце": "солнце",
        "🌙 луна": "луна",
        "☿ меркурий": "меркурий",
        "♀ венера": "венера",
        "♂ марс": "марс",
        "♃ юпитер": "юпитер",
        "♄ сатурн": "сатурн",
        "♅ уран": "уран",
        "♆ нептун": "нептун",
        "♇ плутон": "плутон",
        "⛎ северный узел": "северный узел",
        "🧿 южный узел": "южный узел",
        "🌑 лилит": "лилит",
        "✨ селена": "селена"
    }
    
    # Проверяем кнопку "Назад"
    if "назад в меню" in text or "🔙 назад в меню" in text:
        await update.message.reply_text(
            "🏠 Возвращаемся в главное меню",
            reply_markup=get_main_menu()
        )
        return ConversationHandler.END
    
    planet_name = planet_map.get(text, text)
    
    # Сохраняем выбор планеты
    context.user_data['planet'] = planet_name
    
    await update.message.reply_text(
        f"🪐 Выбрана планета: {planet_name.upper()}\n\nТеперь выберите знак зодиака:",
        reply_markup=get_zodiac_keyboard()
    )
    return CHOOSING_ZODIAC

# Выбор знака зодиака
async def choose_zodiac(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Пользователь выбрал знак зодиака"""
    text = update.message.text.lower()
    
    # Определяем знак по тексту
    zodiac_map = {
        "♈ овен": "овен",
        "♉ телец": "телец",
        "♊ близнецы": "близнецы",
        "♋ рак": "рак",
        "♌ лев": "лев",
        "♍ дева": "дева",
        "♎ весы": "весы",
        "♏ скорпион": "скорпион",
        "♐ стрелец": "стрелец",
        "♑ козерог": "козерог",
        "♒ водолей": "водолей",
        "♓ рыбы": "рыбы"
    }
    
    # Проверяем кнопку "Назад"
    if "назад к планетам" in text or "🔙 назад к планетам" in text:
        await update.message.reply_text(
            "🪐 Возвращаемся к выбору планеты",
            reply_markup=get_planets_keyboard()
        )
        return CHOOSING_PLANET
    
    zodiac_name = zodiac_map.get(text, text)
    
    # Сохраняем выбор знака
    context.user_data['zodiac'] = zodiac_name
    
    planet = context.user_data.get('planet', '')
    
    # Проверяем, нужно ли выбирать тип информации
    if planet.lower() in ["венера", "марс"]:
        if planet.lower() == "венера":
            await update.message.reply_text(
                f"💖 ВЕНЕРА в {zodiac_name.upper()}\n\nВыберите тип информации:",
                reply_markup=get_venus_info_types_keyboard()
            )
        elif planet.lower() == "марс":
            await update.message.reply_text(
                f"♂ МАРС в {zodiac_name.upper()}\n\nВыберите тип информации:",
                reply_markup=get_mars_info_types_keyboard()
            )
        return CHOOSING_INFO_TYPE
    
    # Для других планет - сразу получаем результат
    result = get_astro_text(planet, zodiac_name)
    
    # Отправляем результат
    await send_result(update, context, result)
    
    return ConversationHandler.END

# Выбор типа информации
async def choose_info_type(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Пользователь выбрал тип информации для Венеры/Марса"""
    text = update.message.text.lower()
    
    # Проверяем кнопку "Назад"
    if "назад к знакам" in text or "🔙 назад к знакам" in text:
        await update.message.reply_text(
            "♎ Возвращаемся к выбору знака зодиака",
            reply_markup=get_zodiac_keyboard()
        )
        return CHOOSING_ZODIAC
    
    # Получаем тип информации из текста кнопки
    info_type = button_to_info_type(text)
    
    # Получаем данные
    planet = context.user_data.get('planet', '')
    zodiac = context.user_data.get('zodiac', '')
    
    result = get_astro_text(planet, zodiac, info_type)
    
    # Отправляем результат
    await send_result(update, context, result)
    
    return ConversationHandler.END

# Функция для отправки результата
async def send_result(update: Update, context: ContextTypes.DEFAULT_TYPE, result):
    """Отправка результата пользователю"""
    # Отправляем результат
    await update.message.reply_text(result)
    
    # Предлагаем дальнейшие действия
    await update.message.reply_text(
        "🔮 Что дальше?\n\n"
        "• Нажмите /start для главного меню\n"
        "• Нажмите /quick для быстрых прогнозов\n"
        "• Напишите новый запрос в формате:\n\"Планета в Знаке\"",
        reply_markup=get_home_keyboard()
    )

# Обработка текстовых сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка текстовых сообщений"""
    text = update.message.text
    
    # Проверяем специальные кнопки
    if text == "🏠 В главное меню":
        await start_command(update, context)
        return
    
    if text == "🎯 Примеры запросов":
        await examples_command(update, context)
        return
    
    if text == "⚡ Быстрые прогнозы":
        await quick_command(update, context)
        return
    
    if text == "ℹ️ О боте":
        await about_command(update, context)
        return
    
    if text == "📚 Помощь":
        await help_command(update, context)
        return
    
    # Преобразуем текст в нижний регистр для анализа
    text_lower = text.lower()
    
    if text_lower in ["привет", "hello", "hi", "здравствуй"]:
        await update.message.reply_text(f"👋 Привет! Напишите астрологический запрос или используйте меню!")
    
    elif "юпитер" in text_lower and "дева" in text_lower:
        result = get_astro_text("юпитер", "дева")
        await send_result(update, context, result)
    
    elif "солнце" in text_lower and "лев" in text_lower:
        result = get_astro_text("солнце", "лев")
        await send_result(update, context, result)
    
    elif "венера" in text_lower and "овен" in text_lower and "удовольствие" in text_lower:
        result = get_astro_text("венера", "овен", "удовольствие")
        await send_result(update, context, result)
    
    elif "марс" in text_lower and "телец" in text_lower and "эффективность" in text_lower:
        result = get_astro_text("марс", "телец", "эффективность")
        await send_result(update, context, result)
    
    elif "луна" in text_lower and "рак" in text_lower:
        result = get_astro_text("луна", "рак")
        await send_result(update, context, result)
    
    else:
        # Пытаемся распознать запрос типа "Планета в Знаке"
        if " в " in text_lower:
            parts = text_lower.split(" в ")
            if len(parts) == 2:
                planet, rest = parts[0].strip(), parts[1].strip()
                
                # Проверяем, есть ли тип информации
                if " " in rest:
                    zodiac_parts = rest.split()
                    zodiac = zodiac_parts[0]
                    info_type = "_".join(zodiac_parts[1:]) if len(zodiac_parts) > 1 else None
                    
                    if info_type:
                        result = get_astro_text(planet, zodiac, info_type)
                    else:
                        result = get_astro_text(planet, zodiac)
                else:
                    result = get_astro_text(planet, rest)
                
                await send_result(update, context, result)
                return
        
        # Если не распознали
        await update.message.reply_text(
            "🤔 Я не понял ваш запрос. Используйте меню или напишите запрос в формате:\n"
            "\"Планета в Знаке\"\n\n"
            "Например:\n"
            "• Юпитер в Деве\n"
            "• Венера в Овне удовольствие\n"
            "• Марс в Тельце эффективность",
            reply_markup=get_main_menu()
        )

# Обработка inline кнопок
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка нажатия inline кнопок"""
    query = update.callback_query
    await query.answer()
    
    # Обработка быстрых прогнозов
    if query.data == "quick_jupiter_virgo":
        result = get_astro_text("юпитер", "дева")
        await query.edit_message_text(result)
    
    elif query.data == "quick_sun_leo":
        result = get_astro_text("солнце", "лев")
        await query.edit_message_text(result)
    
    elif query.data == "quick_venus_aries_pleasure":
        result = get_astro_text("венера", "овен", "удовольствие")
        await query.edit_message_text(result)
    
    elif query.data == "quick_mars_taurus_efficiency":
        result = get_astro_text("марс", "телец", "эффективность")
        await query.edit_message_text(result)
    
    elif query.data == "quick_moon_cancer":
        result = get_astro_text("луна", "рак")
        await query.edit_message_text(result)
    
    elif query.data == "quick_saturn_capricorn":
        result = get_astro_text("сатурн", "козерог")
        await query.edit_message_text(result)
    
    elif query.data == "quick_north_node_sagittarius":
        result = get_astro_text("северный узел", "стрелец")
        await query.edit_message_text(result)
    
    elif query.data == "quick_lilith_scorpio":
        result = get_astro_text("лилит", "скорпион")
        await query.edit_message_text(result)
    
    else:
        await query.edit_message_text("Этот вариант пока не реализован.")

# Отмена диалога
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отмена текущего диалога"""
    await update.message.reply_text(
        "Диалог отменен.",
        reply_markup=get_main_menu()
    )
    return ConversationHandler.END

# ========== ОСНОВНАЯ ФУНКЦИЯ ==========
def main():
    """Запуск бота"""
    logger.info(f"Запуск бота {BOT_NAME}...")
    
    # Создаем приложение
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Настройка ConversationHandler для астрологии
    conv_handler = ConversationHandler(
        entry_points=[
            MessageHandler(filters.Regex("^(🌌 Астрология)$"), astrology_start),
            CommandHandler("astrology", astrology_start)
        ],
        states={
            CHOOSING_PLANET: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, choose_planet)
            ],
            CHOOSING_ZODIAC: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, choose_zodiac)
            ],
            CHOOSING_INFO_TYPE: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, choose_info_type)
            ]
        },
        fallbacks=[CommandHandler("cancel", cancel)],
        allow_reentry=True
    )
    
    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("quick", quick_command))
    application.add_handler(conv_handler)
    application.add_handler(CallbackQueryHandler(button_callback))
    
    # Обработчик текстовых сообщений должен быть последним
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Запускаем бота
    logger.info(f"Бот {BOT_NAME} запущен и ожидает сообщений...")
    print(f"Бот {BOT_NAME} запущен и ожидает сообщений...")
    
    try:
        application.run_polling(allowed_updates=Update.ALL_TYPES)
    except KeyboardInterrupt:
        logger.info("Бот остановлен пользователем")
        print("\nБот остановлен. До свидания!")

if __name__ == "__main__":
    main()