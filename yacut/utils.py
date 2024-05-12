from random import choices

from constants import COUNT_SYMBOL_GEN, SYMBOLS_GEN_IDENTIFIER
from .models import URLMap


def get_unique_short_id():
    """Формирует короткую ссылку и проверяет её уникальность."""
    while True:
        gen_symbol_list = choices(SYMBOLS_GEN_IDENTIFIER, k=COUNT_SYMBOL_GEN)
        short_id = "".join(gen_symbol_list)
        if not URLMap.query.filter_by(short=short_id).first():
            return short_id
