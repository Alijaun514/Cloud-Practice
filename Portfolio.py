# portfolio.py
from flask import Flask, render_template_string

app = Flask(__name__)

# ────────────────────────────────────────────────
#   All HTML + CSS + minimal JS in one place
# ────────────────────────────────────────────────

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{{ name }} • Student Portfolio</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>
  <style>
    :root {
      --primary: #6366f1;
      --primary-dark: #4f46e5;
      --text: #1e293b;
      --text-light: #64748b;
      --bg: #f8fafc;
      --card: #ffffff;
    }

    * { margin:0; padding:0; box-sizing:border-box; }
    body {
      font-family: system-ui, -apple-system, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.6;
    }

    .container { max-width: 1100px; margin: 0 auto; padding: 0 1.5rem; }

    /* ─── Header / Hero ─── */
    header {
      background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
      color: white;
      padding: 8rem 0 6rem;
      text-align: center;
    }

    header h1 {
      font-size: 3.5rem;
      margin-bottom: 0.5rem;
    }

    header .subtitle {
      font-size: 1.4rem;
      opacity: 0.9;
      margin-bottom: 2rem;
    }

    .social-links a {
      color: white;
      font-size: 1.8rem;
      margin: 0 0.8rem;
      transition: 0.3s;
    }
    .social-links a:hover { transform: translateY(-4px); opacity: 0.85; }

    /* ─── Sections ─── */
    section {
      padding: 5rem 0;
    }

    h2 {
      text-align: center;
      font-size: 2.5rem;
      margin-bottom: 3rem;
      color: var(--primary-dark);
    }

    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 2rem;
    }

    .card {
      background: var(--card);
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 10px 30px rgba(0,0,0,0.08);
      transition: all 0.3s ease;
    }

    .card:hover {
      transform: translateY(-8px);
      box-shadow: 0 20px 40px rgba(0,0,0,0.12);
    }

    .card img {
      width: 100%;
      height: 220px;
      object-fit: cover;
    }

    .card-content {
      padding: 1.8rem;
    }

    .card h3 {
      margin-bottom: 0.8rem;
      color: var(--primary-dark);
    }

    .tags {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      margin-top: 1rem;
    }

    .tag {
      background: #e0e7ff;
      color: var(--primary-dark);
      padding: 0.35rem 0.9rem;
      border-radius: 30px;
      font-size: 0.85rem;
    }

    /* About & Contact */
    .about-text {
      max-width: 700px;
      margin: 0 auto 2rem;
      font-size: 1.15rem;
      text-align: center;
    }

    .contact-links {
      text-align: center;
      margin-top: 2.5rem;
    }

    .btn {
      display: inline-block;
      background: var(--primary);
      color: white;
      padding: 0.9rem 2rem;
      border-radius: 50px;
      text-decoration: none;
      font-weight: 600;
      margin: 0.5rem;
      transition: 0.3s;
    }

    .btn:hover {
      background: var(--primary-dark);
      transform: translateY(-2px);
    }

    footer {
      background: var(--text);
      color: white;
      text-align: center;
      padding: 3rem 0;
      margin-top: 4rem;
    }

    @media (max-width: 640px) {
      header h1 { font-size: 2.6rem; }
      header { padding: 6rem 0 4rem; }
      h2 { font-size: 2rem; }
    }
  </style>
</head>
<body>

<header>
  <div class="container">
    <h1>{{ name }}</h1>
    <div class="subtitle">{{ title }}</div>
    <div class="social-links">
      {% if github %}<a href="{{ github }}" target="_blank"><i class="fab fa-github"></i></a>{% endif %}
      {% if linkedin %}<a href="{{ linkedin }}" target="_blank"><i class="fab fa-linkedin"></i></a>{% endif %}
      {% if twitter %}<a href="{{ twitter }}" target="_blank"><i class="fab fa-twitter"></i></a>{% endif %}
      {% if email %}<a href="mailto:{{ email }}"><i class="fas fa-envelope"></i></a>{% endif %}
    </div>
  </div>
</header>

