def magic(string1, string2):
	
	# Initializing Variables
	string1_hash = [0]*26
	string2_hash = [0]*26
	string1_len = len(string1)
	string2_len = len(string2)

	# Variable which is used to find the mismatches in the string
	mismatch = 0
	
	# Assigning values to the string1_hash and string2_hash based on the availability of the the alphabets
	for char in string1:
		string1_hash[ord(char)-97] += 1
	for char in string2:
		string2_hash[ord(char)-97] += 1

    # Checking for mismatches
	if string1_len > string2_len : 
		for i in range(26):
			if (string2_hash[i] != 0) and (string2_hash[i] > string1_hash[i]):
				mismatch += string2_hash[i] - string1_hash[i]
	else:
		for i in range(26):
			if (string1_hash[i] != 0) and (string1_hash[i] > string2_hash[i]):
				mismatch += string1_hash[i] - string2_hash[i]
    
    # Returning the values based on the mismatches
	if(mismatch == 0):
		return("yes")
	else:
		return("no")

print(magic("edzlatsh", "hazel"))
print(magic("uwtaqicy", "watch"))


