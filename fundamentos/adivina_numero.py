import random

def user_guess():
	number = random.randint(1,10)
	guess = int(input("Adivina el número entre 1 y 10: "))
	if guess == number:
		print("¡Felicidades! Adivinaste el número")
	elif guess < number:
		print("El número es mayor")
	else:
		print("El número es menor")

def program_guess():
	number = int(input("Ingresa un número entre 1 y 10: "))
	guess = random.randint(1,10)
	print(f"La computadora eligió: {guess}")
	if number == guess:
		print("La computadora adivinó el número!!")
	else:
		print("La computadora no adivinó el número :c")

def main():
	user_guess()
	program_guess()

if __name__ == "__main__":
	main()


