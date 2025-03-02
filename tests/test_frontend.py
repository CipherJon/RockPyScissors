import unittest
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import threading
import requests

# Ensure the root directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

class TestFrontend(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start Flask server in a separate thread
        cls.flask_thread = threading.Thread(target=app.run, kwargs={'port': 5000, 'use_reloader': False})
        cls.flask_thread.daemon = True
        cls.flask_thread.start()
        # Wait for the server to start
        time.sleep(3)
        # Check if the Flask server is running
        try:
            requests.get('http://127.0.0.1:5000')
        except requests.exceptions.ConnectionError:
            raise RuntimeError("Flask server is not running")

    def setUp(self):
        self.driver = webdriver.Chrome()  # Ensure you have the Chrome WebDriver installed
        self.driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to become available

    def test_game(self):
        driver = self.driver
        driver.get('http://127.0.0.1:5000/static/index.html')
        
        # Test Rock
        rock_button = driver.find_element(By.XPATH, "//button[text()='Rock']")
        rock_button.click()
        time.sleep(1)
        result = driver.find_element(By.ID, 'result').text
        self.assertIn('You chose: rock', result)
        
        # Test Paper
        paper_button = driver.find_element(By.XPATH, "//button[text()='Paper']")
        paper_button.click()
        time.sleep(1)
        result = driver.find_element(By.ID, 'result').text
        self.assertIn('You chose: paper', result)
        
        # Test Scissors
        scissors_button = driver.find_element(By.XPATH, "//button[text()='Scissors']")
        scissors_button.click()
        time.sleep(1)
        result = driver.find_element(By.ID, 'result').text
        self.assertIn('You chose: scissors', result)

    def tearDown(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        # Stop the Flask server
        requests.get('http://127.0.0.1:5000/shutdown')

if __name__ == '__main__':
    unittest.main()