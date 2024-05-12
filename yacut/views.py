from flask import redirect, render_template, url_for

from constants import ENDPOINT_SHORT_LINK, NAME_OCCUPIED_MESSAGE
from . import app, db
from .forms import UrlMapForm
from .models import URLMap
from .utils import get_unique_short_id


@app.route("/", methods=["GET", "POST"])
def index_view():
    """
    Главная страница. Выводит пользователю форму для генерации короткой ссылки.
    """
    form = UrlMapForm()
    if not form.validate_on_submit():
        return render_template("index.html", form=form)
    custom_id = form.custom_id.data
    if not custom_id:
        custom_id = get_unique_short_id()
    elif URLMap.query.filter_by(short=custom_id).first():
        form.custom_id.errors = [NAME_OCCUPIED_MESSAGE]
        return render_template("index.html", form=form)
    url_map = URLMap(original=form.original_link.data, short=custom_id)
    db.session.add(url_map)
    db.session.commit()
    short_url = url_for(ENDPOINT_SHORT_LINK, short=custom_id, _external=True)
    context = {"form": form, "short_url": short_url}
    return render_template("index.html", **context)


@app.route("/<string:short>", methods=["GET"])
def redirect_view(short):
    """
    Позволяет исполнить переадресацию на исходный адрес
    при обращении к короткой ссылке.
    """
    return redirect(
        URLMap.query.filter_by(short=short).first_or_404().original
    )
