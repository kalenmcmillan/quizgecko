# QuizGecko API Wrapper

A clean Python client for the [QuizGecko API](https://quizgecko.com/api).   Supports quiz generation, uploads, questions, and language listing.

## Installation

```
pip install quizgecko
```

## Quickstart

```python
from quizgecko import Client, BearerAuth, endpoints

# Initialize
client = Client(BearerAuth('YOUR_API_KEY'))

# Create a quiz
quiz = endpoints.generate.create_quiz(
    client,
    text = 'Physics is the study of matter, energy, and their interactions.',
    question_type = 'multiple_choice',
    difficulty = 'easy'
)

# Wait until processing finishes
completed = endpoints.generate.wait_for_completion(client, quiz['quiz']['id'])

# View generated questions
for question in completed['questions']:
    print(question['text'])
````

## Endpoints

| Module                | Description                          |
| --------------------- | ------------------------------------ |
| `endpoints.generate`  | Create and poll quiz generation jobs |
| `endpoints.quiz`      | Retrieve and update quizzes          |
| `endpoints.questions` | Update individual questions          |
| `endpoints.upload`    | Upload files for content generation  |
| `endpoints.languages` | List supported languages             |

## Development

```
git clone https://github.com/kalenmcmillan/quizgecko.git
cd quizgecko
python -m pip install -e .
pytest
```

## License

MIT License © 2025 Kalen McMillan
