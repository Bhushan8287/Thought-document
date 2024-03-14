import os, shutil
import datetime as dt

#checks if there's a folder named Thoughts created or not/if not there then it will create it
folder_path = "C:/Users/Bhushan/Desktop/Thoughts project/Thoughts"
if os.path.exists(folder_path) and os.path.isdir(folder_path):
    pass
else:
    folder_name = "Thoughts"
    os.mkdir(folder_name)
    print('New Thoughts folder created')

file_path = "C:/Users/Bhushan/Desktop/Thoughts project/Thoughts"


#keeps log when content was written
current_datetime = dt.datetime.now()
formatted_datetime = current_datetime.strftime("\nLast written on Date: %Y-%m-%d and Time: %H:%M:%S")

class Thought:
    #creates thought file and writes to it
    def topic_name(self,question,your_thoughts,thought_name):
        file = open(thought_name +'.txt',"w")
        file.write('Question: '+ question + ' ?' + '\n' + 'My thoughts as of now: ' + your_thoughts)
        file.write(' ' + str(formatted_datetime))
        file.write('\n')
        file.close()
        print('|---------------------|')
        print('thought file created')
        print('|---------------------|')
        print('\n')

    def read_file(self,thought_name,thought_file_path):
        try:
            file = open(thought_file_path + thought_name + '.txt',"r")
            print('|---------------------------------------------------------------------------------------------------------|')
            # print(self.question)
            print(file.read())
            print('|---------------------------------------------------------------------------------------------------------|')
            file.close()
        except FileNotFoundError:
            print('|--------------------------------------|')
            print('no such thought file exists')
            print('|--------------------------------------|')

    def write_to(self,tght_name,txt_to_append):
        file = open('C:/Users/Bhushan/Desktop/Thoughts project/Thoughts/' + tght_name + '.txt',"a")
        file.write('\n' + txt_to_append) #appends text to the next line
        file.write(' ' + str(formatted_datetime))
        file.write('\n')
        print('|-------------------------|')
        print('written to file sucessful')
        print('|-------------------------|')
        file.close()

#functions

#creates thoughts files and moves them to thoughts folder also checks if theres a though with the same name already
def thought_box(thought_name):  
    inst = Thought()
    question = input('enter question here: ')
    your_thoughts = input('enter your thoughts: ')
    inst.topic_name(question,your_thoughts,thought_name)
    src_file = thought_name + '.txt'
    destination_folder = "C:/Users/Bhushan/Desktop/Thoughts project/Thoughts"
    try:    
        shutil.move(src_file,destination_folder)
    except shutil.Error:
        pass
    try:
        f_path = "C:/Users/Bhushan/Desktop/Thoughts project/" + src_file
        if os.path.exists(f_path):
            os.remove(f_path)
            print('|--------------------------------------|')
            print('cant create thought with the same name')
            print('|--------------------------------------|')
    except PermissionError as e:
        print('|--------------------------------------|')
        print('cant delete file because of permission error',e)
        print('|--------------------------------------|')

def show(thought_name):
    hold = Thought()
    file_path = "C:/Users/Bhushan/Desktop/Thoughts project/Thoughts/"
    hold.read_file(thought_name,file_path)

def write_text(tght_name,txt_to_append):
    hold = Thought()
    hold.write_to(tght_name,txt_to_append)

def show_thoughts():
    folder_path = "C:/Users/Bhushan/Desktop/Thoughts project/Thoughts"
    contents = os.listdir(folder_path)
    if not contents:
        print('|-----------------------|')
        print('There are no thoughts as of now')
        print('|-----------------------|')
    else:
        for thoughts in contents:
            print('|-----------------------|')
            print(thoughts)
            print('|-----------------------|')

def del_thought_file(tght_nm):
    tname = tght_nm + '.txt'
    folder_path = "C:/Users/Bhushan/Desktop/Thoughts project/Thoughts/" + tname
    if os.path.exists(folder_path):
        os.remove(folder_path)
        print('|----------------------|')
        print('thought file deleted')
        print('|----------------------|')
    else:
        print('|-----------------------------|')
        print('no such thought file exists')
        print('|-----------------------------|')















    # print('|-----------------------|')
    # folder_path = "C:/Users/Bhushan/Desktop/Thoughts project/Thoughts"
    # for thought_name in os.listdir(folder_path): 
    #     if os.path.isfile(os.path.join(folder_path,thought_name)):
    #         print(thought_name)
    # print('|-----------------------|')