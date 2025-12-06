from flask import Flask, request
import calc

app = Flask(__name__)

@app.route('/')
def home_page():
    return """
    ====Simple Calculator====<br>
    Usage:<br>
    - /equation?&a=N&b=N&c=N - to solve ax^2 + bx + c = 0 equation<br>"""

@app.route('/equation', methods=['GET'])
def equation_page():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    c = float(request.args.get('c'))
    res = calc.equation(a, b, c)
    return res

if __name__ == "__main__":
    app.run()