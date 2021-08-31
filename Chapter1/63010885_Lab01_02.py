print(" *** Wind classification ***")
wildSpeed = float(input("Enter wind speed (km/h) : "))

if wildSpeed >= 0 and wildSpeed <= 51.99 :
    print("Wind classification is Breeze.")
elif wildSpeed >= 52.00 and wildSpeed <= 55.99 :
    print("Wind classification is Tropical Storm.")
elif wildSpeed >= 56.00 and wildSpeed <= 101.99 :
    print("Wind classification is Tropical Storm.")
elif wildSpeed >= 102.00 and wildSpeed <= 208.99 :
    print("Wind classification is Super Typhoon.")
elif wildSpeed > 208.99 :
    print("Wind classification is Super Typhoon.")