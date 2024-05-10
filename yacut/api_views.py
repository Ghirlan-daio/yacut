from http import HTTPStatus as status
from re import match

from flask import jsonify, request

import constants

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .views import get_unique_short_id


@app.route("/api/id/<string:short_id>/", methods=["GET"])
def get_original_link_api(short_id):
    """
    Позволяет получить оригинальную ссылку по её короткому идентификатору.
    """
    object_referens = URLMap.query.filter_by(short=short_id).first()
    if not object_referens:
        raise InvalidAPIUsage(constants.NOT_FOUND_MESSAGE, status.NOT_FOUND)
    return jsonify({"url": object_referens.original}), status.OK


@app.route("/api/id/", methods=["POST"])
def create_short_link_api():
    """Позволяет сгенерировать короткую ссылку."""
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage(constants.EMPTY_REQUEST)
    if "url" not in data:
        raise InvalidAPIUsage(constants.NOT_URL_IN_REQUEST)
    if not data.get("custom_id"):
        data["custom_id"] = get_unique_short_id()
    elif URLMap.query.filter_by(short=data["custom_id"]).first():
        raise InvalidAPIUsage(constants.NAME_OCCUPIED_MESSAGE)
    elif not match(constants.CHECK_PATTERN_SHORT_URL, data["custom_id"]):
        raise InvalidAPIUsage(constants.INVALID_URL_NAME_MESSAGE)
    url_map = URLMap()
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.to_dict()), status.CREATED
