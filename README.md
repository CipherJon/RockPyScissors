# Rock Paper Scissors Game

This is a simple Rock Paper Scissors game with a Flask backend and a web-based frontend interface. The application allows users to play the game against the computer.

## Project Structure

```
rock-paper-scissors/
├── LICENSE
├── README.md
├── app.py
├── requirements.txt
├── game/
│   ├── __init__.py
│   ├── game_logic.py
│   ├── player.py
│   └── __pycache__/
│       ├── __init__.cpython-313.pyc
│       ├── game_logic.cpython-313.pyc
│       └── player.cpython-313.pyc
├── static/
│   ├── index.html
│   ├── styles.css
│   └── script.js
├── tests/
│   ├── __init__.py
│   ├── test_game_logic.py
│   ├── test_flask_app.py
│   └── test_frontend.py
│   └── __pycache__/
│       ├── test_game_logic.cpython-313.pyc
│       └── test_flask_app.cpython-313.pyc
```

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/rock-paper-scissors.git
   cd rock-paper-scissors
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask server**:
   ```bash
   python app.py
   ```

2. **Access the web interface**:
   Open your web browser and navigate to `http://127.0.0.1:5000/static/index.html` to play the game.

## Running the Tests

1. **Unit and Integration Tests**:
   ```bash
   python -m unittest discover tests
   ```

2. **Selenium Frontend Tests**:
   Make sure the Flask server is running before executing the Selenium tests.
   ```bash
   python tests/test_frontend.py
   ```

## Project Details

- **Backend**: Flask
- **Frontend**: HTML, CSS, JavaScript
- **Testing**: `unittest`, `Selenium`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.