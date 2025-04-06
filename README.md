# One Team Stat API

This is the backend API for the **One Team Stat** project, designed for managing football league, club, and match data.  
The API is built with **Django** and **Django REST Framework**.

Visit the project: [One Team Stat Website](https://one-team-stat.onrender.com/)

## 📚 API Endpoints

### Core (Authentication & User Management)

- `POST /api/core/register/` — Register a new user.
- `POST /api/core/login/` — Log in and obtain authentication token.
- `POST /api/core/logout/` — Log out the current user.
- `PUT /api/core/update_info/` — Update user profile information.
- `PUT /api/core/update_password/` — Update user password.
- `GET /api/core/protected/` — Access a protected test route.

---

### Game Core (League Management)

> All endpoints support: **List**, **Retrieve**, **Create**, **Update**, **Delete**.

- `/api/gamecore/league/` — Manage leagues.
- `/api/gamecore/stadium/` — Manage stadiums.
- `/api/gamecore/season/` — Manage seasons.
- `/api/gamecore/club/` — Manage clubs.
- `/api/gamecore/team/` — Manage teams.
- `/api/gamecore/coach/` — Manage coaches.
- `/api/gamecore/player/` — Manage players.
- `/api/gamecore/referee/` — Manage referees.

---

### Games (Match Management)

> All endpoints support: **List**, **Retrieve**, **Create**, **Update**, **Delete**.

- `/api/games/fixtures/` — Manage match fixtures.
- `/api/games/lineups/` — Manage team lineups.
- `/api/games/lineup_players/` — Manage lineup players.
- `/api/games/substitution/` — Manage match substitutions.
- `/api/games/match_officials/` — Manage match officials.
- `/api/games/game_events/` — Manage match events (goals, cards, etc.).
- `/api/games/match_stats/` — Manage match statistics.

---

## ⚙️ Tech Stack

- Django
- Django REST Framework (DRF)
- Gunicorn

---

## 🚀 Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/netsanet-dev/one-team-stat.git
   cd oneteamstat
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional):**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the server with Gunicorn:**
   ```bash
   gunicorn -c gunicorn.conf.py OneTeamStat.wsgi
   ```

---

## 📌 Notes

- All endpoints are **RESTful** and follow **CRUD** operations.
- Authentication is required for protected routes.

---
