import sys
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
def read_data(name):
    #name = input("enter the name to search data:")
    #that is taken from the main method function and is carried out in read_name(name):

  with open(name, 'r') as friend:
      filecontent = friend.read()
      print(filecontent)

    #another way of reading file:
   # friend = open("name.txt",'r')
    #if friend.mode == 'r'
     #   contents = friend.read()
      #  print(contents)
def main():
    print("WELCOME TO MY RECORDS")

    #retake = 'y'
    #while retake =='y' or retake == 'Y':
    option= int(input('enter the option:\n1)to write/add the data\n2)to search the already saved data\n3)to exit the system'))

    #name = input("Ener your friends name:")
    if option == 3:
        sys.exit()
    elif option == 1:
        name = input("Ener your friends name:")
        write_data(name)
    elif option == 2:
        name = input("Ener your friends name:")
        read_data(name)
        #read data function is not working
    else:
          print("enter the valid option from the main menu:")
          sys.exit()#when while loop works, it's to be removed
    #print("do you wish to add another data/ another friend's data?")
    #retake = input("enter: y to continue,\npress anything else(enter) : no: ")
     
main()