from flask import Flask,request,jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    try:
        data = request.get_json()  # Assuming the request data is in JSON format
        num1 = data.get('first')    # Replace 'num1' with the actual key for the first number
        num2 = data.get('second')    # Replace 'num2' with the actual key for the second number

        if num1 is None or num2 is None:
            return "Both 'num1' and 'num2' must be provided in the request data.", 500

        result = num1 + num2  # Perform the addition

        return {"result": result}  # Return the result as JSON

    except Exception as e:
        return str(e), 400 

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    try:
        data = request.get_json()  # Assuming the request data is in JSON format
        num1 = data.get('first')    # Replace 'num1' with the actual key for the first number
        num2 = data.get('second')    # Replace 'num2' with the actual key for the second number

        if num1 is None or num2 is None:
            return jsonify(error="Both 'num1' and 'num2' must be provided in the request data."), 400

        result = num1 - num2  # Perform the subtraction

        return jsonify(result=result)  # Return the result as JSON

    except Exception as e:
        return jsonify(error=str(e)), 400

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
