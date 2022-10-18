import json
from flask import (Blueprint, render_template)
bp = Blueprint('pet', __name__, url_prefix='/pets')

pets = json.load(open("pets_json"))
print(pets)


@bp.route('/')
def index():
    return render_template('index.html', pets=pets)
