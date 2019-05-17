from flask import (
    Flask,
    render_template,
   Blueprint, Response, request
)

app = Flask(__name__, template_folder="templates")

@app.route('/hello')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return "Hello world"


if __name__ == '__main__':
    app.run(debug=True)