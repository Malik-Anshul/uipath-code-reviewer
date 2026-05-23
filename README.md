# 🤖 UiPath Code Reviewer Agent

An AI-powered code reviewer specifically built for UiPath RPA automations.  
Built using Python, Groq API, and LLaMA 3.3 70B.

---

## 📌 What It Does

This project reviews UiPath automation code in **4 intelligent layers**:

### 🔹 Layer 1 — Syntax & Errors
- Detects syntax errors
- Finds undefined variables
- Identifies broken logic references

### 🔹 Layer 2 — Code Quality
- Checks naming conventions
- Reviews project structure
- Detects redundant or repetitive code
- Suggests cleaner practices

### 🔹 Layer 3 — Logic Analysis
- Finds logical flaws
- Detects possible edge cases
- Reviews workflow consistency

### 🔹 Layer 4 — Suggestions & Best Practices
- Gives optimization suggestions
- Recommends UiPath best practices
- Improves maintainability and readability

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Groq API | LLM provider |
| LLaMA 3.3 70B | AI model |
| python-dotenv | Environment variable management |

---

# 📁 Project Structure

```bash
uipath-code-reviewer/
│
├── src/
│   ├── agent.py          # Core agent logic
│   └── prompts.py        # System prompts
│
├── main.py               # Entry point
├── requirements.txt      # Dependencies
├── .env                  # API key (DO NOT PUSH)
└── README.md             # Documentation
```

---

# ⚙️ Setup & Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/uipath-code-reviewer.git
cd uipath-code-reviewer
```

---

## 2️⃣ Create Virtual Environment

### Windows
```bash
python -m venv venv
venv\Scripts\Activate.ps1
```

### Mac/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Add API Key

Create a `.env` file in the root folder:

```env
GROQ_API_KEY=your_api_key_here
```

Get your free API key from:  
https://console.groq.com

---

## 5️⃣ Run the Project

```bash
python main.py
```

---

# 🚀 How To Use

1. Run the project:

```bash
python main.py
```

2. Select option **1** to review code

3. Paste your UiPath automation code

4. Type:

```bash
END
```

5. Press Enter and get your detailed AI review ✅

---

# 📊 Sample Output

```bash
==================================================
⭐ Overall Score: 6/10
📝 Summary: Code has some logic errors and quality issues

🔍 LAYER 1 - SYNTAX
{
    "status": "good",
    "issues": [],
    "details": "No syntax errors found"
}

📐 LAYER 2 - QUALITY
{
    "status": "fair",
    "issues": [
        "variable naming",
        "magic strings"
    ],
    "details": "Variable names are not descriptive..."
}
==================================================
```

---

# 💡 What I Learned

- How AI agents work from scratch
- Prompt engineering for structured outputs
- Groq API integration
- JSON parsing and error handling
- Clean Python code architecture

---

# 🔮 Future Improvements

- [ ] Web UI using Streamlit
- [ ] File upload support (`.py` files)
- [ ] More UiPath-specific rules
- [ ] Export review as PDF
- [ ] Support for XAML files

---

# 👤 Author

**Your Name**

- GitHub: https://github.com/Malik-Anshul/
- LinkedIn: https://www.linkedin.com/in/anshu-malik-7ai/

---

# ⭐ Support

If you found this project useful, please give it a ⭐ on GitHub!
