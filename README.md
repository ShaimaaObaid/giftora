# Giftora

Giftora is a Django-based smart gift recommendation platform that helps users discover thoughtful gift ideas based on recipient type, occasion, and budget.

## Project Overview

Choosing the right gift can be difficult and time-consuming. Giftora simplifies the process by providing personalized recommendations and a searchable gift catalog that helps users quickly find suitable gift ideas.

## Features

* User Registration and Login
* Personalized Gift Finder
* Explore Gifts Catalog
* Live AJAX Search
* Gift Search API Endpoint
* Trending Gifts Section
* Admin Dashboard for Gift Management
* Responsive User Interface
* MySQL Database Integration

## Technologies Used

* Python
* Django
* HTML5
* CSS3
* JavaScript
* AJAX
* MySQL
* Git & GitHub
* Trello
* MySQL Workbench

## Main Pages

* Home Page
* Explore Gifts Page
* Find My Gift Page
* About Page
* Login Page
* Register Page

## API Endpoint

```text
/api/gifts/search/?q=keyword
```

This endpoint returns gift data based on gift name, category, occasion, or recipient type.

## Database

The project uses MySQL as the backend database.

### Main Models

* User
* Gift
* Recommendation
* Favorite

## Project Assets

* ERD Diagram (MySQL Workbench)
* Home Wireframe
* Explore Gifts Wireframe
* Find My Gift Wireframe
* About Wireframe

## Setup Instructions

```bash
git clone https://github.com/ShaimaaObaid/giftora.git

cd giftora

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
```

## Future Improvements

* Favorites / Wishlist Feature
* AI Gift Assistant
* Advanced Recommendation Logic
* Seasonal Gift Collections
* User Gift History
* AWS Deployment

## Author

Developed by Shaymaa Obaid
