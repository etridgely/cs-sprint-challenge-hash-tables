def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    #create cache & result
    cache = {}
    result = []

    #loop de loop, one loop through an array and then through the other
    for i in arrays:
        # i being an array here
        for target in i:
            # see if target is in the cache
            if target in cache:
                cache[target] += 1
                # add the target to the result when the index == length
                if cache[target] == len(arrays):
                    result.append(target)
            else:
                #otherwise, the cache
                cache[target] = 1

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
