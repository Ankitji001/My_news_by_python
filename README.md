# 📰 My News App

A clean, responsive desktop GUI application built in Python using **Tkinter** and **Pillow**. The application connects live to the **NewsAPI** network feed to stream top headlines, structural details, and real-time imagery directly to a user's desktop interface.

---

## 🚀 Features
* **Live News Processing:** Pulls real-time international news payloads dynamically using network endpoints.
* **Responsive Layout:** Automatically fetches, resizes, and renders article images securely via internal memory streams.
* **Navigation Control Panel:** Intuitive `Next`, `Prev`, and `Read More` buttons to step through active data streams.
* **Secure Core:** Features environment variable parameters to fully hide system authentication tokens before pushing online.

---

## 🛠️ Prerequisites & Installation

Before running the app, ensure you have Python 3 installed on your system. Open your terminal inside the project directory and install the necessary library dependencies:

```bash
pip install requests pillow python-dotenv
```

---

## 🔐 Configuration Instructions

This application supports two distinct ways to manage your NewsAPI URL parameters depending on your deployment goal:

### Method 1: The Secure Way (Recommended for GitHub)
This approach completely isolates your private key credentials into a hidden `.env` configuration file so you can share your source code publicly without leaks.

1. Create a file named `.env` in the root folder of your project.
2. Add your full URL API link inside it like this:
   ```text
   NEWS_API_KEY=https://newsapi.org
   ```
3. Ensure `.env` is listed inside your `.gitignore` file so Git skips tracking it.
4. The code fetches this variable dynamically using:
   ```python
   # 1. Fetch the value stored in the environment variable
   full_url = os.getenv('NEWS_API_KEY')

   # 2. Pass the fetched variable string into requests (WITHOUT literal quotes around it)
   self.data = requests.get(full_url).json()
   ```

### Method 2: The Direct URL Way (Quick Local Testing)
If you are running the project strictly on your local machine and do not plan to share the repository publicly, you can drop the environment configuration and paste the full string address directly into the source query:

```python
# Pass the full literal URL string directly into the requests method
self.data = requests.get('https://newsapi.org').json()
```

---

## 🏃 How to Run the App

Once your configuration choice is set up, launch the desktop interface by executing the main script file:

```bash
python news_gui.py
```
