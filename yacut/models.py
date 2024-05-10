from datetime import datetime as dt

from flask import url_for

from constants import (ENDPOINT_SHORT_LINK, MAX_LEN_ORIGINAL_LINK,
                       MAX_LEN_SHORT_LINK)
from yacut import db


class URLMap(db.Model):
    """
    Модель ссылок. Содержит оригинальный URL, его короткий
    сгенерированный идентификатор и время генерации.
    """
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(MAX_LEN_ORIGINAL_LINK), nullable=False)
    short = db.Column(db.String(MAX_LEN_SHORT_LINK), unique=True,
                      nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=dt.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for(
                ENDPOINT_SHORT_LINK,
                short=self.short,
                _external=True
            )
        )

    def from_dict(self, data):
        setattr(self, "original", data["url"])
        setattr(self, "short", data["custom_id"])
