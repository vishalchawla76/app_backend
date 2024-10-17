from flask import Blueprint, request, jsonify

main = Blueprint('main', __name__)


# Dummy data for user authentication (typically, you'd use a database)
users = {
    "testuser": {"password": "password123"}
}


@main.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password required'}), 400

    user = users.get(username)

    if user and user['password'] == password:
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401


@main.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'Healthy'}), 200



@main.route("/123")
def check_status():
    return jsonify({"status": "verified"})

@main.route('/', methods=['GET'])
def hello():
    return "hello"

