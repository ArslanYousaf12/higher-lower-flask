# Higher Lower Flask Game

A web-based guessing game built with Flask where users try to guess whether the next randomly generated number will be higher or lower than the current one.

## Description

This simple web application implements the classic "Higher or Lower" guessing game using Flask. The game generates random numbers, and players need to predict whether the next number will be higher or lower than the current one. It's a fun way to test your luck and intuition!

## Features

- Random number generation
- Score tracking
- Simple and intuitive interface
- Responsive web design for both desktop and mobile

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/arslanyousaf12/higher-lower-flask.git
   cd higher-lower-flask
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the App

1. Start the Flask application:
   ```bash
   python server.py
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## How to Play

1. The game will display a random number.
2. Guess whether the next number will be higher or lower by clicking the corresponding button.
3. If your guess is correct, you earn a point.
4. Try to get as many correct guesses as possible!

## Technologies Used

- Python 3
- Flask
- HTML/CSS
- Jinja2 Templates

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.