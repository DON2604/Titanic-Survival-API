# Titanic Survival Prediction API 🚢

## Overview

This project implements a Flask API for predicting the survival probability of an individual on the Titanic ship based on features such as Class, Sex, Age, and Fare. The machine learning model used for prediction is a Decision Tree Classifier.

## Project Structure 📂

- `main.py`: Contains the Flask application setup and API endpoint for making predictions.
- `training.py`: Includes the machine learning model training logic using the Titanic dataset.
- `titanic.csv`: Dataset containing information about passengers on the Titanic.

## Usage 🚀

1. Create a virtual environment:

   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:

   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask application using Gunicorn:

   ```bash
   gunicorn main:app
   ```

   The API will be accessible at `http://127.0.0.1:8000/`.
5. Make predictions by sending a GET request to the `/predict` endpoint with the required parameters:

   - Example: `http://127.0.0.1:8000/predict/1.0/1.0/25.0/50.0`

   The API will return a JSON response containing the predicted survival probability.

## API Endpoint

- **Endpoint:** `/predict/<float:a>/<float:b>/<float:c>/<float:d>`
- **Method:** GET
- **Parameters:**
  - `a`: Class (float)
  - `b`: Sex (float)
  - `c`: Age (float)
  - `d`: Fare (float)

## Machine Learning Model

The model is trained using the Decision Tree Classifier on the Titanic dataset. Features such as Class, Sex, Age, and Fare are used to predict the survival probability of an individual.

## Dataset

The Titanic dataset (`titanic.csv`) is used for training the machine learning model. It contains information about passengers, including whether they survived or not.

## Notes

- Missing values in the "Age" column are filled with the mean age.
- The "Sex" column is encoded using Label Encoding.

## Dependencies

- blinker==1.7.0
- click==8.1.7
- Flask==3.0.0
- gunicorn==21.2.0
- itsdangerous==2.1.2
- Jinja2==3.1.2
- joblib==1.3.2
- MarkupSafe==2.1.3
- numpy==1.26.3
- packaging==23.2
- pandas==2.1.4
- python-dateutil==2.8.2
- pytz==2023.3.post1
- scikit-learn==1.3.2
- scipy==1.11.4
- six==1.16.0
- threadpoolctl==3.2.0
- tzdata==2023.4
- Werkzeug==3.0.1

Feel free to explore and enhance the functionality of the API! ⚙️
