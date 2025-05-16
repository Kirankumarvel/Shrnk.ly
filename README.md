

<p align="center">
  <img src="https://img.shields.io/badge/Made%20with-Flask-blue?logo=flask" alt="Flask Badge"/>
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License Badge"/>
</p>

<h1 align="center">🔗 Shrnk.ly</h1>
<p align="center">
  <em>A sleek and lightweight URL shortener built with Flask and SQLite. Effortlessly transform long links into concise, shareable URLs.</em>
</p>

---

## 🚀 Features

- 🔗 **Generate short URLs** for any long link
- 📊 **Track the number of clicks** for each short URL
- 🗄️ **Store URLs** securely in a local SQLite database
- 🎨 **Simple and clean UI** using Flask templates

---

## 🛠️ Tech Stack

- <b>Backend:</b> Python (Flask)
- <b>Database:</b> SQLite
- <b>Frontend:</b> HTML & CSS

---

## ✅ Prerequisites

- Python 3.x
- Flask
- SQLite3

---

## ⚡ Installation and Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Kirankumarvel/Shrnk.ly.git
   cd Shrnk.ly
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   # On Unix/macOS
   source venv/bin/activate
   # On Windows
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the SQLite database**
   ```bash
   python init_db.py
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser and visit:**
   ```
   http://127.0.0.1:5000
   ```

---

## 📦 Project Structure

```
Shrnk.ly/
├── app.py             # Main application file
├── init_db.py         # Database initialization script
├── requirements.txt   # Python dependencies
├── database.db        # SQLite database
├── templates/         # HTML templates
└── static/            # CSS and other assets
```

---

## 📝 Usage

1. **Enter a long URL** in the input field and click <b>Shorten</b>.
2. **Copy** the generated short URL and share it!
3. **Track** the number of clicks for your shortened link.

---

## 🤝 Contributing

> Contributions are welcome!  
Fork this repository, create a new branch, make your changes, and submit a pull request.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

