from flask import Blueprint, render_template , request, redirect, url_for

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/', methods=['GET', 'POST'])
def contactHome():
    if request.method == 'POST':
        email = request.form['email']
        message = request.form['message']
        print(email, message)
        return redirect(url_for('contact.thank_you'))
    else:
        return render_template('views/ContactView.html')
    
@contact_bp.route('/thank_you')
def thank_you():
    return "<h1>Gracias por contactarnos. Nos pondremos en contacto contigo pronto.</h1>"
