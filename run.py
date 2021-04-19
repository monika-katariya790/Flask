from flaskblog import create_app
from flask_cors import CORS

app= create_app()

if __name__ == '__main__':
    # initialize_app(app)
    CORS(app,resources={r'/*':{'origins': '*'}})
    app.run(debug=True)