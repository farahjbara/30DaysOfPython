#1️⃣ Assessment1
#Instructions
#Locate and open the playground/challenge_1.py file.

#Complete the the_good_bad_and_sorted function.

#Requirements:

#Process and categorize each str object in the input as good or bad data.

#Good data:

#Even numbers.
#Sorted in descending (high-to-low) order.
#Bad data:

#Objects that cannot be converted into int objects.
#Sorted in ascending (low-to-high) order.
#Discarded data:

#Odd numbers.
#Return a tuple containing the lists of good and bad data.
def the_good_bad_and_sorted(sequence):
    '''
    Args:
        sequence    | An iterable consisting of str objects. 
                    |> Convert all strings possible into int objects.
                    |> Any string that cannot be converted into an int will remain a string.
                    |> Example: ['N/A', '21', '42', 'MISSING']

    Returns:
        A (2)tuple of lists consisting of good and bad data. (good: list, bad: list)
    '''
    good_data = []
    bad_data = []

    for item in sequence:
        try:
            # Try converting the string to an integer
            num = int(item)
            if num % 2 == 0:  # Check if it's even
                good_data.append(num)
            # Discard odd numbers (do nothing)
        except ValueError:
            # If conversion fails, it's bad data
            bad_data.append(item)

    # Sort good data in descending order
    good_data.sort(reverse=True)
    # Sort bad data in ascending alphabetical order
    bad_data.sort()

    return good_data, bad_data

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL, verbose=True)

