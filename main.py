from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def receive_message_and_extract_amount():
    data = request.json
    messageArr = data.get('data')
    print(messageArr)
    
    newArr = []
    for  i in messageArr:
        print(i)
        pattern = r'\bRs:\s*(\d+\.\d{2})'
        import re
        match = re.search(pattern, i['message'])
        if match:
            amount = float(match.group(1))
            newArr.append(amount)
            # return jsonify({'status': 'success', 'message': f'Extracted amount: {amount}'}), 200
        else:
            # return jsonify({'status': 'error', 'message': 'No amount found in the message.'}), 400
            print(i)
    return jsonify({'status': 'success', 'amounts': newArr}), 200
        # Example regex to extract amounts (adjust as needed)
    

if __name__ == "__main__":
    app.run(debug=True)