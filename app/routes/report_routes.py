from flask import Blueprint, render_template, request, jsonify

report_bp = Blueprint('report_bp', __name__)

@report_bp.route('/', methods=['GET', 'POST'])
def contactHome():
    contador = None
    if request.method == 'POST':
        number_members = request.form.get('numberMembers')
        if not number_members:
            return "El campo 'Number Members' es obligatorio", 400
        try:
            contador = int(number_members)
            contador = min(max(contador, 1), 6)
        except ValueError:
            return "El valor de 'Number Members' debe ser un número válido", 400

    return render_template('views/ReportView.html', contador=contador)

@report_bp.route('/submit_team/', methods=['POST'])
def submit_team():
    try:
        members = []
        i = 0
        while True:
            name = request.form.get(f'name_member{i}')
            id_license = request.form.get(f'id_license{i}')
            email = request.form.get(f'email_corp{i}')

            if not name or not id_license or not email:
                break

            members.append({
                'name': name,
                'id_license': id_license,
                'email': email
            })
            i += 1

        text_analysis = request.form.get('text_analysis')
        if not text_analysis:
            return "El campo 'Text Analysis' es obligatorio.", 400

        if not members:
            return "No se enviaron datos de miembros.", 400

        return jsonify({
            'message': 'Datos recibidos correctamente.',
            'members': members,
            'text_analysis': text_analysis
        })

    except Exception as e:
        return f"Error procesando los datos: {e}", 500
