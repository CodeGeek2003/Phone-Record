def main():
    phone_record={}
    while True:
        print('''1. Add a new phone number
2. Delete a phone number
3. Update a phone number
4. Search a phone number
5. Display all phone numbers
6. Quit''')
        choice=int(input('Enter your choice: '))
        if choice ==6:
            break
        elif choice==1:
            add_contact(input('Enter name: '),input('Enter number: '),phone_record)
        elif choice==2:
            delete_contact(input('Enter name: '),phone_record)
        elif choice==3:
            update_contact(input('Enter name: '),input('Enter number: '),phone_record)
        elif choice==4:
            search_contact(input('Enter name: '),phone_record)
        elif choice==5:
            display_all(phone_record)
        else:
            print('Invalid choice')
def add_contact(name,number,phone_record):
    if (name in phone_record):
        print('Contact already exists with this name')
    else:
        phone_record[name]=number
        print('Contact added successfully')
def delete_contact(name,phone_record):
    if name in phone_record:
        del phone_record[name]
        print('Contact deleted successfully')
    else:
        print('Contact not found')
def update_contact(name,number,phone_record):
    if name in phone_record:
        phone_record[name]=number
        print('Contact updated successfully')
    else:
        print('Contact not found')
def search_contact(name,phone_record):
    if name in phone_record:
        print('Contact found')
        print('Name: ',name,'Number: ',phone_record[name])
    else:
        print('Contact not found')
def display_all(phone_record):
    for name,number in phone_record.items():
        print('Name: ',name,'Number: ',number)
if __name__=='__main__':
    main()
