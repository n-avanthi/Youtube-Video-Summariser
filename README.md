# YouTube-Video-Summariser
This is a YouTube video summarizer and question-answering tool implemented as a Chrome extension. It provides concise summaries of video transcripts and answer questions based on the video content. The application also supports summarizing videos in various languages by automatically translating the transcripts to the desired language before generating the summary.
This project aims to enhance the YouTube viewing experience by offering users a convenient way to quickly grasp the essence of a video through a summarized transcript and engage with the content by asking questions and receiving relevant answers, regardless of the language of the video.

## Requirements
- Python (3.6 or later)
- Flask
- youtube-transcript-api
- googletrans

## Setting up the extension
1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/n-avanthi/Youtube-Video-Summariser.git
    ```
2. Navigate to the project directory:

    ```bash
    cd Youtube-Video-Summariser
    ```
3. Create and update the `.env` file:

    ```bash
    GEMINI_API_KEY="Your-Gemini-API-key"
    ```
4. To set up the backend server (make sure this is running in the background for the extension to work)
  ```bash
  $ python app.py
  ```
5. Load the Chrome Extension by navigating to ```chrome://extensions/``` and enable 'Developer mode'. Click 'Load unpacked' and select the directory ```extension``` which contains the ```manifest.json```
6. Go to any YouTube video and click on the 'Summarize' button to start summarizing.
