import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Function to get weather data
def get_weather(city):
    api_key = "9cae75347a0d65b8361b2100c8d55615"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] == "404":
            return None
        else:
            main = data["main"]
            wind = data["wind"]
            weather = data["weather"][0]
            
            temperature = main["temp"]
            humidity = main["humidity"]
            pressure = main["pressure"]
            wind_speed = wind["speed"]
            weather_description = weather["description"]

            return {
                "temperature": temperature,
                "humidity": humidity,
                "pressure": pressure,
                "wind_speed": wind_speed,
                "description": weather_description.capitalize()
            }
    except Exception as e:
        print(e)
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather(city)
        
        if weather_data:
            return render_template('index.html', weather=weather_data, city=city)
        else:
            return render_template('index.html', error="City not found or API error!")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)



