# captcha-solver-x1212as3a

## Overview

`captcha-solver-x1212as3a` is a web application designed to solve CAPTCHA images provided via a URL parameter. The application can handle image URLs and display the solved text within 15 seconds.

## Features
- Accepts a CAPTCHA image URL via the `?url=` query parameter.
- Displays the CAPTCHA image on the page.
- Solves the CAPTCHA and displays the solved text.
- Default to a sample CAPTCHA image if no URL is provided.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/captcha-solver-x1212as3a.git
   cd captcha-solver-x1212as3a
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python app.py
   ```
2. Open your web browser and navigate to `http://localhost:5000/?url=<CAPTCHA_IMAGE_URL>`.
   - Replace `<CAPTCHA_IMAGE_URL>` with the URL of the CAPTCHA image you want to solve.
   - If no URL is provided, the application will default to a sample CAPTCHA image.

## Example

To test the application with the sample CAPTCHA image, use:
```
http://localhost:5000/?url=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAFElEQVQYV2NkQAP/Gf4bBjCqAEMAAHQDAh0U8PYAAAAASUVORK5CYII=
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.