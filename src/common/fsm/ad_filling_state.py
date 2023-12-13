from aiogram.fsm.state import State, StatesGroup


class FSMAdFillForm(StatesGroup):
    fill_ad_text = State()
    upload_photo = State()
    fill_button_text = State()
    fill_url = State()
