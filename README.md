# Giftora

Giftora is a Django-based smart gift recommendation platform that helps users discover suitable gift ideas based on recipient type, occasion, and budget.

## Project Overview

Many users spend time searching for gifts without knowing what to choose. Giftora solves this by providing a guided gift-finding experience and a searchable gift catalog.

## Features

- User Registration and Login
- Personalized Gift Finder
- Explore Gifts Catalog
- Live AJAX Search
- Gift Search API Endpoint
- Trending Gifts Section
- Admin Dashboard for Gift Management
- Responsive User Interface
- MySQL Database Integration

## Technologies Used

- Python
- Django
- HTML
- CSS
- JavaScript
- AJAX
- MySQL
- GitHub
- Trello
- MySQL Workbench

## Main Pages

- Home Page
- Explore Gifts Page
- Find My Gift Page
- About Page
- Login Page
- Register Page

## API Endpoint

```text
/api/gifts/search/?q=keyword
```

This endpoint returns gift data based on gift name, category, occasion, or recipient type.

## Database

The project uses MySQL as the backend database.

Main models:

- Gift
- Recommendation
- Favorite
- User

## Setup Instructions

```bash
git clone <repository-link>
cd giftora

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Future Improvements

- Favorites / Wishlist
- AI Gift Assistant
- Advanced Recommendation Logic
- AWS Deployment
- Seasonal Gift Collections

## Author

Developed by Shaymaa Obaid