# Birthday Reminder Application

A simple Flask web application to manage birthday reminders. This application allows users to add new birthdays, view upcoming birthdays, and send WhatsApp birthday wishes directly from the application.

## Features

- View today's birthdays.
- View upcoming birthdays in the next 30 days.
- Add new birthday entries.
- Edit or delete existing birthday entries.
- Send WhatsApp birthday wishes with pre-filled messages.

## Technologies Used

- Python (Flask framework)
- SQLAlchemy (for database management)
- Bootstrap (for styling and responsiveness)
- SQLite (for database)
- WhatsApp API (for sending wishes)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/your-flask-app.git
    cd your-flask-app
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    python app.py
    ```

5. Open your browser and navigate to `http://127.0.0.1:5000` to access the application.

## Project Structure

```plaintext
your-flask-app/
├── static/
│   └── style.css              # CSS for styling the application
├── templates/
│   ├── base.html               # Base template with navigation bar
│   ├── index.html              # Home page to display today's birthdays
│   ├── upcoming_birthdays.html # Displays upcoming birthdays in the next 30 days
│   ├── add_birthday.html       # Form to add a new birthday
│   └── edit_birthday.html      # Form to edit an existing birthday
├── app.py                      # Main Flask application logic
├── models.py                   # Database models using SQLAlchemy
├── requirements.txt            # Python package dependencies
└── README.md                   # This file


## Usage

- **Home Page**: Lists today's birthdays and provides an option to send wishes via WhatsApp.
- **Upcoming Birthdays**: Shows a list of people whose birthdays are coming up within the next 30 days.
- **Add Birthday**: Add a new entry to the birthday database.
- **Edit/Delete Birthday**: Modify or remove an existing entry from the birthday database.

### WhatsApp Integration

When you click the "Send Wishes" button, the app redirects you to WhatsApp with a pre-filled message. Ensure the contact numbers are stored in the database in the correct format (including country code `+91` for India).

