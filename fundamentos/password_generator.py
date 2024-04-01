import random
import string

def password_generator(lenght, special_characters):
	characters = string.ascii_letters + string.digits
	if special_characters:
		characters += string.punctuation
	password = ''.join(random.choice(characters) for i in range(lenght))
	return password

def main():
	lenght = int(input('Ingresa la longitud de la contraseña: '))
	special_characters = input('¿Quieres caracteres especiales? (s/n): ')
	if special_characters == 's':
		special_characters = True
	else:
		special_characters = False
	password = password_generator(lenght, special_characters)
	print(f'Contraseña generada: {password}')

if __name__ == '__main__':
	main()