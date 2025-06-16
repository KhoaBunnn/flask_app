from flask import Flask
from database.db import db
from routes.api_route import api_bp
from routes.view_route import view_bp  # Thêm dòng này

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///product.db'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(view_bp)  # Thêm dòng này

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)