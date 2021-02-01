from flask import Flask, render_template

from controllers.clients_controller import clients_blueprint
from controllers.trainers_controller import trainers_blueprint

app = Flask(__name__)

app.register_blueprint(clients_blueprint)
app.register_blueprint(trainers_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)