import asyncio

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config

# Функция конфигурирования и запуска бота
async def main() -> None:

    # Загружаем конфиг в переменнуб config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot: Bot = Bot(token=config.tg_bot.token)
    dp: Dispatcher = Dispatcher()

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__name__':
    asyncio.run(main())

# Выводим значения полей экземпляра класса Config на печать,
# чтобы убедиться, что все данные, получаемые из переменных окружения, доступны
"""print('BOT_TOKEN: ', config.tg_bot.token)
print('ADMINS_IDS: ', config.tg_bot.admins_id)
print()
print('DATABSE: ', config.db.database)
print('DB_HOST: ', config.db.db_host)
print('DB_USER: ', config.db.db_user)
print('DB_PASSWORD: ', config.db.db_password)
"""