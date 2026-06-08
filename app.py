import streamlit as st
from src.helper import voice_input, llm_model, text_to_speech


def main():
    st.markdown("""
        <div style="text-align: center; padding: 2rem 0 1rem;">
            <h1 style="font-size: 2.5rem; font-weight: 700;">🤖 Multilingual AI Assistant</h1>
            <p style="color: gray; font-size: 1rem;">Speak in any language — get instant AI responses</p>
        </div>
    """, unsafe_allow_html=True)

    st.divider()

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        ask = st.button("🎙️ Ask me anything", use_container_width=True)

    if ask:
        with st.status("Processing your request...", expanded=True) as status:
            st.write("🎤 Listening...")
            text = voice_input()

            st.write("🧠 Thinking with Gemini...")
            response = llm_model(text)

            st.write("🔊 Generating speech...")
            text_to_speech(response)

            status.update(label="Done!", state="complete")

        st.divider()

        st.subheader("📝 Response")
        st.text_area(
            label="",
            value=response,
            height=250,
            disabled=True
        )

        st.subheader("🔊 Audio")
        audio_file = open("speech.mp3", "rb")
        audio_bytes = audio_file.read()
        audio_file.close()

        st.audio(audio_bytes, format="audio/mp3")

        st.download_button(
            label="⬇️ Download Speech",
            data=audio_bytes,
            file_name="speech.mp3",
            mime="audio/mp3",
            use_container_width=True
        )


if __name__ == '__main__':
    main()