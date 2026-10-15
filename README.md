# 🎨 ComicCraft - AI Comic Story Creator

Turn a story prompt into a fully illustrated, downloadable comic using Google's Gemini models and Stable Diffusion.

### Features
- 5-panel comic story generation using Gemini Flash
- Dialogue & narration using Gemini Pro
- Image generation using Stable Diffusion
- PDF export using FPDF
- FastAPI + Streamlit support

### Tech Stack
FastAPI, Uvicorn, Python, HTML/CSS/Jinja2, Gemini API, Hugging Face Diffusers, PyTorch, FPDF, Git, pip

### How to Run
pip install -r requirements.txt
uvicorn app.main:app --reload
# OR
streamlit run app.py

### API Keys
GEMINI_API_KEY from https://aistudio.google.com/apikey
HF_API_KEY from https://huggingface.co/settings/tokens

Developed by Rithika C for Vetri Thiran Payirchi Thittam
