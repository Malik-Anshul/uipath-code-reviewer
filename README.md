# 🤖 UiPath Code Reviewer Agent

An AI-powered code reviewer specifically built for UiPath RPA automations.  
The system analyzes automation code using LLM-powered multi-layer review pipelines.

Built completely from scratch using Python, Groq API, and LLaMA 3.3 70B — without using any agent framework.

---

# 🚀 Features

## ✅ Dual Input Support
The agent supports two different ways to review code:

- Direct code paste
- `.py` file path input using a File Reader Tool

---

## 🧠 4-Layer Intelligent Code Review

### 🔹 Layer 1 — Syntax & Basic Errors
- Detects syntax errors
- Finds undefined variables
- Identifies broken references
- Detects basic runtime risks

### 🔹 Layer 2 — Code Quality Analysis
- Reviews naming conventions
- Detects redundant code
- Checks code structure
- Suggests cleaner practices

### 🔹 Layer 3 — Logic & Edge Case Analysis
- Finds logical flaws
- Detects possible edge cases
- Reviews workflow consistency
- Identifies risky conditions

### 🔹 Layer 4 — Suggestions & Best Practices
- Gives optimization suggestions
- Recommends UiPath best practices
- Improves maintainability
- Enhances readability

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Groq API | LLM provider |
| LLaMA 3.3 70B | AI model |
| python-dotenv | Environment variable management |
| JSON | Structured output parsing |

---

# 🧠 How The Agent Works

```text
User Input / File Path
            ↓
     File Reader Tool
            ↓
    Prompt Construction
            ↓
      Groq API Call
            ↓
    LLaMA 3.3 70B Model
            ↓
 Structured Multi-Layer Review
            ↓
     JSON Output Response
```

---

# 📁 Project Structure

```bash
uipath-code-reviewer/
│
├── src/
│   ├── agent.py           # Core agent logic
│   ├── prompts.py         # System prompts
│   ├── tools.py           # File reader tool
│   └── parser.py          # JSON parsing & formatting
│
├── main.py                # Entry point
├── requirements.txt       # Dependencies
├── .env                   # API key (DO NOT PUSH)
└── README.md              # Documentation
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

## 🔹 Option 1 — Direct Code Paste

1. Run the project

```bash
python main.py
```

2. Select review option
3. Paste UiPath/Python automation code
4. Type:

```bash
END
```

5. Get AI-generated review output ✅

---

## 🔹 Option 2 — File Path Input

Provide the `.py` file path:

```bash
D:\Projects\automation.py
```

The File Reader Tool automatically:
- Reads file contents
- Sends code to the agent
- Generates structured review output

---

# 📊 Sample Output

```bash
==================================================
⭐ Overall Score: 8/10
📝 Summary: Code quality is good but some edge cases exist.

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
        "magic strings",
        "non-descriptive variable names"
    ],
    "details": "Some variable names can be improved."
}

🧠 LAYER 3 - LOGIC
{
    "status": "warning",
    "issues": [
        "possible null condition"
    ],
    "details": "Missing validation before loop execution."
}

💡 LAYER 4 - SUGGESTIONS
{
    "suggestions": [
        "Add input validation",
        "Use constants for reusable values",
        "Improve exception handling"
    ]
}
==================================================
```

---

# 💡 Key Learnings

Through this project, I explored:

- How AI agents work internally
- Tool integration in AI agents
- Prompt engineering for structured outputs
- JSON parsing & formatting
- Error handling & edge cases
- Modular Python architecture
- LLM workflow design

---

# 🔮 Future Improvements

- [ ] Streamlit Web UI
- [ ] Upload `.py` files directly
- [ ] Support for `.xaml` UiPath workflows
- [ ] Export review reports as PDF
- [ ] More advanced UiPath-specific validations
- [ ] Multi-agent review pipeline
- [ ] AI-powered code scoring dashboard

---

# 📸 Demo

<img width="1841" height="950" alt="Screenshot 2026-05-23 183221" src="https://github.com/user-attachments/assets/4978e878-4c77-4bf3-b85a-620b35c71e20" />



---

# 👤 Author

**Anshul Malik**

- GitHub: https://github.com/Malik-Anshul/
- LinkedIn: https://www.linkedin.com/in/anshu-malik-7ai/

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
