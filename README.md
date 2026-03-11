# 🎯 AI-Powered Resume to Portfolio Website Generator

**Resume2Web AI** is an AI-powered application that automatically converts a resume (PDF/DOCX) or a manual text prompt into a **professional, responsive portfolio website** using modern frontend technologies.

With just one click, users can generate clean **HTML, CSS, and JavaScript** files packaged into a downloadable ZIP.

---

## 🚀 Features

* 📄 Upload Resume (PDF or DOCX)
* ✍️ Manual prompt-based input
* 🧠 AI-powered content understanding using **Google Gemini**
* 🌐 Generates a complete portfolio website
* 📦 Outputs clean **HTML, CSS, and JavaScript** files
* ⬇️ One-click ZIP download
* 🎨 Modern, responsive portfolio layout
* ⚙️ Simple and intuitive Streamlit UI

---

## 🧠 How It Works

1. User chooses an input method from the sidebar:

   * Manual prompt
   * Resume upload (PDF/DOCX)
2. The app extracts text from the resume (if uploaded).
3. The extracted content or prompt is sent to **Gemini AI**.
4. AI generates frontend code in a structured format.
5. The app saves the code as files and bundles them into a ZIP.
6. User downloads the ready-to-deploy portfolio website.

---

## 🛠️ Tech Stack

* **Frontend Generation**: HTML, CSS, JavaScript
* **AI Model**: Google Gemini (via LangChain)
* **Framework**: Streamlit
* **Language**: Python
* **Libraries**:

  * `langchain`
  * `langchain-google-genai`
  * `streamlit`
  * `python-dotenv`
  * `PyPDF2`
  * `python-docx`

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Resume2Web-AI.git
cd Resume2Web-AI
```

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Setup

Create a `.env` file in the project root:

```env
gemini=YOUR_GOOGLE_GEMINI_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Then open your browser at:

```
http://localhost:8501
```

---

## 📁 Output Structure

After generation, the app provides a ZIP file containing:

```text
portfolio_website.zip
├── index.html
├── style.css
└── script.js
```

You can deploy these files directly to:

* GitHub Pages
* Netlify
* Vercel
* Any static hosting service

---

## 🎯 Use Cases

* Developers building personal portfolios
* Students creating online resumes
* Designers showcasing projects
* Hackathons & AI demos
* Resume-to-website automation

---

## 🚀 Future Enhancements

* 🌈 Theme selector (Dark / Light)
* 🖼 Profile photo upload
* 📄 Resume parsing into structured JSON
* 🔗 GitHub & LinkedIn auto-linking
* 🌍 Live preview inside the app
* ☁️ One-click deployment

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**.

---

## ⭐ Acknowledgements

* Google Gemini AI
* LangChain
* Streamlit Community

---

## 💡 Author

Name - Sahu Pavan
Linkedin - linkedin.com/in/sahu-pavan
