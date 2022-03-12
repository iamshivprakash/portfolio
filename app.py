from flask import Flask, render_template
import sql

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/blog')
def blog():
    return render_template("blog.html")


@app.route('/projects')
def project():
    projects = sql.projects
    return render_template("projects.html", projects=projects)


@app.route('/certifications')
def certification():
    certificates = sql.certificates
    return render_template("certifications.html", certificates=certificates)


if __name__ == '__main__':
    app.run(debug=True)
