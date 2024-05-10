MAX_LEN_ORIGINAL_LINK = 256
MAX_LEN_SHORT_LINK = 64
MIN_LINE_LEN_VALID = 1
MAX_USER_LEN_SHORT_LINK = 16
SYMBOLS_GEN_IDENTIFIER = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
    "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d",
    "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
    "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7",
    "8", "9"
]
COUNT_SYMBOL_GEN = 6
ENDPOINT_SHORT_LINK = "redirect_view"
NOT_FOUND_MESSAGE = "Указанный id не найден"
EMPTY_REQUEST = "Отсутствует тело запроса"
NOT_URL_IN_REQUEST = '\"url\" является обязательным полем!'
NAME_OCCUPIED_MESSAGE = "Предложенный вариант короткой ссылки уже существует."
CHECK_PATTERN_SHORT_URL = r"^[A-Za-z0-9_]{1,16}$"
INVALID_URL_NAME_MESSAGE = "Указано недопустимое имя для короткой ссылки"
