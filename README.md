# Cybersecurity AI Chatbot

This project is a web-based AI chatbot assistant focused on cybersecurity, built with Flask and OpenAI's GPT models. The chatbot provides long, detailed, and comprehensive answers to user questions about cybersecurity, information security, and digital safety.

## Features

- **Conversational AI**: Uses OpenAI's GPT-3.5/4-turbo models for natural, informative responses.
- **Session-based Chat**: Maintains conversation history per user session.
- **Web Interface**: Clean, responsive UI with avatars and code highlighting.
- **Clear Chat**: Option to clear the current conversation.
- **Customizable System Prompt**: Tailored for cybersecurity expertise.

## Demo

![Chatbot Screenshot](static/images/gpt.jpg)

## Getting Started

### Prerequisites
- Python 3.7+
- An OpenAI API key ([get one here](https://platform.openai.com/account/api-keys))

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/manish_chatbot.git
   cd manish_chatbot
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv_1
   venv_1\Scripts\activate  # On Windows
   # Or
   source venv_1/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Create a `.env` file in the project root:
     ```env
     OPENAI_API_KEY=your_openai_api_key_here
     ```

### Running the App

```bash
python app_1.py
```

- The app will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000)

### Usage
- Type your cybersecurity question in the chat box and press Send.
- The chatbot will respond with a detailed answer.
- Click "Clear Chat" to reset the conversation.

## Project Structure

```
manish_chatbot/
├── app_1.py            # Main Flask app with session-based chat
├── app.py              # Alternate Flask app (single-turn, cybersecurity expert)
├── requirements.txt    # Python dependencies
├── static/
│   ├── images/         # Avatars for user and bot
│   └── style.css       # Custom styles
├── templates/
│   └── index.html      # Main chat UI
└── README.md           # Project documentation
```

## Customization
- **Model**: Change the model in `app_1.py` or `app.py` (e.g., `gpt-3.5-turbo`, `gpt-4-turbo`).
- **System Prompt**: Edit the system message in the Python files to adjust the chatbot's persona.

## Notes
- Do **not** commit your `.env` file or API keys to version control.
- The `venv_1/` folder should be excluded from git (add to `.gitignore`).

## License
This project is for educational and personal use. For commercial use, check OpenAI's terms and add a license as needed.

---

Feel free to contribute or open issues for suggestions!

---

### 1. **Security**
- **Sensitive information**: You might have files like `.env` that contain API keys, passwords, or other secrets. If you accidentally upload these, anyone can see them on GitHub, which can lead to security breaches or abuse of your API keys.

### 2. **Reduce Repository Size**
- **Unnecessary files**: Some files and folders (like virtual environments, build artifacts, or temporary files) are large and not needed for your code to run elsewhere. Uploading them makes your repository bigger and slower to clone.

### 3. **Consistency Across Environments**
- **Machine-specific files**: Files like OS-generated files (`Thumbs.db`, `.DS_Store`), IDE settings, or compiled code are specific to your computer and not needed by others. Ignoring them keeps the repository clean and consistent for everyone.

### 4. **Best Practices**
- **Virtual environments**: For Python projects, folders like `venv_1/` contain all the installed packages for your local machine. Other users should create their own virtual environment using `requirements.txt` rather than using yours.

---

## Example: What to Put in `.gitignore` for Your Project

```
# Ignore Python virtual environment
venv_1/

# Ignore environment variable files
.env

# Ignore OS and editor files
__pycache__/
*.pyc
.DS_Store
Thumbs.db

# Ignore log files
*.log
```

---

## Summary

- The `.gitignore` file keeps your repository safe, clean, and professional.
- It prevents accidental uploads of sensitive or unnecessary files.
- It helps collaborators and users set up the project correctly on their own machines.

Would you like me to create a `.gitignore` file for your project?