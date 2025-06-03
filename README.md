# Gemini AI Assistant 🤖

A simple command-line AI assistant powered by **Google's Gemini 2.0 Flash model** using Python. This project uses the `agents` library to configure an AI agent that responds to user queries via Gemini's Generative Language API.

---


## 🛠 Technologies Used

- Python  
- Gemini 2.0 Flash (Generative Language API)  
- `agents` library  
- `dotenv` for API key management  
- **uv** – a modern Python package manager for fast and reliable environments

---

## 🚀 How It Works

1. Loads the Gemini API key securely from an `.env` file.  
2. Initializes the Gemini model via `AsyncOpenAI` client.  
3. Sets up a custom agent with predefined instructions.  
4. Uses the `Runner` class to execute the agent synchronously.  
5. Outputs the assistant's response directly in the terminal.

---

## 📦 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/DanishHaji/My_First_Chat_AI_Agent.git
cd your-repo-name

# Create and sync environment using uv
uv venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
uv pip install -r requirements.txt
```

📁 Then, create a `.env` file in the root directory with your API key:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

---

## 🧠 Example Prompt

```bash
Who is the founder of Pakistan? and what is the population of Pakistan?
```

The assistant will return an accurate response using Gemini 2.0 Flash.

---

## 🙏 Acknowledgments

Special thanks to:  
- **Sir Zia Khan** – COO of GIAIC  
- **Sir Ameen Alam** – Dean of Faculty, GIAIC  
For their exceptional support and contribution to AI education in Pakistan.

---

## 📌 License

This project is for educational purposes only.

---

## 📢 Connect

If you like this project, feel free to ⭐ the repo and connect with me on [LinkedIn](#) *(www.linkedin.com/in/danish-b5b26b190)*
