# 🤖 Multilingual AI Voice Assistant

> Speak in any language — get instant AI responses

A voice-powered AI assistant built with **Streamlit**, **Google Gemini**, and **Google Text-to-Speech** that lets you ask questions in any language using your microphone and receive intelligent spoken responses.

---

## ✨ Features

- 🎙️ **Voice Input** — Speak your query directly into the microphone using `SpeechRecognition`
- 🌍 **Multilingual Support** — Understands and responds to queries in multiple languages
- 🧠 **Gemini AI** — Powered by Google's Gemini LLM for accurate, context-aware responses
- 🔊 **Text-to-Speech Output** — Converts AI responses to natural-sounding audio via `gTTS`
- ⬇️ **Downloadable Audio** — Save the generated speech as an MP3 file
- 🖥️ **Clean Web UI** — Minimal dark-themed interface built with Streamlit

---

## 🖼️ UI Preview

<img src="./image/image.png" alt="ui">

> A clean, centered interface with a single "Ask me anything" button to kick off the voice interaction.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend / UI | Streamlit |
| AI / LLM | Google Gemini (`google-generativeai`) |
| Speech-to-Text | SpeechRecognition + PyAudio |
| Text-to-Speech | gTTS (Google Text-to-Speech) |
| Environment Config | python-dotenv |
| Language | Python 3.x |

---

## 📁 Project Structure

```
Multilingual-AI-Voice-Assistant/
├── src/
│   └── helper.py          # Core logic: voice_input, llm_model, text_to_speech
├── app.py                 # Streamlit app entry point
├── requirements.txt       # Python dependencies
├── setup.py               # Package setup
├── template.py            # Project scaffold template
└── .gitignore
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- A working microphone
- A Google Gemini API key

### 1. Clone the Repository

```bash
git clone https://github.com/Pratik5767/Multilingual-AI-Voice-Assistant.git
cd Multilingual-AI-Voice-Assistant
```

### 2. Install Dependencies

On Windows, PyAudio requires `pipwin`:

```bash
pip install pipwin
pipwin install pyaudio
pip install -r requirements.txt
```

On Linux/macOS:

```bash
sudo apt-get install portaudio19-dev   # Linux
brew install portaudio                 # macOS
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

> Get your free API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

### 4. Run the App

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501` and click **🎙️ Ask me anything** to start.

---

## 🔄 How It Works

```
[User speaks into mic]
        ↓
[SpeechRecognition converts audio to text]
        ↓
[Text sent to Google Gemini API]
        ↓
[Gemini returns AI-generated response]
        ↓
[gTTS converts response to speech (speech.mp3)]
        ↓
[Streamlit displays text + plays audio]
```

---

## 📦 Dependencies

```
SpeechRecognition==3.10.0
pyaudio
gTTS
google-generativeai
python-dotenv
streamlit
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an [issue](https://github.com/Pratik5767/Multilingual-AI-Voice-Assistant/issues) or submit a pull request.

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Pratik** — [@Pratik5767](https://github.com/Pratik5767)

---

> ⭐ If you found this project helpful, consider giving it a star on GitHub!