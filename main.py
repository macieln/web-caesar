from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
            <!-- create your form here -->
            <form action="/encrypt" method="post">
                <label for="rotation">Rotate By:</label>
                <input id="rotation" type="text" name="rot" value="0">
                </input>
                <textarea name="text">{0}
                </textarea>
                <input type="submit" value="Encrypt Query">
                {1}
            </form>
        </body>
    </html>
"""

@app.route('/')
def index():
    return form.format("", "")

@app.route('/encrypt', methods=['post'])
def encrypt():
    rot = request.form["rot"]
    text = request.form["text"]
    
    
    return form.format(rotate_string(text, int(rot)), """<input type="submit" value="Decrypt Query"></input>""")

@app.route('/decrypt', methods=['post'])
def decrypt():
    rot = request.form["rot"]
    text = request.form["text"]
    
    return form.format(rotate_string(text, 26 - int(rot)))

app.run()
