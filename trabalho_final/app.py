
from flask import Flask
from routes import inventario_routes

app = Flask(__name__)
app.register_blueprint(inventario_routes)

if __name__ == "__main__":
    app.run(debug=True)
