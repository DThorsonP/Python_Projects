# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {words: words.__len__() for words in sentence.split()}
# print(result)

weather_c = {
    "Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14,
    "Friday": 21, "Saturday": 22, "Sunday": 24
    }

# weather_f = {new_key: new_value for key, value in weather_c.items()}
weather_f = {day:temp * 9/5 +32 for (day, temp) in weather_c.items()}
print(weather_f)

# Output
# {'Monday': 53.6, 'Tuesday': 57.2, 'Wednesday': 59.0, 'Thursday': 57.2,
# 'Friday': 69.8, 'Saturday': 71.6, 'Sunday': 75.2}
