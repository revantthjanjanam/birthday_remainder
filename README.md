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
```

## Usage

### Adding a New Birthday
1. Go to the **Add New Birthday** page.
2. Fill in the name, date of birth, and contact details.
3. Submit the form to add the birthday to the database.

### Viewing Today's Birthdays
- The home page displays a list of people whose birthday is today, along with a button to send them a pre-filled WhatsApp message.

### Viewing Upcoming Birthdays
- Navigate to the **Upcoming Birthdays** section to view all the birthdays happening in the next 30 days.

### Editing or Deleting a Birthday
1. Navigate to the **Edit Birthday** section.
2. You can modify the name, phone number, or date of birth of any existing entry, or delete the entry entirely.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
```

This `README.md` includes an overview of the project, installation instructions, a description of the project structure, usage details, and licensing information.
