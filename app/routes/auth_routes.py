from flask import Blueprint, render_template

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def authHome():
    return 'Page Authme'

@auth_bp.route('/login')
def login():
    return render_template('login.html')

@auth_bp.route('/signup')
def signup():
    return "Formulario de registro"
