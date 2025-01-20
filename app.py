from flask import Flask, render_template, request
from utils import recommend_events_for_county
from models import load_data
from counties import oklahoma_counties

app = Flask(__name__)

event_county_matrix = load_data()

@app.route('/', methods=['GET', 'POST'])
def index():
    selected_county = ''  # Initialize with an empty string or None
    recommendations = []
    
    if request.method == 'POST':
        selected_county = request.form.get('county')
        recommended_events = recommend_events_for_county(selected_county, event_county_matrix, 5)
        return render_template('index.html', recommendations=recommended_events, counties = oklahoma_counties, selected_county=selected_county)
    return render_template('index.html', recommendations=[], counties = oklahoma_counties, selected_county=selected_county)

if __name__ == '__main__':
    app.run(debug=True)
