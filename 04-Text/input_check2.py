import re

while True:

    print("Voer je postcode in:")
    invoer = input("> ")

    patroon = '\d{4} ?[A-Z]{2}654'

    matches = re.findall(patroon, invoer)

    
    if (len(matches) > 0):
        break

print("Bedankt postcode in juiste formaat:", matches[0])