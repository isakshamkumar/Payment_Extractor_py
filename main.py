from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api', methods=['POST'])
def receive_message_and_extract_amount():
    data = request.json
    messageArr = data.get('data')
    
    newArr = []
    for i in messageArr:
        pattern = r'\bRs:\s*(\d+\.\d{2})'
        import re
        match = re.search(pattern, i['message'])
        if match:
            amount = float(match.group(1))
            newArr.append(amount)
        else:
            print(i)
    return jsonify({'status': 'success', 'amounts': newArr}), 200

if __name__ == "__main__":
    # Run the app on all available network interfaces and use the provided port
    app.run(host='0.0.0.0', port=8080)
