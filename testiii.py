def get_int(start_message, error_message, end_message):
    print(start_message)
    while True:
        p = input()
        try:
            int(p)
        except:
            print(error_message)
        else:
            print(end_message)
            return int(p)




x = get_int('Input int number:', 'Wrong value. Input int number:', 'Thank you.')