import sys
import os
def write_data(name):

    friend = open(name+".txt",'w')
    id_num = input('ID number: ')
    phone_number = int(input('phone_number: '))

    friend.write("the details of {} is:\n".format(name))
    friend.write("name: %s\n" %name)
    friend.write("id_num: %s\n"% id_num)
    friend.write("phone number: %s\n" %phone_number)
    friend.close()
#my problem is :
#name is not passing to the function in read_data
#and read_data function is not working
def delete_data(name):
        os.remove(name+".txt")
        print("information file, removed successfully")

def read_data(name):
    #name = input("enter the name to search data:")
    #that is taken from the main method function and is carried out in read_name(name):
   #try
   with open(name+".txt",'r') as filehandle:
     filecontent = filehandle.read()
     print(filecontent)

     #except ValueError:
     # print("enter the valid name")
    #another way of reading file:
    #infile = open(name,'r')
   # contents = infile.read()
   # print(contents)
    #infile.close()
def edit_data(name):
    with open(name+".txt",'r') as filehandle:
      filecontent = filehandle.readlines()
      print(filecontent)

    change_param = input("What would like to change: ")
    value = input("Enter the value for %s"%change_param)
    person = []
    for line in filecontent[1:]:
        person.append(line.split(":"))
        
    new_person = []
    for data in person:
        if data[0]==change_param:
            new_person.append([data[0],value])
        else:
            new_person.append(data)
    if change_param == "name":
        name = value

    with open(name+".txt",'w') as f :
        f.write("The details of %s are:\n"%name)
        for line in new_person:
            f.write("{} : {}".format(line[0],line[1]))
    


def main():
    print("WELCOME TO MY RECORDS")

    retake = 'y'
    while retake =='y':
        option= int(input('enter the option:\n1)to write/add the data\n2)to search the already saved data\n3)to edit the data\n'
                      '4)to remove the data\n5)to exit the system'))

       #name = input("Ener your friends name:")
        if option == 5:
            sys.exit()
        elif option == 1:
            name = input("Ener your friends name:")
            write_data(name)
        elif option == 2:
            name = input("Ener your friends name:")
            read_data(name)
            #read data function is not working
        elif option == 3:
            name = input("enter the name to edit the data:")
            edit_data(name)
        elif option == 4:
              name = input("enter the name to delete the data:")
              delete_data(name)

        else:
              print("enter the valid option from the main menu:")
              main()#when while loop works, it's to be removed

        print("do you wish to go to main menu?")
        retake = input("enter: y to continue,\npress anything else(enter) : no: ")

main()
