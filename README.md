# 🎯 MyToDo — Flask ToDo Web App

A minimalist and responsive ToDo list web application built with **Flask**, **SQLite**, **SQLAlchemy**, and **Bootstrap 5**.

> 🔧 Easily Add, ✅ View, 🔄 Update, and 🗑️ Delete your daily tasks!



## 📦 Features

- ➕ Add new tasks with title & description  
- ✅ View all your ToDos  
- ✏️ Update any task details  
- ❌ Delete completed/unwanted tasks  
- 🕒 Automatically timestamps your ToDos  
- 🎨 Clean Bootstrap UI  



## 🛠 Tech Stack

- **Backend**: Flask, SQLAlchemy  
- **Database**: SQLite  
- **Frontend**: HTML, Jinja2, Bootstrap 5  
- **Templating Engine**: Jinja2  



## 📂 Folder Structure



mytodo/<br>
├── app.py<br>
├── instance/<br>
│   ├── todo.db  # will be create after running init_db.py<br>
├── templates/<br>
│   ├── base.html<br>
│   ├── index.html<br>
│   └── update.html<br>
├── init_db.py<br>
└── README.md




## 🚀 Getting Started

### 1. 🧰 Prerequisites

- Python 3.x installed
- pip installed

### 2. 🔧 Installation

```bash
git clone https://github.com/Ishu6129/mytodo.git
cd mytodo

# (Optional) create and activate virtual environment
python -m venv venv
source venv/bin/activate    # Windows

# Install dependencies
pip install flask flask_sqlalchemy
````



## 🗃️ Database Setup

In Python shell or a separate file (like `init_db.py`):

```python
from app import app, db

with app.app_context():
    db.create_all()
```

---

## ▶️ Run the App

```bash
python app.py
```

Visit in browser: [http://127.0.0.1:5000](http://127.0.0.1:5000)


## 💡 Example Usage

* Add a new task with title & description
* View all your tasks in a table
* Click **Update** to edit title/desc
* Click **Delete** to remove task

## 🙌 Acknowledgements

* [Flask](https://flask.palletsprojects.com/)
* [Bootstrap](https://getbootstrap.com/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Jinja2](https://jinja.palletsprojects.com/)

