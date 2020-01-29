from darksky.api import DarkSky
from darksky.types import languages, units, weather
from geopy.geocoders import Nominatim
from flask import Flask,render_template ,request
app=Flask(__name__)
@app.route("/")
def index():
    geolocator = Nominatim(user_agent="MJGEo")
    location = geolocator.geocode("Patna")
    mloc=location
    API_KEY = 'e2fea81b36c2588f1315c4ad2b721989'
    darksky = DarkSky(API_KEY)
    latitude = location.latitude
    longitude = location.longitude
    forecast = darksky.get_forecast(
        latitude, longitude,
        extend=False, # default `False`
        lang=languages.HINDI, # default `ENGLISH`
        units=units.AUTO, # default `auto`
        exclude=[weather.MINUTELY, weather.ALERTS] # default `[]`
    )

    icon=forecast.currently.icon
    temperature=forecast.currently.temperature
    print(temperature)
    print(forecast.timezone)
    forecast.latitude # 42.3601
    forecast.longitude # -71.0589
    forecast.timezone # timezone for coordinates. For exmaple: `America/New_York`

    forecast.currently # CurrentlyForecast. Can be finded at darksky/forecast.py
    forecast.minutely # MinutelyForecast. Can be finded at darksky/forecast.py
    forecast.hourly # HourlyForecast. Can be finded at darksky/forecast.py
    forecast.daily # DailyForecast. Can be finded at darksky/forecast.py
    forecast.alerts # [Alert]. Can be finded at darksky/forecast.py
    params={'sloc':mloc}
    return render_template("index.html",name=mloc,icon=icon,temperature=temperature)
@app.route("/result",methods=['GET','POST'])
def result():
    if request.method == 'POST':
        result=request.form
        print(result['mlocation'])
        geolocator = Nominatim(user_agent="MJGEo")
        location = geolocator.geocode(result['mlocation'])
        mloc=location
        API_KEY = 'e2fea81b36c2588f1315c4ad2b721989'
        darksky = DarkSky(API_KEY)
        latitude = location.latitude
        longitude = location.longitude
        forecast = darksky.get_forecast(
            latitude, longitude,
            extend=False, # default `False`
            lang=languages.ENGLISH, # default `ENGLISH`
            units=units.AUTO, # default `auto`
            exclude=[weather.MINUTELY, weather.ALERTS] # default `[]`
        )

        summary=forecast.hourly.summary
        temperature=forecast.hourly.data[0].temperature
        icon=forecast.daily.data[0].icon
        visibility=forecast.daily.data[0].visibility
        print(temperature)
        print(forecast.timezone)
        forecast.latitude # 42.3601
        forecast.longitude # -71.0589
        forecast.timezone # timezone for coordinates. For exmaple: `America/New_York`

        forecast.currently # CurrentlyForecast. Can be finded at darksky/forecast.py
        forecast.minutely # MinutelyForecast. Can be finded at darksky/forecast.py
        forecast.hourly # HourlyForecast. Can be finded at darksky/forecast.py
        forecast.daily # DailyForecast. Can be finded at darksky/forecast.py
        forecast.alerts # [Alert]. Can be finded at darksky/forecast.py
        params=[mloc,summary,temperature,icon,visibility]
        return render_template("index.html",params=params)