# app.py

import streamlit as st
from transformers import pipeline

# Initialize the next-word prediction pipeline from Hugging Face
generator = pipeline('text-generation', model='gpt2')

# Streamlit app layout
st.title("Next-Word Prediction App")

# Input field for user text
input_text = st.text_input("Enter your text:", "")

if input_text:
    try:
        # Generate multiple text completions using the model
        predictions = generator(input_text, max_new_tokens=1, num_return_sequences=5, top_k=50, temperature=0.7)
        
        # Extract the next word suggestions from each prediction
        suggestions = [pred['generated_text'][len(input_text):].strip() for pred in predictions]
        
        # Post-process suggestions to filter out invalid ones
        suggestions = [s for s in suggestions if s.isalpha()]

        # Display the suggestions
        st.subheader("Next Word Suggestions:")
        for i, suggestion in enumerate(suggestions, start=1):
            st.write(f"{i}. {suggestion}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please enter some text to get a prediction.")

