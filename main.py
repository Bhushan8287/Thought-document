import functions

print('------------------------')
user_action = input("press enter to continue: ")
while user_action != '0':
    print('------------------------')
    user_action = input("|1 to create thought      |\n|2 to read thought        |\n|3 to write to a file     |\n|4 to show all thoughts   |\n|5 to delete thought file |\n|0 to exit program        |\n------------------------\nenter here: ")
    if user_action == '1':
        thought_name = input('type the thought name here: ')
        functions.thought_box(thought_name)
    elif user_action == '2':
        functions.show_thoughts()
        tght_name = input('type the thought name here you want to read: ')
        functions.show(tght_name)
    elif user_action == '3':
        tght_name = input('name of thought to append to: ')
        txt = input('write here to append to file: ')
        functions.write_text(tght_name,txt)
    elif user_action == '4':
        functions.show_thoughts()
    elif user_action == '5':
        tght_nm = input('enter thought name you want to delete: ')
        functions.del_thought_file(tght_nm)
    elif user_action == '0':
        print('program closed')
        break