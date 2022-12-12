from app_config import app
from model import db
from flask_cors import CORS

if __name__ == '__main__':
    CORS(app)
    db.init_app(app)
    app.run(host='0.0.0.0', debug=True, port=5000)
