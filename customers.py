"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this
    def __init__(self, first, last, email, password):
        self.first = first
        self.last = last
        self.email = email
        self.password = password


    def __repr__(self):
        return "<Customer: {} {}, {}, {}>".format(self.first, self.last, 
                                                  self.email, self.password)


def read_customers_from_file(filepath):
    customers = {}

    with open(filepath) as file:
        for line in file:
            (first,
             last,
             email,
             password) = line.strip().split("|")
    
            customers[email] = Customer(first, last, email, password)

    return customers


def get_by_email(email):
    return customers[email]


customers = read_customers_from_file('customers.txt')    
