from flask import Flask

app = Flask(_name_)

@app.route('/name')
def name():
    return "SATHYA. P"

@app.route('/register_number')
def register_number():
    return "22IT046"

@app.route('/department')
def department():
    return "IT"

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
