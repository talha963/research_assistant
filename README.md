# 🧠 Calder AI Research Assistant

An AI-powered research assistant built with **Streamlit**, **LangChain**, and **Groq LLMs**. The application performs structured research on a given topic and generates a well-formatted report with citations and an AI confidence score.

## 🚀 Features

- 🔍 Research any topic using an LLM
- 📄 Generates a structured research report
- 📊 Displays AI confidence score
- 📚 Includes citations for reference
- ⚡ Fast inference using Groq
- 🎨 Simple and interactive Streamlit interface
- ✅ Structured output using Pydantic models

---

## 🛠️ Tech Stack

- Python 3.13
- Streamlit
- LangChain
- Groq API
- Pydantic
- python-dotenv

---

## 📂 Project Structure

```
Calder_Project/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Project dependencies
├── .env                   # API keys (Not included in GitHub)
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Calder-Project.git
```

### 2. Move into the project folder

```bash
cd Calder-Project
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 📸 Demo

You can add screenshots here later.

Example:

```
assets/home.png
assets/result.png
```

---

## 💡 How It Works

1. User enters a research topic.
2. LangChain builds a research prompt.
3. Groq LLM generates detailed research.
4. Output is parsed using Pydantic.
5. Streamlit displays:
   - Research Report
   - Confidence Score
   - Citations

---

## 📦 Requirements

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## 🔮 Future Improvements

- PDF Export
- Multiple LLM Support
- Chat History
- Research Memory
- RAG Integration
- Web Search Support
- Source Verification
- Dark/Light Theme

---

## 👨‍💻 Author

**Talha Khan**

AI & Software Engineering Student

GitHub: https://github.com/YOUR_USERNAME

LinkedIn: https://linkedin.com/in/YOUR_LINKEDIN

---

## 📄 License

This project is licensed under the MIT License.
