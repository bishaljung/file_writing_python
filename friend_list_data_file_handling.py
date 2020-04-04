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

def main():
    print("WELCOME TO MUY DIARY")
    # run = True
    while True:
        print("Enter exit if your want to exit")
        name = input("Ener your friends name:")
        if name == "exit":
            # run = False
            sys.exit()

        write_data(name)

main()