#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    #create route array since that's what we'll return
    route=[]

    #transform into a dictionary for ease
    tickets = {flight.source:flight for flight in tickets}

    # set current flight
    current = tickets["NONE"]

    #knowing that the final destination is set to "NONE", loop through
    while current.destination !="NONE":
        #add the flight to route
        route.append(current.destination)
        current = tickets[current.destination]    

    #add the current to the route
    route.append(current.destination)

    return route
