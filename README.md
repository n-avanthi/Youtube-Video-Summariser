# YouTube-Video-Summariser
This is a YouTube video summarizer and question-answering tool implemented as a Chrome extension. It provides concise summaries of video transcripts and answer questions based on the video content. The application also supports summarizing videos in various languages by automatically translating the transcripts to the desired language before generating the summary.
This project aims to enhance the YouTube viewing experience by offering users a convenient way to quickly grasp the essence of a video through a summarized transcript and engage with the content by asking questions and receiving relevant answers, regardless of the language of the video.

## Requirements
- Python (3.6 or later)
- Flask
- youtube-transcript-api
- googletrans

## Executing the code
- Update your GEMINI_API_KEY in the ```.env``` file
- To set up the backend server
  ```bash
  $ python app.py
  ```
- Load the Chrome Extension by navigating to ```chrome://extensions/``` and enable 'Developer mode'. Click 'Load unpacked' and select the directory ```extension``` which contains the ```manifest.json```
- Go to any YouTube video and click on the 'Summarize' button to start summarizing.
