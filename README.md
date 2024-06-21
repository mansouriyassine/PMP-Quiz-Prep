# PMP Quiz Prep

PMP Quiz Prep is a web-based application designed to help aspiring Project Management Professionals (PMP) prepare for their certification exam. The platform offers a comprehensive set of practice questions, progress tracking, and study resources to enhance the learning experience.

## Features

- **Extensive Question Bank**: Access to 1000 PMP exam-style questions.
- **Customized Quiz Sets**: Take quizzes in sets of 25 questions each.
- **Progress Tracking**: Monitor your performance and identify areas for improvement.
- **Detailed Explanations**: Each question comes with thorough explanations for better understanding.
- **User-Friendly Interface**: Intuitive design for seamless navigation and quiz-taking experience.
- **Responsive Design**: Access the platform on various devices - desktop, tablet, or mobile.

## Tech Stack

- Frontend: React.js with Tailwind CSS
- Backend: Flask (Python)
- Database: MongoDB
- Authentication: JSON Web Tokens (JWT)

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Node.js and npm installed
- Python 3.7+ installed
- MongoDB installed and running

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/PMP-Quiz-Prep.git
   cd PMP-Quiz-Prep
   ```

2. Set up the backend:
   ```
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Set up the frontend:
   ```
   cd ../frontend
   npm install
   ```

4. Create a `.env` file in the backend directory with the following content:
   ```
   FLASK_APP=main.py
   FLASK_ENV=development
   MONGODB_URI=your_mongodb_connection_string
   JWT_SECRET_KEY=your_secret_key
   ```

5. Start the backend server:
   ```
   cd ../backend
   flask run
   ```

6. In a new terminal, start the frontend development server:
   ```
   cd ../frontend
   npm start
   ```

7. Open your browser and navigate to `http://localhost:3000` to access the application.

## Usage

1. Register for an account or log in if you already have one.
2. From the dashboard, you can start a new quiz or review your progress.
3. Each quiz consists of 25 questions. Select your answers and submit when done.
4. After completing a quiz, you'll see your score and can review the correct answers.
5. Track your progress over time and focus on areas that need improvement.

## Contributing

Contributions to the PMP Quiz Prep project are welcome. Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/articles/creating-a-pull-request/).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or feedback, please reach out to us at [mansouri.yassine1@gmail.com]

Happy studying and good luck with your PMP certification!