import PersonClass as p

def main():
    # Local variables
    name = 'John'
    address = '1234 Main St'
    phone_number = '123-456-7890'
    cust_number = 1234
    on_list_flag = False

    john_person = p.Person(name,address,phone_number)

    john_customer = p.Customer(name,address,phone_number,cust_number,on_list_flag)

    john_person.print_person()

    print()
    print()

    john_customer.print_person()


main()