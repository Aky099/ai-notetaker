import streamlit as st

from utils.summarize import summarize_transcript
from utils.transcribe import transcribe_audio


st.title("AI Notetaker")
st.write("Upload an audio recording to get a transcript and an AI-generated summary.")

uploaded_file = st.file_uploader(
    "Upload an audio file",
    type=["mp3", "wav", "m4a", "mp4", "webm", "ogg"],
)

if st.button("Process Audio", disabled=uploaded_file is None):
    if uploaded_file is None:
        st.warning("Please upload an audio file first.")
    else:
        try:
            with st.spinner("Transcribing audio..."):
                transcript = transcribe_audio(
                    uploaded_file.getvalue(),
                    uploaded_file.name,
                )

            with st.spinner("Summarizing transcript..."):
                summary = summarize_transcript(transcript)

            st.markdown(summary)

            with st.expander("View transcript"):
                st.text(transcript)
        except Exception as error:
            st.error(f"Unable to process the audio file: {error}")