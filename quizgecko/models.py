# src/quizgecko/models.py
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Answer:
    """Represents an individual answer option for a question.

    Attributes:
        id: Unique identifier for the answer.
        question_id: ID of the related question.
        text: The displayed answer text.
        correct: True if this answer is correct.
    """
    id: int
    question_id: int
    text: str
    correct: bool

    @staticmethod
    def from_json(data: Dict[str, Any]) -> 'Answer':
        """Convert a raw API dictionary into an Answer instance."""
        return Answer(
            id = int(data.get('id')),
            question_id = int(data.get('question_id')),
            text = str(data.get('text') or ''),
            correct = bool(data.get('correct', False))
        )


@dataclass
class Question:
    """Represents a question within a quiz.

    Attributes:
        id: Unique identifier for the question.
        quiz_id: ID of the quiz this question belongs to.
        type: Question type (multiple_choice, fill_in_the_blank, etc.).
        text: The question text.
        info: Optional extra information or context.
        answers: List of associated Answer objects.
    """
    id: int
    quiz_id: int
    type: str
    text: str
    info: Optional[str]
    answers: List[Answer]

    @staticmethod
    def from_json(data: Dict[str, Any]) -> 'Question':
        """Convert a raw API dictionary into a Question instance."""
        answers = [Answer.from_json(answer) for answer in data.get('answers', [])]
        return Question(
            id = int(data.get('id')),
            quiz_id = int(data.get('quiz_id')),
            type = str(data.get('type') or ''),
            text = str(data.get('text') or ''),
            info = data.get('info'),
            answers = answers
        )


@dataclass
class Quiz:
    """Represents a complete quiz object returned by the QuizGecko API.

    Attributes:
        id: Unique identifier for the quiz.
        title: Title of the quiz.
        slug: Slug or URL-friendly identifier.
        description: Description or summary text.
        status: Processing status (e.g., 'processing', 'completed').
        language: ISO language code of the quiz.
        url: Public web URL of the quiz.
        questions: List of Question objects belonging to this quiz.
    """
    id: int
    title: Optional[str]
    slug: Optional[str]
    description: Optional[str]
    status: str
    language: Optional[str]
    url: Optional[str]
    questions: List[Question]

    @staticmethod
    def from_json(data: Dict[str, Any]) -> 'Quiz':
        """Convert a raw API dictionary into a Quiz instance."""
        questions = [Question.from_json(question) for question in data.get('questions', [])]
        return Quiz(
            id = int(data.get('id')),
            title = data.get('title'),
            slug = data.get('slug'),
            description = data.get('description'),
            status = str(data.get('status') or ''),
            language = data.get('language'),
            url = data.get('url'),
            questions = questions
        )
