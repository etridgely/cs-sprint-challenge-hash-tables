def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    #create cache set
    cache = {}

     #add all the items into cache
    for i in range(len(weights)):
        # print(i)
        cache[weights[i]] = i

    #loop through again to find the target weight needed
    for j in range(len(weights)):
        k = limit- weights[j]
        
        if k in cache:
            #return the max and min if the values are there
            return (max(j, cache[k]), min(j, cache[k]))

    return None
