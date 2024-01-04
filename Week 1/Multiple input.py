def weather_predictor(T, H, w):
    W = (0.5 * (T**2)) - (0.2 * H) + (0.1 * w) - 15
    if W > 300:
        return "Sunny"
    elif 200 < W <= 300:
        return "Cloudy"
    elif 100 < W <= 200:
        return "Rainy"
    else:
        return "Stormy"

while(True):
    option = int(input("Select from the below: \n1. Calculate weather condition \n2. Exit\n"))
    match option:
        case 1:
            t = eval(input("Enter temperature in celsius : "))
            h = eval(input("Enter humidity in % : "))
            ws = eval(input("Enter wind speed in kmph : "))

            print(f"The weather condition for the given values is {weather_predictor(t, h, ws)}")
        case 2:
            break
