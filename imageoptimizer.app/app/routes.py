from flask import render_template
from flask import current_app as app  # Use current_app instead of recreating the app

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/about')
def about():
    return "About Page"

@app.route('/routes')
def show_routes():
    output = []
    for rule in app.url_map.iter_rules():
        output.append(f"{rule.endpoint}: {rule.rule}")
    return "<br>".join(output)