# ~~~ This is a template for question 2  ~~~

#imports

#~~~  implementation of Insertion Sort  ~~~


#we decided to code the two insertion sorts that we studied in class, the first one that we choose is more efficient because
#it uses a while loop that might finish this step earlier. In worst case it is the same as the other implementation.


def insertion_sort(_input=list):
    if len(_input)==0:              #checks that the list is not empty
        raise ValueError("invalid input")
    if type(_input[0]) == str:      #type checks
        raise TypeError ("invalid input")
    count = 2                       #counting 2: 2 comparison

    for i in range(1,len(_input)):  #running on the list, starting from 1 until the end
        if type(_input[i]) == str:  #check type for value i
            raise TypeError ("invalid input")
        val = _input[i]         
        j=i-1
        count += 4                  #counting 4: 1 for loop, 1 type check, and 2 assignments

        # we assume that all the values from 0 to i-1 are sorted, and now we insert value i in the right place
        # between 0 and i
        while (j>=0 and _input[j]>val):
            _input[j+1] = _input[j]
            j = j-1
            count += 4          #counting 4: 2 compares (in the while statement) and 2 assignments
        _input[j+1] = val
        count += 3              #counting 3: 1 or 2 compares (that ended the while loop), and assignment  
        
    return _input, count


#the second insertion sort
def insertion_sort_2(_input=list):
    if len(_input)==0:              #checks that the list is not empty
        raise ValueError("invalid input")
    if type(_input[0]) == str:      #type checks
        raise TypeError ("invalid input")
    count = 2                       #counting 2: 2 comparison            

    for i in range(1, len(_input)): #running on the list starting from 1
        if type(_input[i]) == str:  #check type for value i
            raise TypeError ("invalid input")
        count += 2                  #counting 2: the for loop and the type check

        # running from 0 to i-1, inserting the i value in its place
        for j in range(i):
            if _input[i]<_input[j]:     #checks which number is smaller
                item=_input.pop(i)      #removing the smaller number from the list
                _input.insert(j,item)   #inserting the smaller number to the right location
                count += 4          #counting 4: for loop,if,two assignments
            else:
                count += 3          #counting 3: for loop,if,else
    return _input, count


#this function gets a list and uses insertion sort

def insertion_sort_implementation(_input=list):
    return (insertion_sort(_input))
