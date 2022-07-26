# News manager  [![Django][django]][django-url]

A Django-based website to manage news articles or blog posts.

<details>
  <summary>Contents</summary>
  <ol>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#installation">Installation</a></li>
  </ol>
</details>

## Usage

On the home page, the user can select which article to read based on its headline and a short preview.

<div align='center'>
 <img src="https://github.com/juanpablosalas/django-news-manager/blob/main/screenshots/home-page.png" alt="News manager home page preview" height="300px">
</div>

The user can add news articles using the "+" symbol located in the home page. This will redirect them to 

<div align='center'>
 <img src="https://github.com/juanpablosalas/django-news-manager/blob/main/screenshots/add-page.png" alt="News manager add page preview" height="300px">
</div>

The user can click on each article to see a detailed version of it. They can choose to edit or delete the article.

<div align='center'>
 <img src="https://github.com/juanpablosalas/django-news-manager/blob/main/screenshots/detail-page.png" alt="News manager detail page preview" height="300px">
</div>

When the user tries to delete an article, a confirmation message appears.

<div align='center'>
 <img src="https://github.com/juanpablosalas/django-news-manager/blob/main/screenshots/delete-warning.png" alt="News manager delete page preview" height="300px">
</div>

## Getting started

### Prerequisites

* Django
* Python

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/juanpablosalas/django-news-manager.git
   ```
2. Run the developer server
   ```sh
   python manage.py runserver
   ```


[django]: https://www.djangoproject.com/m/img/badges/djangomade124x25.gif
[django-url]: http://www.djangoproject.com/
