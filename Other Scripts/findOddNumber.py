def iq_test(numbers):
    #Find the odd or even number different from the others
    numbersArray = [int(x) for x in numbers.split(" ")]
    filteredArray = [x%2 for x in numbersArray]
    return filteredArray.index(1)+1 if sum(filteredArray) == 1 else filteredArray.index(0)+1