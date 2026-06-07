from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    projects = [
        {
            "title": "Weather App",
            "description": "A robust web-based inventory management system that enables businesses to track stock levels, manage orders, and generate detailed reports in real time.",
            "technologies": ["Python", "Flask", "SQLite", "Jinja2", "Bootstrap"],
            "github": "https://github.com/spw3bt3ch/ai-weather-app",
            "demo": "https://ai-weather-app-pi.vercel.app/",
            "image": "images/weather.png",
        },
        {
            "title": "COSEF Platform",
            "description": "A comprehensive web portal for the Civic Orientation and Social Empowerment Foundation (COSEF), facilitating community empowerment, social orientation program management, and student enrollments.",
            "technologies": ["Python", "Flask", "SQLite", "Tailwind CSS", "Jinja2"],
            "github": "https://github.com/spw3bt3ch/cosef",
            "demo": "https://www.cosef.org.ng/",
            "image": "images/cosef.png",
        },
        {
            "title": "Portfolio Platform for Designers",
            "description": "A dynamic portfolio web application built for creative designers to showcase their work, attract clients, and manage project galleries.",
            "technologies": ["Python", "Flask", "Tailwind CSS", "SQLite", "Jinja2"],
            "github": "https://github.com/spw3bt3ch",
            "demo": "https://graphics-designers-portfolio-websit.vercel.app/",
            "image": "images/graphics-design.png",
        },
        {
            "title": "Health Radar",
            "description": "A modern Flask web application for evaluating 14 key health metrics including BMI, cardiovascular health, stroke risk, metabolic health, respiratory health, and more.",
            "technologies": ["Python", "Flask", "SQLite", "Jinja2", "Bootstrap"],
            "github": "https://github.com/spw3bt3ch",
            "demo": "https://health-radar-three.vercel.app/",
            "image": "images/health-radarr.png",
        },
    ]

    skills = {
        "Design & UI/UX": ["Figma", "Adobe Suite", "UI/UX Prototypes", "Wireframes", "Mobile-First Design"],
        "Web Development": ["Python", "Flask & FastAPI", "JavaScript (ES6+)", "HTML5 & CSS3", "Tailwind CSS"],
        "Databases & Backend": ["PostgreSQL", "MySQL", "SQLite", "REST APIs", "SQLAlchemy"],
        "Cloud & Infrastructure": ["Vercel / Netlify", "AWS / DigitalOcean", "Git & GitHub", "Cloudflare / DNS", "SSL / Security"],
    }

    services = [
        {
            "icon": "mdi mdi-web",
            "title": "Web Design & Development",
            "description": "Stunning, responsive designs paired with powerful development to create high-conversion websites. Sub-services include SEO, cloud hosting, domains, and maintenance.",
            "link": "/web-design-development",
        },
        {
            "icon": "mdi mdi-server",
            "title": "Backend Development",
            "description": "Scalable, secure, and high-performance backend systems using Python, Flask, and FastAPI tailored to your business needs.",
        },
        {
            "icon": "mdi mdi-api",
            "title": "API Development",
            "description": "Custom RESTful APIs that power mobile apps, web clients, and third-party integrations with full documentation.",
        },
        {
            "icon": "mdi mdi-cog",
            "title": "Custom Software Development",
            "description": "Bespoke software solutions engineered from scratch to solve unique business challenges efficiently.",
        },
        {
            "icon": "mdi mdi-robot",
            "title": "Automation Systems",
            "description": "Intelligent automation tools and scripts that eliminate repetitive tasks and streamline operations at scale.",
        },
        {
            "icon": "mdi mdi-palette",
            "title": "Graphics & Product Design",
            "description": "Creative visual solutions spanning brand identity, UI/UX design, and product graphics — delivering stunning, user-centred designs.",
        },
    ]

    return render_template("index.html", projects=projects, skills=skills, services=services)


@app.route("/web-design-development")
def web_design_development():
    return render_template("web_design_development.html")


@app.route("/ai-training")
def ai_training():
    return render_template("genai_training.html")


@app.route("/ai-training-cohort3")
def ai_training_cohort3():
    return render_template("genai_training_cohort3.html")


# Legacy redirect — keep old URL working
@app.route("/women-ai-training")
def women_ai_training():
    from flask import redirect
    return redirect("/ai-training")


if __name__ == "__main__":
    app.run(debug=True)
