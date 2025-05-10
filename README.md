# AutoToon – AI Comic Generator

AutoToon is an AI-driven comic generator that transforms any short story into a beautifully illustrated comic book. Using Google Gemini's multimodal capabilities, AutoToon analyzes your story, breaks it into scenes, generates detailed panel prompts, creates stylistically consistent images, and compiles them into a downloadable PDF comic.

---

## Features

* Story to Scene Breakdown – Automatically splits your story into manageable visual scenes.
* Style Guide Generation – Creates a visual design guide to ensure consistency across panels.
* Panel Prompt Generation – Describes each panel in rich visual detail using the selected style.
* AI Image Creation – Uses Gemini's image model to generate high-quality square comic panels.
* PDF Export – Compiles all panels into a single high-resolution comic book PDF.
* Parallel Processing – Fast and efficient generation with multi-threading.

---

## Example Styles

* 2D (Flat Art)
* Manga Style
* Vector Art
* Painted / Watercolor Style
* 3D Rendered (Stylized)
* Grayscale / Black & White
* Ink & Brush (Traditional Inking)

---

## Tech Stack

* **Frontend**: Streamlit
* **Backend**: Google Gemini API (genai)
* **Image Handling**: Pillow (PIL)
* **Concurrency**: Python's ThreadPoolExecutor

---

## Installation

```bash
git clone https://github.com/your-username/auto-toon.git
cd auto-toon
pip install -r requirements.txt
```

Ensure you have a valid Google Gemini API key. You can get one from the [Google AI Studio](https://makersuite.google.com/app/apikey).

---

## Usage

```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## API Key Setup

You will need a **Gemini API key** from Google AI Studio to use this application. Enter it in the sidebar of the app. It is not stored or shared.

---

## Project Structure

```
auto-toon/
│
├── app.py                  # Streamlit frontend
├── backend.py              # Core logic and Gemini API interaction
├── image/                  # Stores generated comic panels and final PDF
├── requirements.txt        # Python dependencies
└── README.md
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Future Improvements

* Speech balloon + narration box generation
* Panel layout customization (e.g., vertical manga style)
* Scene editor / preview before generation
* Multilingual story input support

---

## Acknowledgments

* Thanks to Google AI for the Gemini API
* Inspired by creators who tell stories with code and imagination

---