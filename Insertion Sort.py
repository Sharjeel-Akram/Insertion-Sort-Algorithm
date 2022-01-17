# Recall the “Building Block” strategy discussed in class. Using this strategy:
# a. Implement “insert” algorithm as building block (as a function).
# b. Implement “Insertion Sort” algorithm using “insert” as the building block.
# c. Test your program on 10 integers taken as input from user.



# def Insert(List,i):
#     Current_Value = List[i]
#     Current_Position = i
#     for j in range(len(List)):
#         if Current_Position > 0 and List[Current_Position-1] > Current_Value:
#             List[Current_Position] = List[Current_Position - 1]
#             Current_Position = Current_Position - 1
#         List[Current_Position] = Current_Value
#     return List
def Insert(A,n):
    Current_Value = A[n]
    Current_Position = n
    for j in range(len(A)):
        if Current_Position > 0 and A[Current_Position] > Current_Value:
            A[Current_Position + 1] = A[Current_Position]
            Current_Position = Current_Position - 1
        A[Current_Position + 1] = Current_Value
    return A

def Insertion_Sort(K):
    for i in range(1,len(K)):
        listt = Insert(K,i)
    return listt

#Driver Code to get input from the user
List1 = []
List_Limit = input("How many numbers you want to store: ")
print("Enter your Numbers for the list Please: ")
for i in range(int(List_Limit)):
    N = int(input(" "))
    List1.append(N)
print("The Original List is: ")
print(List1)
print("The Sorted List is Given Below: ")
print(Insertion_Sort(List1))