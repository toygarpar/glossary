


---

# 📚 Glossary

Welcome to **Glossary**, an English-to-Turkish Computing Terms Dictionary project! 🌟  

This repository provides two Python-based web applications for managing and viewing glossary terms. It leverages **Flask**, **Jinja2 templates**, and **JSON** data files to create a simple yet flexible glossary system.

---

## 📂 Project Structure

```
glossary/
├── data/
│   ├── glossary.json          # Glossary terms database (JSON format)
│   └── backups/               # Auto backups when overwriting glossary items
├── glossary_web_app/
│   ├── static/
│   │   ├── style.css          # Custom CSS for app.py and templates
│   │   └── fancystyle.css     # Default CSS file for fancy_app.py
│   ├── templates/
│   │   ├── index.html         # Main HTML templates for Fancy App
│   │   └── fancy/             # Directory containing Jinja2 HTML template
│   │       └── index.html     # Template for generating glossary pages
│   └── app.py                 # Minimal Flask app for glossary management
├── fancy_app.py               # Flask app rendering static glossary pages
├── .gitignore
└── README.md                  # Project documentation
```

---

## 🚀 Applications Overview

### 🛠️ **app.py**

> **Purpose**: A Python-based web application for managing and displaying glossary terms using Flask.  

#### **Features**:
- Add new glossary entries via a simple form ✏️  
- Search for terms interactively 🔍  
- List all entries 📋  
- Edit/update terms and export glossary data to HTML files 💾  

#### **UI**:
- **Responsive Design**: Ensures the site looks great on all devices (desktop, tablet, mobile) 📱💻  

#### **Target Users**:
- Ideal for users looking for a simple and functional glossary management tool 🧑‍💻  

---

### 🎨 **fancy_app.py**

> **Purpose**: A Jinja2 Flask application that renders a static, searchable glossary page(s).  

#### **Features**:
- Reads glossary terms directly from `data/glossary.json` 📂  
- **Dynamic Content Generation**: Generates static HTML pages from a JSON glossary file 📄  
- **Pagination**: Splits large glossaries(over 100) into multiple pages for better navigation 📃➡️📄  
- **Search Functionality**: Allows users to filter glossary terms dynamically using a search bar 🔍  
- **Static File Handling**: Automatically creates a `static` folder for CSS files if it doesn’t exist 🖼️  
- **Error Handling**: Provides meaningful error messages for missing files or directories ⚠️  

#### **Target Users**:
- Perfect for users who want a visually attractive, easily readable glossary 🌈  

---

## 🎨 Templates & Styling

#### **HTML Templates**:
- Located inside `glossary_web_app/templates/` and `glossary_web_app/fancy/`📁  
- Uses **Jinja2 syntax** for dynamic rendering 🔄  

#### **CSS Styling**:
- Located at `glossary_web_app/static/` 🖼️  
  - `fancy_app.py` uses `fancystyle.css`  
  - `app.py` and templates/ use `style.css`  

#### **Templates**:
-  app.py using `glossary_web_app/templates/` includes the following templates:  
  - `add_term.html`  
  - `base.html`  
  - `delete_confirm.html`  
  - `edit_term.html`  
  - `export_plain.html`  
  - `export_special.html`  
  - `export.html`  
  - `index.html`  
  - `search.html`  
- fancy_app.py uses `glossary_web_app/fancy/index.html`

#### **Design Philosophy**:
- Clean, modern, and responsive user interface 🌟  
- Ensures readability across devices (mobile, tablet, desktop) 📱💻  

---

## 🗃️ Data Storage & Backup

#### **Primary Storage**:
- All glossary terms are stored in `data/glossary.json` 📂  

#### **Backup Features**:
- Backups are saved in `data/backups/` while overwriting terms 🔄  
- Future versions can integrate automatic backup creation (e.g., saving previous versions with timestamps) ⏳  

#### **Data Structure**:
```json
{
  "terms": [
    {
      "name": "term name",
      "definition": "term definition",
      "category": "optional category",
      "created": "timestamp"
    }
  ]
}
```

---

## ⚙️ Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/toygarpar/glossary.git
   cd glossary
   ```

2. **Install Dependencies**:
   ```bash
   pip install flask
   ```

3. **Run the Desired App**:
   - To run the management app:
     ```bash
     python app.py
     ```
   - To run the fancy static page renderer:
     ```bash
     python fancy_app.py
     ```

4. **Open Your Browser**:
   Visit:
   ```
   http://localhost:5000 or http://127.0.0.1:5000/
   ```

---

## 🛠️ Technologies Used

- **Python 3.x** 🐍  
- **Flask** 🌐  
- **HTML5 & CSS3** 🎨  
- **Jinja2** 🔄  
- **JSON** 📂  

---

## 📜 License

This project is open source and available under the **MIT License**.  
Feel free to use, modify, and distribute! 🚀  

---

## 🙏 Acknowledgments

Created by [toygarpar](https://github.com/toygarpar) 👨‍💻  
Designed to make learning and managing computing terms easier for everyone! 🌟  

---

