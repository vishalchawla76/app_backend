from app import app1

# from app import create_app

# app = create_app()

if __name__ == '__main__':
    app1.run(host='0.0.0.0', debug=True, port=8000)
