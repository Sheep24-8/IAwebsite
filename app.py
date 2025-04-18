from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def data_page():
    return render_template('data.html')

@app.route('/health')
def health_page():
    return render_template('health.html')

if __name__ == '__main__':
    app.run(debug=True)
