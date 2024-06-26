#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')    
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/string:text>', methods=['GET']) 
def print_string(text):
    print(text)
    return text

@app.route('/count/<int:number>')
def count(number):
    count = ''
    for n in range(number):
        count += f'{n}\n'
    return count

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, num2, operation):
    if operation == '+':
        return str(num1 + num2)
    
    elif operation == '-':
        return str(num1 - num2)

    elif operation == '*':
        return str(num1 * num2)

    elif operation == 'div':
        return str(num1 / num2)

    elif operation == '%':
        return str(num1 % num2)

if __name__ == '__main__':
    app.run(port=5555, debug=True)


