import streamlit as st
import speech_recognition as sr

# Set the title of the app
st.title("Speech Recognition App")

# Initialize the recognizer
recognizer = sr.Recognizer()

# Explanation of the app's functionality
st.write("""
This app allows you to speak into your microphone, and it will transcribe your speech into text using Google's Speech Recognition API.
Simply click the "Start Speaking" button, and the app will listen to your speech and provide a transcription.
""")

# Create a button for the user to click to start speaking
if st.button("Start Speaking"):
    # Inform the user to speak into the microphone
    st.info("Please speak now...")

    # Use the microphone as the audio source for speech recognition
    with sr.Microphone() as source:
        # Adjust for ambient noise (background noise like room sounds)
        recognizer.adjust_for_ambient_noise(source)
        
        # Listen for the speech input from the microphone
        audio_data = recognizer.listen(source)
        
        # Attempt to recognize the speech using Google's Speech Recognition API
        try:
            # Using the Google Web Speech API to convert speech to text
            text = recognizer.recognize_google(audio_data)
            
            # If the speech is successfully recognized, display the transcription
            st.success("Transcription:")
            st.write(text)
        
        except sr.UnknownValueError:
            # Error handling when the speech could not be understood
            st.error("Sorry, I could not understand the audio. Please try again.")
        
        except sr.RequestError:
            # Error handling when the Google Speech Recognition service cannot be reached
            st.error("There was an error with the Google Speech Recognition service. Please try again later.")
