from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional

from constants import (MAX_LEN_ORIGINAL_LINK, MAX_USER_LEN_SHORT_LINK,
                       MIN_LINE_LEN_VALID)


class UrlMapForm(FlaskForm):
    """
    Форма позволяет пользователям приложения добавлять ссылку,
    которую необходимо укоротить (сгенерировать короткий вариант),
    и предложить свой вариант короткой записи ссылки.
    """
    original_link = URLField(
        "Длинная ссылка",
        validators=[DataRequired(message="Обязательное поле"),
                    Length(MIN_LINE_LEN_VALID, MAX_LEN_ORIGINAL_LINK)]
    )
    custom_id = URLField(
        "Ваш вариант короткой ссылки",
        validators=[Length(MIN_LINE_LEN_VALID, MAX_USER_LEN_SHORT_LINK),
                    Optional()]
    )
    submit = SubmitField("Создать")
