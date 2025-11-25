📘 Recipe Management Web Application

A full-stack Django + Django REST Framework application for creating, updating, browsing, and managing recipes with images, difficulty levels, and detailed descriptions.

🚀 Features
🧁 Recipe Management

Create new recipes with:

Name
Preparation time
Difficulty (Easy / Medium / Hard)
Vegetarian / Non-vegetarian
Image Upload
Description (auto-parsed into ingredients)

✏️ Update & Delete Recipes

Edit any recipe through an interactive HTML form
Upload new images or keep existing ones
Soft error handling (recipe not found, invalid form)

🔍 Search Functionality

Search recipes by name (case-insensitive)
Works from the home page

📄 Pagination

Home page lists recipes with pagination (6 per page)

🖼️ Image Handling

Images saved inside /media/recipe/
Displayed in both templates and API responses

🔌 REST API Endpoints (Django REST Framework)

GET /api/recipes/ → List all recipes
POST /api/recipes/ → Create a recipe
GET /detail/<id>/ → Retrieve
PUT /update/<id>/ → Update
DELETE /delete/<id>/ → Delete
GET /search/<name>/ → Search

API returns absolute URLs for images.

🎨 Frontend Templates

Responsive HTML templates
Custom CSS styling

Pages:

Home page (index)
Create recipe
Update recipe
Fetch single recipe details

🏗️ Project Structure
recipe_project/

│
├── assets/

├── media/

│   └── recipe/
│
├── recipe_project/

│   ├── settings.py

│   ├── urls.py

│   └── ...
│
├── rest_app/
│   ├── admin.py

│   ├── apps.py

│   ├── forms.py

│   ├── models.py

│   ├── serializers.py

│   ├── urls.py

│   ├── views.py

│   ├── migrations/

│   ├── media/

│   └── templates/
│       ├── base.html

│       ├── index.html

│       ├── create_recipe.html

│       ├── recipe_update.html

│       └── recipe_fetch.html
│
├── static/
│   └── css/

│       └── style.css
│
└── manage.py

⚙️ Installation & Setup
1. Clone the Repository
git clone <your-repository-url>
cd recipe_project

2. Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Install Dependencies
pip install -r requirements.txt

4. Run Migrations
python manage.py makemigrations
python manage.py migrate

5. Create Superuser (Optional)
python manage.py createsuperuser

6. Run the Server
python manage.py runserver


Visit:
http://127.0.0.1:8000/
 – Home page
http://127.0.0.1:8000/api/recipes/
 – API endpoint

🌄 Image Uploads

Ensure media/ directory exists.
In settings.py:

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


In project urls.py:

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

🔧 Tech Stack

Python 3.x
Django
Django REST Framework
HTML, CSS

Mysql

🧪 Future Enhancements

Add user authentication (login/register)
Allow users to rate recipes
Add categories/cuisines
Convert description into markdown
Add API authentication

🤝 Contributing

Pull requests are welcome!
If you want to make major changes, please open an issue first.

📜 License

This project is open-source and available under the MIT License.
