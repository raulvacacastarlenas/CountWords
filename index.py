print("Hola, ¿En qué estas pensando?")
user_sentence = input()

words = user_sentence.split(" ")

numberWords = len(words)

print("¡Muy bien, tu me has mostrado tu pensamiento en " + str(numberWords) + " palabras!")