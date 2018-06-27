alphabet = "abcdefghijklmnopqrstuvwxyz"
mykey = 3
mymessage = (input("Please enter a message:"))
for character in mymessage:
	if character in alphabet:
	    letternumber = alphabet.find(character)
	    newposition = (letternumber + mykey) %26
	    newcharacterinmyalphabet = alphabet[newposition]
	    print("The secret code for",mymessage,"is:",newcharacterinmyalphabet)
	    