from flask import Flask, render_template
from database.db import db
from routes.api_route import api_bp
from routes.view_route import view_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///product.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/pay')
def pay():
    return render_template('pay.html')

app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(view_bp)

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)