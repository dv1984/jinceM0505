import app
flask_app = app.create_app("development")
if __name__ == '__main__':
    flask_app.run(host="0.0.0.0",port=80,debug=True)