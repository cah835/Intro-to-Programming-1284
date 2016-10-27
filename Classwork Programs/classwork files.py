def main():
    try:
        my_file = open(input('Please enter to file you wish to open: '))
        if not my_file.endswith('.text'):
            myfile += '.txt'
    except FileNotFoundError as error:
        print(error)
        print('Restart the program to continue.')
    print(my_file)

main()
