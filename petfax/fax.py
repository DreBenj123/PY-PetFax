from flask import (Blueprint, render_template)

bp = Blueprint('fact', _name_, url_prefix="/fax")


@bp.route('/new')
def new():
    return render_template('facts/new.html')