<section id="about">
  <div class="container">
    <h2>About Me</h2>
    <p class="about-text">{{ about|safe }}</p>
  </div>
</section>

<section id="projects" style="background:#f1f5f9;">
  <div class="container">
    <h2>Projects</h2>
    <div class="grid">
      {% for project in projects %}
      <div class="card">
        {% if project.image %}
        <img src="{{ project.image }}" alt="{{ project.title }}">
        {% endif %}
        <div class="card-content">
          <h3>{{ project.title }}</h3>
          <p>{{ project.description }}</p>
          <div class="tags">
            {% for tag in project.tags %}
            <span class="tag">{{ tag }}</span>
            {% endfor %}
          </div>
          {% if project.link %}
          <a href="{{ project.link }}" target="_blank" class="btn" style="margin-top:1.2rem;">View Project →</a>
          {% endif %}
        </div>
      </div>
      {% endfor %}
    </div>
  </div>
</section>

<section id="contact">
  <div class="container">
    <h2>Get in Touch</h2>
    <p class="about-text">I'm currently looking for internship / freelance opportunities<br>and interesting student projects to collaborate on.</p>
    
    <div class="contact-links">
      <a href="mailto:{{ email }}" class="btn"><i class="fas fa-envelope"></i> Email Me</a>
      {% if linkedin %}
      <a href="{{ linkedin }}" target="_blank" class="btn"><i class="fab fa-linkedin"></i> LinkedIn</a>
      {% endif %}
      {% if github %}
      <a href="{{ github }}" target="_blank" class="btn"><i class="fab fa-github"></i> GitHub</a>
      {% endif %}
    </div>
  </div>
</section>

<footer>
  <div class="container">
    <p>© {{ year }} {{ name }} • Made with ☕ & Flask</p>
  </div>
</footer>

</body>
</html>
"""

@app.route("/")
def portfolio():
    data = {
        "name": "Alex Taylor",
        "title": "Computer Science Student • AI & Web Enthusiast",
        "about": """
        I'm a third-year Computer Science student passionate about building useful 
        things with code. Currently learning <strong>full-stack development</strong>, 
        <strong>machine learning</strong> and <strong>cloud technologies</strong>.<br><br>
        I love turning ideas into working products — whether it's a tiny script 
        that saves hours of work or a complete web application used by hundreds of people.
        """,
        "email": "alex.taylor.edu@gmail.com",
        "github": "https://github.com/alextay-student",
        "linkedin": "https://linkedin.com/in/alextaylor-cs",
        "twitter": None,
        "year": "2026",
        "projects": [
            {
                "title": "StudyFlow – AI Study Planner",
                "description": "Web app that creates personalized study schedules using GPT-like model + drag & drop calendar",
                "tags": ["React", "Python", "FastAPI", "PostgreSQL"],
                "image": "https://images.unsplash.com/photo-1506784983877-45594f9d87db?w=800",
                "link": "https://github.com/alextay-student/studyflow"
            },
            {
                "title": "Campus Marketplace",
                "description": "Second-hand student marketplace with image recognition upload and price suggestion",
                "tags": ["Next.js", "Firebase", "TensorFlow.js"],
                "image": "https://images.unsplash.com/photo-1556740738-b6a63e27c4df?w=800",
                "link": "https://github.com/alextay-student/campus-market"
            },
            {
                "title": "Mood Music Recommender",
                "description": "Detects emotion from webcam → recommends Spotify playlist (group project)",
                "tags": ["Python", "OpenCV", "Flask", "Spotify API"],
                "image": "https://images.unsplash.com/photo-1511671782779-c97d3d27c1d4?w=800"
            },
            {
                "title": "Personal Finance Tracker",
                "description": "Expense tracker with OCR receipt scanning and monthly insights",
                "tags": ["Django", "Tesseract", "Chart.js", "Tailwind"],
                "image": "https://images.unsplash.com/photo-1554224155-6726b3ffdb1c?w=800"
            }
        ]
    }

    return render_template_string(HTML_TEMPLATE, **data)


if __name__ == "__main__":
    print("Portfolio running at:  http://127.0.0.1:5000")
    app.run(debug=True)