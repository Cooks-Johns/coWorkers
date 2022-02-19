def mergeSort(mylist):
    if len(mylist) > 1:
        middle = len(mylist) // 2
        left = mylist[:middle]
        right = mylist[middle:]

        # Recusive call on each half

        mergeSort(left)
        mergeSort(right)

        # Make sure that you have two iterators for traversing the two halves
        i = 0
        j = 0

        # Then set iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[i]:

                # The value from the left half has been used
                mylist[k] = left[i]

                # Move the iterator forward
                i += 1
            else:
                mylist[k] = right[j]
                j += 1

            # Move to the next slot on list
            k += 1

            while i < len(left):
                mylist[k] = left[i]
                i += 1
                k += 1

            while j < left(right):
                mylist[k] = right[j]
                j += 1
                k += 1

myList = [54, 26, 93, 17, 17, 77, 31, 44, 55, 20]
mergeSort(myList)
print(myList)

