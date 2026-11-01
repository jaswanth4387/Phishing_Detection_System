# 🔐 Phishing Detection System

A Django web application that classifies URLs as **phishing** or **legitimate** using a machine learning model, with **role-based access control (RBAC)** separating regular users from providers/admins. Providers get an analytics dashboard and can retrain the model from the browser.

**Live demo:** https://phishing-detection-system-rujb.onrender.com

---

## ✨ Features

### For users
- Register, log in, and manage a profile
- Paste any URL and get an instant **Phishing URL / Legitimate URL** verdict
- Every prediction is saved to the database against the user

### For providers / admins
- Separate admin login at `/adminlogin/`
- **Dashboard** with total users, total predictions, and phishing ratio
- **Users** and **Predictions** views (all users, newest first)
- **Analytics:** phishing-vs-safe ratio, charts (Chart.js), and model accuracy page
- **Train Model** button that re-runs the training pipeline and refreshes the model files

### Access control
- Provider-only pages are guarded by an `is_provider` check (superuser or member of the `provider` group)
- Custom permissions defined in `AdminControl`: `can_train_model`, `can_view_dashboard`, `can_view_users`, `can_view_predictions`, `can_view_analytics`
- After login, users are redirected by role (providers → dashboard, users → profile)

---

## 🧠 How the ML works

| Step | Detail |
|------|--------|
| Dataset | `ml_model/dataset/dataset.csv`, about 549K labelled URLs (~393K `good`, ~156K `bad`) |
| Features | Bag-of-words over the raw URL string, using `CountVectorizer(max_features=5000)` |
| Model | `LogisticRegression(max_iter=1000)` |
| Split | 80/20 train/test, `random_state=42` |
| Output | Pickled `model.pkl` and `vectorizer.pkl` in `ml_model/model/` |
| Inference | `ml_model/predict.py` loads both pickles once and exposes `predict_url(url)` |

Labels are mapped `bad → 1 (Phishing URL)` and `good → 0 (Legitimate URL)`.

To retrain from the command line:

```bash
python ml_model/train.py
```

The script prints the held-out test accuracy when it finishes.

---

## 🛠 Tech Stack

- **Backend:** Python, Django 5.2
- **ML:** scikit-learn, pandas, numpy, joblib
- **Frontend:** HTML, CSS, JavaScript, Chart.js
- **Database:** SQLite (local); `psycopg2-binary` is included for PostgreSQL
- **Deployment:** Gunicorn + WhiteNoise (Render-ready via `Procfile`)

---

## 📁 Project Structure

```
phishing_detection_system/
├── core/                 # Project settings, root URLs, WSGI/ASGI
├── client_portal/        # User-facing app: auth, profile, predict, Prediction model
├── admin_dashboard/      # Provider app: dashboard, analytics, training, RBAC helpers
│   ├── rbac.py           # is_provider / is_user checks
│   └── models.py         # AdminControl (custom permissions)
├── ml_model/
│   ├── dataset/          # Training data (CSV)
│   ├── model/            # Saved model.pkl + vectorizer.pkl
│   ├── train.py          # Training pipeline
│   └── predict.py        # Inference helper
├── templates/            # base, client/, admin/ pages
├── static/               # CSS and JS per page
├── requirements.txt
├── Procfile              # web: gunicorn core.wsgi
└── manage.py
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- pip

### Installation

```bash
# 1. Clone
git clone https://github.com/jaswanth4387/Phishing_Detection_System.git
cd Phishing_Detection_System

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Create a superuser (acts as a provider/admin)
python manage.py createsuperuser

# 6. Run the server
python manage.py runserver
```

Open http://127.0.0.1:8000/.

> **Running locally:** `ALLOWED_HOSTS` in `core/settings.py` currently lists only the production host. Add `'127.0.0.1'` and `'localhost'` if you get a "DisallowedHost" error with `DEBUG = False`.

### Creating a provider account
Either log in with a superuser, or create a group named `provider` in the Django admin (`/admin/`) and add the user to it. Providers log in at `/adminlogin/`.

---

## 🗺 URL Reference

| Route | Access | Purpose |
|-------|--------|---------|
| `/` | Public | Landing page |
| `/register/`, `/login/` | Public | User signup and login |
| `/adminlogin/` | Public (provider credentials) | Provider login |
| `/predict/` | Logged-in | URL phishing check |
| `/profile/` | Logged-in | User profile |
| `/dashboard/` | Provider | Stats overview |
| `/users/`, `/predictions/` | Provider | User and prediction lists |
| `/ratio/`, `/charts/`, `/accuracy/` | Provider | Analytics |
| `/train/` | Provider | Retrain the model |
| `/admin/` | Superuser | Django admin |

---

## ⚠️ Known Limitations & Roadmap

- [ ] **Forgot password / OTP / reset flow** has routes and templates, but is not yet implemented
- [ ] **Accuracy page** shows a static placeholder value; wire it to the real test accuracy from training
- [ ] Move secrets (`SECRET_KEY`, email credentials) and `DEBUG` to **environment variables**
- [ ] Add unit tests for prediction, RBAC, and views
- [ ] Richer features (URL length, special characters, domain age, TLD) and model comparison (Random Forest, XGBoost)
- [ ] REST API endpoint for programmatic URL checks

---
<!--
## 🤝 Contributing

1. Fork the repo
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit and push your changes
4. Open a Pull Request

---
-->
## 👤 Author

**Jakkampudi Jaswanth Krishna**
GitHub: [@jaswanth4387](https://github.com/jaswanth4387)

---


