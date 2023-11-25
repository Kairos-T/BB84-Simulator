from flask import Flask, render_template, request
from main import quantum_communication, simulate_eavesdropping

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    error_rate = float(request.form['error_rate'])
    num_iterations = int(request.form['num_iterations'])
    eavesdrop = request.form.get('eavesdrop') == 'on'

    if eavesdrop:
        simulate_eavesdropping(num_iterations)
    else:
        quantum_communication(error_rate, num_iterations)

    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
