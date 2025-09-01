**Auto News Fetcher & Dashboard (project 2)**
This is Django based project which fetched news via newsapi module by creating news API.

**Set_Up Instructions:**
## Setup Instructions

Follow these steps to set up and run the project locally.

1.  Clone the repository:
    ```bash
    git clone (https://github.com/AAMENA123/Auto-News-Fetcher-Dashboard/edit/main/README.md)
    cd Auto-News-Fetcher-Dashboard
    ```

2.  Create and activate a virtual environment:
    ```bash
    # Create the virtual environment
    python -m venv venv

    # Activate on Windows
    venv\Scripts\activate

    # Activate on macOS/Linux
    source venv/bin/activate
    ```

3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4.  Apply database migrations:
    ```bash
    python manage.py migrate
    ```

5.  Run the development server:
    ```bash
    python manage.py runserver
    ```
    Open your web browser and go to `http://127.0.0.1:8000/` to see the application.

---

** Brief explanation of my solution**
Backend: A Django model named `NewsArticle` is used to store headlines with its metadata in a SQLite database. The application fetches news using public newsapi, ensuring that duplicate articles are not saved.
Frontend: The dashboard is a simple Django template styled with Bootstrap. It displays the fetched articles and includes a button to manually trigger a fetch for the latest news.
