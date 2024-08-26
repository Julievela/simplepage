from flask import Flask, render_template, url_for

servidor = Flask(__name__)

@servidor.route('/inicio')
def home():
    return render_template('plantilla.html')

if __name__ == '__main__':
    servidor.run(debug=True)