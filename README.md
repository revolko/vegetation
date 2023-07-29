# Vegetation
Simple Django app to help you manage your vegetation

## Installation
1. Create a virtual environment
    ```bash
    python3 -m venv venv
    ```
2. Activate the virtual environment
    ```bash
    source venv/bin/activate
    ```
3. Install the requirements
    ```bash
    pip install -r requirements.txt
    ```
4. Run the migrations
    ```bash
    python manage.py migrate
    ```
5. Run the server
    ```bash
    python manage.py runserver
    ```

## TODO
- [ ] Add email notifications (possibly using APScheduler)
- [ ] Add user authentication
- [ ] Add tests
- [ ] Add CI/CD
- [ ] Add Dockerfile
- [ ] Add Docker-compose
- [ ] Add Postgres support
- [ ] Add swagger documentation
