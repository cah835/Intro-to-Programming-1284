def main():
    encrypt = {'A' : 'D', 'B' : 'E', 'C': 'F', 'D' : 'G', 'E' : 'H', 'F':'I', 'G' :'J', 'H':'K','J':'M','K':'N','L':'O','M':'P', 'N':'Q', 'O':'R', 'P':'S', 'Q':'T','R' :'U', 'S':'V','T':'W', 'U':'X','V':'Y','W':'Z','X':'A','Y':'B','Z':'C'}
    message = input('Enter your message: ')
#get message
    message = message.upper()
#
    e_message = ''

    for letter in message:
        if letter in encrypt:
            e_message += encrypt[letter]
        else:
            e_message += letter

    print(e_message)

main()
