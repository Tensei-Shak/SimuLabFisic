from flask import Blueprint, render_template

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def login():
    return render_template('login.html')

@auth_bp.route('/signup')
def signup():
    return "Formulario de registro"
