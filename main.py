from zdesk import Zendesk

def get_var(var, array):
    try:
        val = array[var]
    except KeyError:
        val = ""
    return val

def main():

    try:
        zendesk = Zendesk('https://zccstudents3720.zendesk.com', 'davecverano@gmail.com', None, None, 'Asdf123!')
    except:
        print("API Error")
        return
    # List
    ticket_list = zendesk.tickets_list()

    print('Welcome to ticket viewer')

    while True:
        print('Type \'menu\' to view options or \'quit\' to exit.')
        user_input = input()

        if user_input == 'menu':
            while True:
                print('\t')
                print('\tPress 1 to view all tickets.')
                print('\tPress 2 to view a tickets.')
                print('\tType \'quit\' to exit.')
                print('\t')

                user_input = input()

                if user_input == '1':
                    for ticket in get_var('tickets', ticket_list)[1:9]:
                        print("Ticket with subject \'{subject}\' created on {date}".format(subject=get_var('subject', ticket),date=get_var('created_at', ticket)))
                elif user_input == '2':
                    if get_var('tickets', ticket_list):
                        print("Ticket with subject \'{subject}\' created on {date}".format(subject=get_var('subject', ticket_list['tickets'][0]),date=get_var('created_at', ticket_list['tickets'][0])))
                elif user_input == 'quit':
                    break
                else:
                    print('The input you entered is invalid. Please type \'menu\' to view options or \'quit\' to exit')


        if user_input == "quit":
            print('Thanks for using the viewer. Goodbye.')
            break

        else:
            print('The input you entered is invalid.')


if __name__ == "__main__":
    main()