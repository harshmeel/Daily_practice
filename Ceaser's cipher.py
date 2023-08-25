import string
# write your code here!
alphabet = " " + string.ascii_lowercase


positions ={}
i = 0
for x in alphabet:
    positions[x] = i
    i += 1


message = "hi my name is caesar"

#function to do the same
def encoding(msg, key):
    encoded_msg=""
    for x in msg:
        #find the position original    
        ind = positions[x]
        #find letter correponding to altered position
        encoded_msg += alphabet[(ind+key)%27]
    return encoded_msg
