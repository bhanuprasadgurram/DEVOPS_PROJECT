# AI Coding Tracker

An interactive coding challenge platform with AI-powered feedback. Practice coding problems and receive instant analysis of your code quality, complexity, and best practices.

## Features

- **Multiple Coding Challenges**: Browse and solve various coding problems
- **AI-Powered Feedback**: Get instant analysis of your code including:
  - Quality score (0-100)
  - Complexity assessment
  - Readability metrics
  - Strengths identification
  - Improvement suggestions
  - Best practices verification
- **Multi-Language Support**: Write solutions in Python, JavaScript, or Java
- **Modern UI**: Clean, responsive interface built with vanilla HTML/CSS/JS
- **RESTful API**: FastAPI backend with comprehensive endpoints
- **Containerized**: Docker-ready for easy deployment

## Project Structure

```
ai-coding-tracker/
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   │   ├── challenges.py       # Challenge endpoints
│   │   │   ├── submissions.py      # Submission endpoints
│   │   │   └── ai_feedback.py      # AI feedback endpoints
│   │   ├── static/
│   │   │   ├── index.html          # Main UI
│   │   │   ├── style.css           # Styling
│   │   │   └── script.js           # Frontend logic
│   │   ├── utils/
│   │   │   └── ai_analyzer.py      # AI analysis logic
│   │   ├── database.py             # In-memory data store
│   │   └── main.py                 # FastAPI application
│   ├── requirements.txt            # Python dependencies
│   └── Dockerfile                  # Backend container config
├── docker-compose.yml              # Docker orchestration
├── README.md                       # This file
└── LICENSE                         # MIT License
```

## API Endpoints

### Challenges
- `GET /api/problems` - List all coding challenges
- `GET /api/problems/{challenge_id}` - Get specific challenge details

### Submissions
- `POST /api/submit` - Submit code solution
  ```json
  {
    "challenge_id": "uuid",
    "code": "your code here",
    "language": "python"
  }
  ```
- `GET /api/submissions/{submission_id}` - Get submission details
- `GET /api/submissions` - List recent submissions

### Feedback
- `POST /api/feedback` - Request AI analysis
  ```json
  {
    "submission_id": "uuid"
  }
  ```
- `GET /api/feedback/{submission_id}` - Get existing feedback

### Health
- `GET /health` - Health check endpoint

## Getting Started

### Prerequisites

- Docker and Docker Compose (recommended)
- OR Python 3.11+ (for local development)

### Option 1: Run with Docker (Recommended)

1. Clone the repository:
```bash
git clone <repository-url>
cd ai-coding-tracker
```

2. Build and start the containers:
```bash
docker-compose up --build
```

3. Access the application:
- Open your browser to http://localhost:8000
- API documentation: http://localhost:8000/docs

4. Stop the application:
```bash
docker-compose down
```

### Option 2: Run Locally (Development)

1. Navigate to the backend directory:
```bash
cd ai-coding-tracker/backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

5. Access the application:
- Open your browser to http://localhost:8000

## Usage

1. **Select a Challenge**: Browse the available coding challenges on the home page
2. **Write Your Solution**: Use the code editor to write your solution in Python, JavaScript, or Java
3. **Submit Code**: Click "Submit Code" to send your solution for analysis
4. **Review Feedback**: View AI-generated feedback including:
   - Overall quality score
   - Code complexity and readability metrics
   - Strengths in your implementation
   - Suggestions for improvement
   - Best practices you've applied
5. **Try Again**: Refine your solution based on feedback and resubmit

## AI Analysis Components

The AI analyzer evaluates code based on:

- **Quality Score**: Overall code quality (0-100)
- **Complexity**: Assessment of algorithmic complexity (low/moderate/high)
- **Readability**: Code clarity and formatting evaluation
- **Strengths**: Positive aspects of your implementation
- **Suggestions**: Actionable improvements for better code
- **Best Practices**: Language-specific conventions followed

## Deployment

### Deploy to Production

1. **Update docker-compose.yml** for production:
   - Remove volume mounts
   - Add environment variables for production settings
   - Configure proper networking and security

2. **Build production images**:
```bash
docker-compose build
```

3. **Deploy to your hosting platform**:
   - AWS ECS/Fargate
   - Google Cloud Run
   - Azure Container Instances
   - DigitalOcean App Platform
   - Or any Docker-compatible hosting

### Environment Variables

No environment variables required for basic operation. The application runs with default settings.

For production, consider adding:
- `DATABASE_URL` - If using external database
- `API_KEY` - For rate limiting or authentication
- `CORS_ORIGINS` - Restrict allowed origins

## Development

### Adding New Challenges

Edit `backend/app/database.py` and add challenges to the `challenges` list:

```python
{
    "id": str(uuid.uuid4()),
    "title": "Your Challenge",
    "description": "Challenge description",
    "difficulty": "easy|medium|hard",
    "test_cases": [
        {"input": "example input", "output": "expected output"}
    ],
    "created_at": datetime.utcnow().isoformat()
}
```

### Customizing AI Analysis

Modify `backend/app/utils/ai_analyzer.py` to adjust:
- Quality scoring algorithm
- Complexity detection patterns
- Best practices checks
- Suggestion generation logic

### Frontend Customization

Edit files in `backend/app/static/`:
- `index.html` - Structure and layout
- `style.css` - Styling and appearance
- `script.js` - Functionality and API interactions

## Technologies Used

- **Backend**: FastAPI (Python)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Containerization**: Docker, Docker Compose
- **API Documentation**: OpenAPI/Swagger (auto-generated)

## License

MIT License - see LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues, questions, or suggestions, please open an issue on the repository.

## Roadmap

- [ ] Add user authentication
- [ ] Implement actual code execution and testing
- [ ] Add more coding challenges
- [ ] Support additional programming languages
- [ ] Integrate advanced AI models for deeper analysis
- [ ] Add leaderboard and user statistics
- [ ] Implement code sharing and collaboration features
