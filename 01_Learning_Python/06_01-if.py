weather = input("How's the weather today? ")
if weather == "Rain" or weather == "Snow":
    print("Takes an umbrella.")
elif weather == "Air pollution":
    print("Takes a Mask.")
else:
    print("No preparation needed.")


temp = int(input("How's the temperature today? "))
if temp >= 30:
    print("It's too hot. Don't go out.")
elif 10 <= temp <= 30:
    print("Nice weather.")
elif 0 <= temp:
    print("Bring your coat.")
else:
    print("It's too cold. Don't go out.")