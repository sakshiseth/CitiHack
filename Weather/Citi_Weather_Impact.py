from Weather.WeatherAlert import getWeatherForecastDetails
import matplotlib.pyplot as plt
import random

class makeWeatherConclusion():
    def getWeatherConclusionAsImage(self):
        metro_city = ["Delhi", "Bangalore", "Pune", "Hyderabad", "Chennai", "Mumbai", "Kolkata", "Ahmedabad",
                          "Amaravati", "Visakhapatnam", "Jaipur", "Surat", "Jamshedpur", "Nagpur"]

        WeatherFore = getWeatherForecastDetails()
        State_pair = dict()
        for city in metro_city:
            response = WeatherFore.getDetails(city)
            if response in State_pair:
                State_pair[response] += ", "+ city
            else:
                State_pair[response] = city
        Labels = []
        Sizes = []
        for condition in State_pair:
            label = str(condition).upper()+ " : " +State_pair[condition]
            Labels.append(label)
            Sizes.append(len(label.split(', ')))
        print(Labels)
        print(Sizes)
        explode = []
        for i in range(0,len(Sizes)):
            if i%2 == 0:
                explode.append(0.0)
            else:
                explode.append(0.1)
        plt.subplots(figsize =(15, 12))
        plt.pie(Sizes, labels = Labels,explode=explode)
        plt.savefig('./template/Weather.jpg')