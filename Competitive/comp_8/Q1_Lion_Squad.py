def list_input():
    lst = []
    n = int(input("Enter number of elements: "))
    #List input from user
    for i in range(0, n):
        element = int(input("Enter element: "))
        lst.append(element)

    print("Entered list: ", lst)
    return lst

def list_part(lst):
    sum_lst = []
    size_list = len(lst)

    for i in range(0,size_list):
        sum_lst.append(sum(lst)) #calculating total sum of all elements in list and storing in another list
        lst.pop(0)

    sum_lst.append(0)
    print("Sum of list parts:")
    print(sum_lst)

if __name__=="__main__":
    lst = list_input()
    list_part(lst)