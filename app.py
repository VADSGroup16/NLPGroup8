import streamlit as st
import requests

# Set the title of the Streamlit app
st.title("English to German Translation")

# Text input for the German sentence
german_sentence = st.text_input("Enter a English sentence:")

if st.button("Translate"):
    if german_sentence:
        # Make a POST request to the FastAPI endpoint
        response = requests.post(
            "https://5185-35-247-172-177.ngrok-free.app/translate",
            json={"sentence": german_sentence}
        )

        if response.status_code == 200:
            data = response.json()
            st.write("### Translation")
            st.write(f"**German Sentence:** {data['german_sentence']}")
        else:
            st.write("Error:", response.status_code)
    else:
        st.write("Please enter a German sentence.")
