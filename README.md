# 💼 Showvator – The Smart Portfolio Showcase Activator

**Showvator** is an intelligent, interactive portfolio chatbot that lets anyone explore the technical background, achievements, and expertise of **Muhammad Ali Musawir** — as if they’re speaking directly with him.

This project is not just a static résumé or portfolio — it’s a **smart assistant** that can answer any question about Muhammad Ali’s profile in a conversational, expressive, and impressive tone.

Live Demo: 👉 [Visit the Showvator Web App](https://muhammadalimusawir-showvator-portfolio-chatbot.streamlit.app)

---

## ✨ Features

- 🔹 AI-powered responses via [OpenRouter API](https://openrouter.ai) (uses DeepSeek Chat model)
- 🔹 Reads dynamically from an external `portfolio.txt` (easy to update without changing code)
- 🔹 Professional UI using **Streamlit**
- 🔹 Lightweight standalone `.exe` launcher to access the chatbot directly
- 🔹 Fully free, serverless, and open-source – deploy it anywhere!

---

## 📦 Requirements

> These are only needed if you want to run or modify the source code.

- Python 3.9 or later
- `streamlit`, `requests`, `python-dotenv`
- OpenRouter API Key (free or paid)
- Internet connection (for model response)

---

## ⚙️ How It Works

There are **two ways** to use this chatbot after downloading the project:

### ✅ 1. Use the Ready-Made Website Launcher

Go to the folder:
```
Website/Showvator - Portfolio Chatbot.exe
```

Just **double-click the `.exe` file**, and it will open the hosted chatbot in your browser.

This is perfect for trying the website without touching any code.

---

### 🛠️ 2. Run the Source Code (with custom portfolio or model)

Go to the folder:
```
Source Code/
```

Then make the following changes:

1. **Add your OpenRouter API key**  
   Inside `Assets/`, create a `.env` file:
   ```
   OPENROUTER_API_KEY=your_api_key_here
   ```
   
2. **Make sure the file paths are correct**  
Update the paths in `main.py` **if your folder structure is different**, especially for:
- `logo.png`
- `icon.ico`
- `portfolio.txt`
- 
3. **Install required packages**

```
pip install -r Assets/requirements.txt
```

4. **Run the app**

```
streamlit run main.py
```

---

## 🗂 Folder Structure

Here’s what the downloaded project will look like:

```
Showvator – The Smart Portfolio Showcase Activator/
├── Source Code/
│   ├── main.py                     # Main Streamlit app
│   ├── .gitignore
│   ├── .streamlit/
│   │   └── config.toml
│   ├── Assets/
│   │   ├── logo.png
│   │   ├── icon.ico
│   │   ├── portfolio.txt
│   │   ├── requirements.txt
│   │   └── .env (you must create this manually)
├── Website/
│   ├── Assets/
│   │   └── icon.ico
│   └── Showvator - Portfolio Chatbot.exe
├── README.md
└── LICENSE
```

---

## 🧠 Behind the Chatbot

The chatbot is powered by the `deepseek/deepseek-chat-v3-0324:free` model via the [OpenRouter API](https://openrouter.ai/).  
The responses are **influenced by the content of `portfolio.txt`**, written in a conversational tone — as if Muhammad Ali Musawir himself is replying.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Built By

**Muhammad Ali Musawir**  
Electrical Engineer | AI & Embedded Systems | Chatbot Architect  
[GitHub](https://github.com/Muhammad-Ali-Musawir)  
[LinkedIn](https://linkedin.com/in/muhammad-ali-musawir)
