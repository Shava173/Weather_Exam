from flask import Flask, render_template
import requests
from config import API_KEY, CITY_NAME

app = Flask(__name__)

@app.route('/')
def index():
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}&units=metric&lang=uk"
    
    response = requests.get(base_url)
    data = response.json()

    # Додатковий принт для перевірки структури даних
    print(data)

    if response.status_code == 200:
        city = data.get('name', 'Невідомо')
        temperature = data['main'].get('temp', 'Невідомо')
        description = data['weather'][0].get('description', 'Невідомо')
        
        return render_template('index.html', city=city, temperature=temperature, description=description)
    else:
        return f"Error: {response.status_code}, {data.get('message', 'No additional information')}", response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777)
