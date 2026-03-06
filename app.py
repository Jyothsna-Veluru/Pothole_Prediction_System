from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('home.html', page='home')

@app.route('/support')
def support():
    return render_template('support.html', page='support')

@app.route('/contact')
def contact():
    return render_template('contact.html', page='contact')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    result = "Pothole detected with 0.78 confidence"  # Example result
    return render_template('result.html', filename=filename, result=result, page='')


if __name__ == '__main__':
    app.run(debug=True)
