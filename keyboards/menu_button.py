from aiogram import Dispatcher, types


# Создаём Меню ***в разработке
async def set_main_menu(dp: Dispatcher):
    # Создаем список с командами для кнопки menu
    main_menu_commands = [
        types.BotCommand(command='/start', description='Старт бота'),
        types.BotCommand(command='/help', description='Помощь, Правила игры')
    ]
    await dp.bot.set_my_commands(main_menu_commands)
