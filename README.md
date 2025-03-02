# Workout Tracker

This Python project uses the **Nutritionix API** to analyze workout details based on user input through an LLM (Large Language Model). The gathered workout data, including exercise name, duration, and calories burned, is then stored in a **Google Sheets** document via the Sheety API for tracking workouts over time.

## Features

- Uses **Natural Language Processing (NLP)** to interpret workout details from user input.
- Fetches workout **name, duration, and calories burned** from the **Nutritionix API**.
- Stores workout data in a **Google Sheets document** using the **Sheety API**.
- Securely manages API keys using **environment variables**.

## Setup Instructions

### 1. Prerequisites

- Python 3.x installed
- A **Nutritionix** account to obtain API credentials
- A **Google Sheets document** linked to Sheety for data storage
- A GitHub repository (optional, for version control)

### 2. Install Dependencies

Ensure you have `requests` and `dotenv` installed:

```bash
pip install requests python-dotenv
```

### 3. Configure Environment Variables

Create a `.env` file in the project directory and store API credentials:

```
APP_ID=your_nutritionix_app_id
API_KEY=your_nutritionix_api_key
SHEETS_URL=your_google_sheets_url
TOKEN=your_sheety_api_token
```

### 4. Running the Script

Run the script from the terminal:

```bash
python main.py
```

Then, input your workout details when prompted.

### 5. Example Usage

```bash
Tell me which exercises you did: I ran for 30 minutes
```

The script will then fetch exercise details and store them in your Google Sheets.

## API References

- **Nutritionix API**: [https://www.nutritionix.com/business/api](https://www.nutritionix.com/business/api)
- **Sheety API**: [https://sheety.co/](https://sheety.co/)

## Security Best Practices

- **Never hardcode API keys in your script**. Always use environment variables.
- Add `.env` to `.gitignore` before pushing to GitHub:
  ```
  .env
  ```

## Future Improvements

- Add a **Flask/Django web interface** to visualize workout history.
- Implement **authentication** for multiple users.
- Enable **data analysis** for workout trends and progress tracking.

## License

This project is open-source and available under the **MIT License**.

---

Feel free to contribute to the project by submitting a pull request!

