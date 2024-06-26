# Streamlit_project

This project displays some basic application of machine learning models, including word correction based on levenshtein algorithm, implementing object detection with a MobileNet SSD model, and building a chatbot

## Installation
To install this application, follow these steps:

**1. Clone the repository:**
```bash
git https://github.com/Tuevu110405/Streamlit_project.git
cd Streamlit_project
```
**2. (Optional) Create and activate a virtual environment:**
- For Unix/macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

- For Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

**3. Install the required dependencies:**
```bash
pip install -r requirements.txt
```

## Implementing models
When everything is ready, you can launch these models by running one of the following commands:
- Word correction
```sh
streamlit run models/word_correction.py
```
- Object Detection
```sh
streamlit run models/object_detection.py
```
- Chatbot
```sh
streamlit run models/chatbot.py
```
