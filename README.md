
# Birthday Reminder Application

This is a Flask-based web application designed to store and manage birthdays, send birthday wishes through WhatsApp, and manage a list of upcoming birthdays.

## Features

- **Add New Birthdays**: Store the name, contact number, and birthdate of individuals.
- **View Today's Birthdays**: Display a list of people whose birthday is today.
- **Send Wishes**: Pre-fill WhatsApp messages to wish the birthday person.
- **Upcoming Birthdays**: View a list of birthdays happening in the next 30 days.
- **Edit and Delete**: Modify or remove existing birthday entries.
  
Here’s how you can format the project structure in your `README.md` file to make it look cleaner and more visually appealing using Markdown:

```markdown
## Project Structure

```
your-flask-app/
├── static/
│   └── **style.css**              # CSS for styling the application
├── templates/
│   ├── **base.html**               # Base template with navigation bar
│   ├── **index.html**              # Home page to display today's birthdays
│   ├── **upcoming_birthdays.html** # Displays upcoming birthdays in next 30 days
│   ├── **add_birthday.html**       # Form to add new birthday
│   └── **edit_birthday.html**      # Form to edit existing birthday
├── **app.py**                      # Main Flask application logic
├── **models.py**                   # Database models using SQLAlchemy
├── **requirements.txt**            # Python package dependencies
└── **README.md**                   # This file
```

This uses **bold** to highlight the important file names and makes the structure clear. You can further customize the descriptions as needed.

## Getting Started

### Prerequisites

Ensure you have Python 3.x and the following packages installed:

- Flask
- SQLAlchemy
- Bootstrap (for styling)
- WhatsApp API integration

You can install the dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Running the Application

1. Clone the repository and navigate to the project folder:
   ```bash
   git clone https://github.com/your-username/birthday-reminder-app.git
   cd birthday-reminder-app
   ```

2. Initialize the SQLite database:
   ```bash
   python app.py init-db
   ```

3. Run the Flask server:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://127.0.0.1:5000`.

### File Upload Issue

If the `style.css` is not loading, ensure the file exists in the `/static` directory and the correct path is referenced in the HTML templates.

### Database

The database is powered by SQLite and managed through SQLAlchemy. To reset the database or view/edit entries, you can modify `models.py` or use Flask-SQLAlchemy commands.

## Usage

- **Home Page**: Lists today's birthdays and provides an option to send wishes via WhatsApp.
- **Upcoming Birthdays**: Shows a list of people whose birthdays are coming up within the next 30 days.
- **Add Birthday**: Add a new entry to the birthday database.
- **Edit/Delete Birthday**: Modify or remove an existing entry from the birthday database.

### WhatsApp Integration

When you click the "Send Wishes" button, the app redirects you to WhatsApp with a pre-filled message. Ensure the contact numbers are stored in the database in the correct format (including country code `+91` for India).

