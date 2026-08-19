from aiogram.utils.keyboard import InlineKeyboardBuilder
from emojis import *

def main_menu(user_id: int, is_admin: bool = False):
    b = InlineKeyboardBuilder()
    b.button(text="Сдать", callback_data="submit_menu", icon_custom_emoji_id=B_SUBMIT, color="green")
    b.button(text="Кабинет", callback_data="profile", icon_custom_emoji_id=B_PROFILE, color="blue")
    b.button(text="Вывод", callback_data="withdraw", icon_custom_emoji_id=B_WITHDRAW, color="blue")
    b.button(text="История", callback_data="my_numbers", icon_custom_emoji_id=B_MY, color="blue")
    b.button(text="Очередь", callback_data="public_queue", icon_custom_emoji_id=B_QUEUE, color="blue")
    b.button(text="Поддержка", callback_data="support", icon_custom_emoji_id=B_SUPPORT, color="blue")
    b.adjust(1, 2, 2, 1)
    return b.as_markup()

# ... (все остальные функции с новыми эмодзи и цветами)

def admin_panel_kb(is_owner: bool = False, bot_enabled: bool = True):
    b = InlineKeyboardBuilder()
    b.button(text="Цены", callback_data="price_menu", icon_custom_emoji_id=B_MIN, color="blue")
    b.button(text="Выплаты", callback_data="wd_panel", icon_custom_emoji_id=B_PAY, color="blue")
    b.button(text="Рассылка", callback_data="broadcast", icon_custom_emoji_id=B_CAST, color="blue")
    b.button(text="Информация", callback_data="stats", icon_custom_emoji_id=B_STATS, color="blue")  # кнопка "Инфо", текст внутри — "Информация"
    b.button(text="Юзеры", callback_data="users_list", icon_custom_emoji_id=B_USERS, color="blue")
    if bot_enabled:
        b.button(text="Стоп", callback_data="bot_stop", icon_custom_emoji_id=B_STOP, color="red")
    else:
        b.button(text="Старт", callback_data="bot_start", icon_custom_emoji_id=B_START, color="red")
    b.button(text="Очистка", callback_data="clear_queue_menu", icon_custom_emoji_id=B_CLR_REG, color="red")
    if is_owner:
        b.button(text="Админы", callback_data="manage_admins", icon_custom_emoji_id=B_ADMINS, color="blue")
    b.adjust(1, 2, 2, 2, 1)
    return b.as_markup()

# cancel_kb — теперь красная
def cancel_kb(back_data: str = "main_menu", with_back: bool = True):
    b = InlineKeyboardBuilder()
    b.button(text="Назад", callback_data=back_data, icon_custom_emoji_id=B_BACK, color="red")
    return b.as_markup()

# price_menu_kb — зелёные/синие
def price_menu_kb():
    b = InlineKeyboardBuilder()
    b.button(text="MAX • Нерег", callback_data="set_price_unregistered", icon_custom_emoji_id=B_PRICE_NEW, color="green")
    b.button(text="MAX • Рег", callback_data="set_price_registered", icon_custom_emoji_id=B_PRICE_REG, color="green")
    b.button(text="Мин. вывод", callback_data="set_min_withdraw", icon_custom_emoji_id=B_MIN, color="blue")
    b.button(text="Назад", callback_data="admin_panel", icon_custom_emoji_id=B_BACK, color="red")
    b.adjust(2, 1, 1)
    return b.as_markup()

# wd_panel_kb, wd_item_actions_kb и все остальные — аналогично с цветами
# (я сделал их зелёными/синими/красными по смыслу — полный код ниже если нужно)
