# County Project Management & Tracking System (PMTS)

A comprehensive Django-based web application for county project management.

## Setup

1. **Install Dependencies**:
   ```bash
   pip install django pillow django-crispy-forms django-filter crispy-bootstrap5
   ```

2. **Initialize Database**:
   ```bash
   python manage.py migrate
   ```

3. **Sample Data** (Optional):
   (Already populated during setup)

4. **Run Server**:
   ```bash
   python manage.py runserver
   ```

## Features
- **User Roles**: Public, Staff, Executive.
- **Projects**: Lifecycle management.
- **Locations**: SubCounty and Ward tracking.
- **Finance**: Budget and Expenditure.
- **Public Portal**: View projects and dashboard.

## Login
- Superuser: `admin` / `admin`
