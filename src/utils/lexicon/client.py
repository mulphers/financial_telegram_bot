START_COMMAND_MESSAGE = '''
👋 Приветствую!

💸 Данный бот предназначен для контроля финансов. Он обеспечивает удобный и простой способ 
отслеживания расходов.

📑 Чтобы посмотреть список доступных команд введи - /help
'''

HELP_COMMAND_MESSAGE = '''
📑 Список доступных команд:

1. /profile - просмотреть информацию о пользователе
2. /action - просмотреть список доступных действий
'''

PROFILE_COMMAND_MESSAGE = '''
💾 Информация о Вашем аккаунте:

1. Ваш идентификатор: {}
2. Дата присоединения: {}
'''

ACTION_COMMAND_MESSAGE = '💾 Выберите действие'

ACTION_ON_FINANCES_MESSAGE = '💸 Действия над финансами'

VIEW_EXPENSES_MESSAGE = '📊 Просмотреть расходы'

FINANCIAL_ACTIONS_MESSAGE = '📑 Список доступных действий над финансами'

ADD_EXPENSE_MESSAGE = '➕ Добавить расход'

REMOVE_EXPENSE_MESSAGE = '➖ Удалить расход'

SELECT_PERIOD_MESSAGE = '🕜 Выберите период'

DAY_PERIOD_MESSAGE = '📗 За день'

MONTH_PERIOD_MESSAGE = '📘 За месяц'

YEAR_PERIOD_MESSAGE = '📙 За год'

WRITE_AMOUNT_EXPENSE_MESSAGE = '🔹 Введите сумму которую вы потратили'

WARNING_AMOUNT_EXPENSE_MESSAGE = '❗️ Ошибка! Введите корректное число.' \
                                 ' Если вы вводите дробное число - используйте символ "."'

WRITE_SHORT_DESCRIPTION_MESSAGE = '🔹 Введите краткое описание'

WARNING_SHORT_DESCRIPTION_MESSAGE = '❗️ Ошибка! В качестве описания разрешается использовать только текст'

EXPENSE_SAVED_MESSAGE = '✅ Расход успешно сохранен'

EXPENSE_PERIOD_MESSAGE = '💵 За текущий {} вы потратили: {} рубля(-ей)'

SELECT_DELETE_EXPENSE_MESSAGE = '❌ Выберите расход который хотите удалить. Допускается удаление только тех расходов,' \
                                ' который были созданы в текущий день'

EXPENSE_DELETE_MESSAGE = '✅ Расход успешно удалён'

EXPENSE_DELETE_WARNING_MESSAGE = '❗️ Ошибка! Данный расход уже был удален либо никогда не существовал'
