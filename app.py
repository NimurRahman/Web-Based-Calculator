from flask import Flask, render_template, request

from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Calculator</title>
</head>
<body>
    <h2>Simple Calculator</h2>
    <form method="post">
        <input type="text" name="num1" placeholder="Number 1" required>
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>
        <input type="text" name="num2" placeholder="Number 2" required>
        <button type="submit">Calculate</button>
    </form>
    <h3>Result: {{result}}</h3>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = ""
    if request.method == 'POST':
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        operation = request.form.get("operation")
        try:
            if operation == "add":
                result = float(num1) + float(num2)
            elif operation == "subtract":
                result = float(num1) - float(num2)
            elif operation == "multiply":
                result = float(num1) * float(num2)
            elif operation == "divide":
                result = float(num1) / float(num2)
        except (ValueError, ZeroDivisionError):
            result = "Invalid input or division by zero."
    # This line renders the index.html template and sends the result to it
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)

