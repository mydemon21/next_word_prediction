# Next-Word Prediction App

## Overview

This Streamlit app uses the Hugging Face transformers library to predict the next word in a given text. The application is built using the GPT-2 model from Hugging Face.

## Features

- **Next-Word Prediction**: Enter a text and get predictions for the next word(s) using GPT-2.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/mydemon21/next_word_prediction.git
    cd next_word_prediction
    ```

2. **Create and activate a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Streamlit app**:

    ```bash
    streamlit run app.py
    ```

2. **Interact with the App**:
   - Open the provided URL in your web browser.
   - Enter a text in the input field to get the next-word prediction.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
