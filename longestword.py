def magic(string1, string2):
	
	# Initializing Variables
	string1_hash = [0]*26
	string2_hash = [0]*26
	string1_len = len(string1)
	string2_len = len(string2)

	# variable used to track of the number of wildcard in a string
	string1_wildcard = 0
	string2_wildcard = 0

	# Variable which is used to find the mismatches in the string
	mismatch = 0

	# Assigning values to the string1_hash and string2_hash based on the availability of the the alphabets 
	for char in string1:
		# Checking for wildcard entries
		if char != "?":
			string1_hash[ord(char)-97] += 1
		else:
			string1_wildcard += 1
	for char in string2:
		# Checking for wildcard entries
		if char != "?":
			string2_hash[ord(char)-97] += 1
		else:
			string2_wildcard += 1

    # Checking for mismatches
	if string1_len > string2_len : 
		for i in range(26):
			if (string2_hash[i] != 0) and (string2_hash[i] > string1_hash[i]):
				mismatch += string2_hash[i] - string1_hash[i]
		# returning values based on wilcard entries and mismatch
		if mismatch <= string1_wildcard:
			return True
		else:
			return False
	else:
		for i in range(26):
			if (string1_hash[i] != 0) and (string1_hash[i] > string2_hash[i]):
				mismatch += string1_hash[i] - string2_hash[i]
		# returning values based on wilcard entries and mismatch
		if mismatch <= string2_wildcard:
			return True
		else:
			return False
    
def longest(string):
	file = open("enable1.txt", "r") 
	max_letter = ""
	for line in file.read().splitlines():
		if magic(string, line):
			if len(max_letter) < len(line):
				max_letter = line
	return(max_letter)

print(longest("uruqrnytrois"))
print(longest("rryqeiaegicgeo??"))