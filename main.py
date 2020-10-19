import random

running = True


while running == True:
	number = random.randint(1, 6)
	print(f"Du fick en {number}a")
	thing = input("Skriv 'Fortsätt' för att slå om tärningen\nSkriv 'Sluta' för att avsluta programmet")

	print("\n\n\n")
	if thing == "Sluta" or thing == "sluta":
		running = False

	if not thing == "Fortsätt" or thing == "fortsätt" or thing == "sluta" or thing == "Sluta":
		while True:
			shait = random.choice(["&", "#", "%", "?", "~", "!", "@", "$", "¤", "}", "{", ";"])
			shait2 = random.choice(["&", "#", "%", "?", "~", "!", "@", "$", "¤", "}", "{", ";"])
			print(f"{shait}ERROR{shait2}")

