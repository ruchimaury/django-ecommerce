# Django Ecommerce Assignment

##  Overview
This is a simple ecommerce web app built using Django and Stripe (test mode).

Users can:
- View products
- Select quantity
- Make payment using Stripe
- View paid orders on the same page

---

##  Tech Stack
- Django
- SQLite (can be replaced with Postgres)
- Stripe (test mode)
- HTML + Bootstrap

---

##  Flow
- User selects product and quantity
- Order is created (unpaid)
- User is redirected to Stripe Checkout
- After successful payment, order is marked as paid
- Paid order is shown in "My Orders"

---

##  Payment Integration
- Used Stripe Checkout (test mode)
- Test card: 4242 4242 4242 4242

---

##  Handling Double Payment
- Order is marked as paid only once
- Added check to avoid duplicate updates on refresh

---

##  Setup Instructions

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Screenshot

<img width="1876" height="803" alt="image" src="https://github.com/user-attachments/assets/df43a11d-f910-496c-a4b4-8bb55b63233c" />
