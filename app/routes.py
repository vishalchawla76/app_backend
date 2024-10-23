from flask import Blueprint, request, jsonify, render_template

from app.logger import logger

# from app.logger import LoggerConfig
main = Blueprint('main', __name__)


# Dummy data for user authentication (typically, you'd use a database)
users = {
    "vishal": {"password": "vishal"}
}

@main.route('/login', methods=['POST'])
def login():
    logger.info("ENTERED IN LOGIN API")
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        logger.error("USERNAME NOT FOUND")
        return jsonify({'error': 'Username and password required'}), 400

    user = users.get(username)

    if user and user['password'] == password:
        logger.info("LOGIN SUCCESS")
        return jsonify({'message': 'Login successful'}), 200
    else:
        logger.error("ERROR")
        return jsonify({'error': 'Invalid credentials'}), 401


@main.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'Healthy'}), 200


@main.route("/123")
def check_status():
    return jsonify({"status": "verified"})

@main.route("/")
def router1():
    return render_template("index.html")





