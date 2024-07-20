# Transcribe Genius 🧠

**Transcribe Genius** is an AI-powered tool that summarizes YouTube video content into concise text. It leverages advanced AI models to generate summaries, and provides features for downloading the summary as a PDF, copying the text, and converting the text to audio.

## Features

- **Summarize Videos**: Paste a YouTube video URL and receive a concise summary.
- **Copy Text**: Copy the summarized text to your clipboard.
- **Play Audio**: Convert the summarized text to speech and play it directly in the browser.
- **Stop Audio**: Stop the audio playback if currently playing.
- **Download as PDF**: Download the summarized text as a PDF document.

## Technologies Used

- **Flask**: Python web framework for building the web application.
- **Requests**: For making HTTP requests to external APIs.
- **YouTube Transcript API**: For fetching video transcripts.
- **FPDF**: For generating PDF files.
- **Markdown2**: For converting text to Markdown format.

## Installation

1. **Clone the repository:**

    ```bash
    git clone <https://github.com/shahram8708/AI-Video-Summarizer/>
    cd <AI-Video-Summarizer>
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**

    ```bash
    python app.py
    ```

5. **Access the application in your web browser:**

    Open your browser and go to `http://127.0.0.1:5000/`.

## Configuration

- **API Key**: You need a valid API key for the Google Gemini API. Replace `AIzaSyBc9a2I57vkHjVYhJ42QkzMxZvwq0BY44k` with your own API key in the `app.py` file.

## Usage

1. **Enter the YouTube Video URL**: Paste the URL of the YouTube video you want to summarize into the input field.
2. **Summarize**: Click the "✅" button to generate the summary.
3. **Copy Text**: Click the "📋" button to copy the summary text to your clipboard.
4. **Play Audio**: Click the "▶️" button to convert the summary text to speech and play it. The button will change to "⏹️" to allow stopping the audio.
5. **Stop Audio**: Click the "⏹️" button to stop the audio playback.
6. **Download as PDF**: Click the "📥" button to download the summary as a PDF file.

## Development

To contribute or modify the application:

1. **Create a new branch:**

    ```bash
    git checkout -b
    ```

2. **Make your changes and commit:**

    ```bash
    git add .
    git commit -m 
    ```

3. **Push to the repository:**

    ```bash
    git push origin
    ```

4. **Create a Pull Request** to merge your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or support, please reach out to:

- **Email**: shahram8708@gmail.com
- **GitHub Issues**: [Submit an Issue](https://github.com/shahram8708/AI-Video-Summarizer/issues)
