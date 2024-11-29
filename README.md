# Definity

**Definity** is a web-based dictionary application that fetches word definitions, pronunciations, and audio from the Merriam-Webster API. It provides users a simple and efficient way to look up word meanings. Check out the site [here](https://definity-8.vercel.app/).


## Technologies Used

- **Backend:** Django
- **Frontend:** HTML, CSS (Tailwind CSS)
- **API Integration:** Merriam-Webster Dictionary API
- **Deployment:** Vercel


## Installation and Setup

### Prerequisites

- Python 3.9 or higher
- A Merriam-Webster API key (get yours from [Merriam-Webster Developer Portal](https://dictionaryapi.com/))

### Steps

1. **Clone the Repository**
   
   ```bash
   git clone https://github.com/jadhavanushka/definity.git
   cd definite

2. Set Up a Virtual Environment

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
 
3. Install Dependencies

   ```bash
   pip install -r requirements.txt

4. Set Up Environment Variables Create a .env file in the project's root directory and add your API key:
 
   ```bash
   DICTIONARY_API_KEY=your_merriam_webster_api_key

5. Run Migrations
 
   ```bash
   python manage.py migrate

6. Run the Development Server
 
   ```bash
   python manage.py runserver
   ```
   
   Visit http://127.0.0.1:8000 to view the application.


