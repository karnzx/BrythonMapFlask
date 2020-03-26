from flask import Flask, render_template
import folium
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1><a href="/map">Map</a></h1>'

@app.route('/map')
def map():
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)
