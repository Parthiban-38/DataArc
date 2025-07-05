from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    feedback = request.form['feedback']
    
    # Here you can save to a file or database
    with open('feedback.txt', 'a') as f:
        f.write(f"{name}: {feedback}\n")

    return render_template('thankyou.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
