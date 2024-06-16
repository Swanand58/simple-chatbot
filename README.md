# Simple Chatbot

A simple chatbot built using Python and TFlearn.

## Overview

This project implements a basic chatbot using neural networks. It leverages the TFlearn library for training the model and Flask for creating a web interface.

## Features

- Chatbot logic implemented in `bot.py`
- Web interface using Flask (`app.py`)
- Training data defined in `intents.json`
- Model and training data saved in `model.tflearn.*` and `data.pickle`

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Swanand58/simple-chatbot.git
   ```

2. Navigate to the project directory:

   ```bash
   cd simple-chatbot
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. run the app:

   ```bash
   python app.py
   ```

5. Usage:

- Access the chatbot via the web interface at http://127.0.0.1:5000.
- Modify intents.json to customize the chatbot's responses

## Project Structure

- app.py: Main application script.
- bot.py: Contains the chatbot logic.
- static: Contains static files for the web interface.
- templates: HTML templates for the web interface.
- intents.json: Defines the intents and responses for the chatbot.
- db.py: Script for handling database operations.
- model.tflearn.\*, data.pickle, checkpoint: Model files and data.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.
