from flask import Flask, request, render_template
import base64
import pytesseract
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def index():
    captcha_url = request.args.get('url')
    if not captcha_url:
        captcha_url = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAFElEQVQYV2NkQAP/Gf4bBjCqAEMAAHQDAh0U8PYAAAAASUVORK5CYII='
    return render_template('index.html', captcha_url=captcha_url)

@app.route('/solve', methods=['POST'])
def solve():
    captcha_url = request.form['captcha_url']
    image_data = captcha_url.split(',')[1]
    image = Image.open(io.BytesIO(base64.b64decode(image_data)))
    solved_text = pytesseract.image_to_string(image)
    return solved_text

if __name__ == '__main__':
    app.run(debug=True)