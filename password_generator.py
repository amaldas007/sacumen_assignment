import random
import array

MAX_LEN = 20
UPPER_CASE_ARRAY = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
   

 
LOWER_CASE_ARRAY = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
  

SYMBOLS_ARRAY = ['@', '#', '$', '%', '=', '?', '|', '*']
DIGITS_ARRAY = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

print('This is a Password generator! Enter length of your password')

#input the length of password
length = int(input('\nEnter the length of password: ')) 
if (length>=8 and length <= MAX_LEN):

   # find digit array
    rand_digit = random.choice(DIGITS_ARRAY)
    DIGITS_ARRAY.remove(rand_digit)
    rand_symbol = random.choice(SYMBOLS_ARRAY)
    SYMBOLS_ARRAY.remove(rand_symbol)
    # find upper and remove it from the lower case array Exclude similar characters
    rand_upper = random.choice(UPPER_CASE_ARRAY)
    UPPER_CASE_ARRAY.remove(rand_upper)
    LOWER_CASE_ARRAY.remove(rand_upper.lower())
    # find lower and remove it from upper case array to Exclude similar characters
    rand_lower = random.choice(LOWER_CASE_ARRAY)  
    UPPER_CASE_ARRAY.remove(rand_lower.upper())
    LOWER_CASE_ARRAY.remove(rand_lower)
    FULL_LIST = DIGITS_ARRAY  + SYMBOLS_ARRAY + LOWER_CASE_ARRAY

    temp_pass = rand_digit + rand_lower  + rand_symbol + rand_upper

    for x in range(length - 4):
        rand = random.choice(FULL_LIST)
        temp_pass = temp_pass + rand
        FULL_LIST.remove(rand)
       

    print(temp_pass)
else:
    print('Invalid Entry- Max length is 20 and Min length is 8')
