from flask import Blueprint, render_template
from markupsafe import escape

from app.data.dao.GuestDAO import GuestDAO
from app.data.database.sqlite3.db import get_db
from app.data.repositories.GuestRepository import GuestRepository

bp = Blueprint("guests", __name__, url_prefix="/hospedes")


@bp.get("/")
def hospedes():
    db = get_db()
    dao = GuestDAO(db)
    repository = GuestRepository(dao)
    guests = [guest.to_dict() for guest in repository.find_many()]
    return render_template("guests.html", rows=guests)


@bp.get("/cadastro/")
def cadastro():
    return render_template("newGuest.html")


@bp.get("/<document>/")
def editar(document):
    url_param = escape(document)
    db = get_db()
    dao = GuestDAO(db)
    repository = GuestRepository(dao)
    guest = repository.findBy("document", str(url_param))
    return render_template("updateGuest.html", guest=guest.to_dict())
