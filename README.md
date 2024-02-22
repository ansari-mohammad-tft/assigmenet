# Wikipedia Word Frequency API

This Django project provides an API for performing word frequency analysis on Wikipedia articles and retrieving search history.

## Setup Instructions

1. **Clone the repository:**
   
   git clone <repository-url>
   cd <repository-directory>

2 **Create and activate a virtual environment**

    python -m venv venv
    source venv/bin/activate   # On Windows: .\venv\Scripts\activate
    
3 **Install dependencies**

   pip install -r requirements.txt
   
4 **Run migrations:**

   python manage.py makemigrations
   python manage.py migrate
   
5 **Start the development server**

   python manage.py runserver

**Endpoints**
**API docs**

URL: /docs/

**Word Frequency Analysis Endpoint**

URL: /top-words/

Method: POST

Parameters:

topic (string, required): The subject of a Wikipedia article.

n (integer, required): Number of top frequent words to return.

Example Request:curl -X POST http://localhost:8000/top-words/ -d "topic=Python programming&n=5"

**Example Response:**

  {
  "topic": "Python programming",
  "n": 5,
  "top_words": [
    {"word": "python", "count": 20},
    {"word": "programming", "count": 15},
    ...
  ]
}


**Search History Endpoint**

  URL: /search-history/
  
Method: GET

Example Request:curl http://localhost:8000/search-history/

**Example Response:**
[
  {
    "topic": "Python programming",
    "n": 5,
    "top_words": [
      {"word": "python", "count": 20},
      {"word": "programming", "count": 15},
      ...
    ],
    "created_at": "2024-02-22T12:30:45Z"
  },
  {
    "topic": "Machine learning",
    "n": 3,
    "top_words": [
      {"word": "machine", "count": 18},
      {"word": "learning", "count": 12},
      ...
    ],
    "created_at": "2024-02-21T14:20:10Z"
  }
]

**Testing**

To run tests, use the following command:
python manage.py test







