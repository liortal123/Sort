# ~~~ This is a template for question 1  ~~~

#imports

#~~~  implementation of merge sort  ~~~




#this function gets a list and uses merge sort
def merge_sort_implementation(_input=list):
    if len(_input)==0:
        raise ValueError("invalid input")
    return _input, merge_sort(_input, 0, len(_input)-1, 2)      #counting 2: the compare, and calling merge_sort (the last parameter is the counter)

#calling our functing merge sort, sending the indexes of the first and last index of the list,
#and a counter of the number of actions in the function


# counting steps logic: the counter that is passed to the merge-sort function includes the steps in the function so far
# the counter takes into account: the comparison action, each function call, assignment statement, loop iteration
def merge_sort (lst,start,end,count):
    if start < end:
        middle = (start+end)//2                         #middle index
        count = merge_sort(lst, start, middle, count+3) #counting 3: the compare, the assignment, and the function call
        #(the value that returns sums all the following and previous steps from the recursion call)
        count = merge_sort(lst, middle+1, end, count+1) #counting 1: the function call 
        count = merge(lst,start,middle,end,count+1)     #counting 1: the function call, and add to the counter the amount of steps in the merge
    return count                                        #returning the final values 



def merge(lst, start, middle, end, count):
    length_L = middle - start + 1   #the length of the left side
    length_R = end - middle         #the length of the rest of the list
    L = [0]*(length_L+1)
    R = [0]*(length_R+1)
    count += 4                      #counting 4 assignment actions

    # copy lst[start:middle] into L - the left sub-list
    for i in range(0,length_L):
        L[i] = lst[start+i]
        count += 2                  #counting the steps: for loop, and one assignment

    # copy lst[middle+1:end] into R - the right sub-list
    for j in range(0,length_R):
        R[j] = lst[middle+j+1]
        count += 2                  #counting the steps: for loop, and one assignment 

    # put inf value at the end of L and R
    L[length_L] = float("inf")
    R[length_R]= float("inf")
    i=0
    j=0
    count += 4                      #counting 4 assignment actions 

    # because of the recursion each list (L,R) is sorted internally
    # this loop merge the 2 list into a single sorted list
    for num in range(start,end+1):
        if type(L[i])== str or type(R[j]) == str:
            raise TypeError("invalid input")
        if L[i] <= R[j]:
            lst[num] = L[i]
            i += 1
            count += 5      #counting the steps: for loop, two compares, and two assignments
        else:
            lst[num] = R[j]
            j += 1
            count += 6      #counting the steps: for loop, two compares, else, and the two assignment
    return count            #returning the amount of steps, the list is merged in place
            

