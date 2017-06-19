from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
form = 
"""
    <!DOCTYPE html>
            <hmtl>
                <head>
                    <style>
                        form {
                            background-color: #eee;
                            padding: 20px;
                            margin: 0 auto;
                            width: 540px;
                            font: 16px sans-serif;
                            border-radius: 10px; 
                        }
                         textarea {
                            margin: 10px 0;
                            width: 540px;
                            height: 120px;
                        }
                    </style>
                </head>
                <body>
                <!-- create your form here -->
                </body>
            </html>               
"""
def index():
    return 'Hello World!'

app.run()