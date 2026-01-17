# MOV - Movie Management System

A comprehensive movie management web application built with Django (Python) that allows users to browse, search, and manage movie collections with an elegant and responsive interface.

## 🌟 Features


* Browse and search movie collections
* Dynamic movie grid layout with responsive design
* Movie details with poster images
* Admin panel for content management
* Database-driven movie catalog
* Template-based rendering system
* Static file management for images and assets
* User-friendly navigation and interface

## 🖥️ How to Use

1. Clone the repository:
```bash
   git clone https://github.com/yourusername/mov.git
```

2. Open the folder:
```bash
   cd mov
```



3. Run database migrations:
```bash
   python manage.py migrate
```

4. Create a superuser (admin):
```bash
   python manage.py createsuperuser
```

5. Run the development server:
```bash
   python manage.py runserver
```

6. Open your browser and navigate to:
```
   http://127.0.0.1:8000/
```

## 💡 Project Structure
```
mov/
│
├── movies/                 # Main app directory
│   ├── migrations/         # Database migrations
│   ├── static/            # Static files (CSS, JS, images)
│   ├── templates/         # HTML templates
│   │   ├── about.html
│   │   ├── bases.html
│   │   ├── Collection.html
│   │   ├── contact.html
│   │   ├── home.html
│   │   └── login.html
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── urls.py            # URL routing
│   ├── forms.py           # Form definitions
│   └── tests.py           # Unit tests
│
├── posters/               # Movie poster images
├── wsgi.py               # WSGI configuration
├── manage.py             # Django management script
├── admin.py              # Admin panel configuration
├── apps.py               # App configuration
├── db.sqlite3            # SQLite database
└── requirements.txt      # Python dependencies
```

## 🎬 Features Implemented

* **Home Page** - Landing page with featured movies
* **Collection** - Browse all movies with grid layout
* **About** - Information about the platform
* **Contact** - Contact form and information

* **Admin Panel** - Manage movies, users, and content
* **Responsive Design** - Mobile-friendly interface with animations
* **Dynamic Content** - Database-driven movie listings

## 🔧 Technologies Used

* **Backend**: Django (Python)
* **Frontend**: HTML5, CSS3, JavaScript
* **Database**: SQLite3
* **Template Engine**: Django Templates
* **Static Files**: Django Static Files Management
* **Authentication**: Django Auth System

## 📊 Database Models

* User authentication and profiles
* Movie information (title, description, poster, release date)
* Categories and genres
* User ratings and reviews (if implemented)

## 🎨 Frontend Features

* Perspective wrapper animations
* Grid-based movie layout
* Responsive column design
* Image lazy loading
* Smooth transitions and animations
* Mobile-optimized navigation

## 🔐 Admin Access

Access the admin panel at:
```
http://127.0.0.1:8000/admin/
```
Use the superuser credentials created during setup.

## 📄 License

This project is open source and available for educational and personal use.
