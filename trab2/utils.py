def accuracy(predict, real):
    equals = zip(predict, real)
    equals = filter(lambda x: x[0] == x[1], equals)
    
    accuracy = len(list(equals)) / len(list(real))

    return accuracy