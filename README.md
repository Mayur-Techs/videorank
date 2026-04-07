VideoRank — YouTube Data Intelligence Tool


VideoRank is a backend-driven system that extracts, processes, and ranks YouTube video data to identify high-performing and low-competition content opportunities.

⚙️ Features
- Custom YouTube data extraction without official API
- Modular scraping and data processing pipeline
- Scoring and ranking algorithm for content evaluation
- Multiple analysis modes (best, trending, opportunity)
- REST API built with FastAPI
- CSV export for downstream usage
- Responsive frontend interface
- Containerized setup using Docker

Engineering Focus:
- Backend system design and modular architecture
- Data extraction and processing pipelines
- API development and structured responses
- Automation-ready workflows
- Clean and maintainable code structure


🧱 Tech Stack
Python
FastAPI
yt-dlp
HTML/CSS/JS
Docker

📦 Installation
git clone <repo>
cd videorank
pip install -r requirements.txt
uvicorn src.api:app --reload

🐳 Docker
docker build -t videorank .
docker run -p 8000:8000 videorank

🔗 API Endpoints
/search
/health

📸 Screenshots
### Home Page
![Home](assets/home.png)

### Results Page
![Results](assets/results.png)

🌐 Live Demo
render - https://youtube-scraper-mxsc.onrender.com/
website - https://videorank.netlify.app/