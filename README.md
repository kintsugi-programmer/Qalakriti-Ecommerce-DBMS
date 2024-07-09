# QalaKriti Project README

## Overview
QalaKriti is a web application aimed at showcasing and selling handicrafts from artisans worldwide. It provides a platform where craftsmen can display their work and users can browse and purchase products.

## Features
- **Homepage**: Includes information about the platform and a call-to-action for shopping.
- **Authentication**: Login and registration functionalities for users.
- **Product Listings**: Displays various categories of handicrafts with images and descriptions.
- **Product Pages**: Detailed pages for each product with specifications and the option to purchase.
- **Responsive Design**: Ensures compatibility across various devices.

## Technologies Used
- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Python, Flask framework
- **Database**: MySQL
- **Deployment**: Deployed using a web server (specifics may vary)

## Setup Instructions
1. **Clone the Repository**: `git clone [repository_url]`
2. **Database Setup**: Configure MySQL database credentials in `config.py`.
3. **Run the Application**: `python app.py`
4. **Access the Application**: Open your browser and go to `http://localhost:5000`

## Directory Structure
```
QalaKriti/
│
├── static/
│   ├── assets/
│   │   ├── dist/
│   │   │   ├── css/
│   │   │   │   └── bootstrap.min.css
│   │   │   └── js/
│   │   │       └── bootstrap.bundle.min.js
│   │   └── img_html/
│   │       ├── coverpage.png
│   │       └── qalalogo.png
│   ├── coverpage.css
│   └── ...
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── registration.html
│   └── ...
│
├── app.py
├── config.py
└── README.md
```