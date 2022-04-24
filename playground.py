### Goal is to merge two given Node lists into one sorted list
### Ex: list1 = [1, 2, 4] ---- list2 = [1, 3, 4]
### Result: merged_list = [1, 1, 2, 3, 4, 4]

### IMPORTANT!!
## Node lists does not work like a normal list
## list1 = [(1) -> (2) -> (4)] ----------- The list has some nodes () with its own value 1, 2, 4 which has a pointer that directs
## to the next node ------- Ex: list = [(1) -> (2)]  This means list[0] = node1 and node1.value = 1 and node1.next = node2

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val                        ### This is a basic ListNode class that is used to create Nodes
        self.next = next                      ### Ex: node1 = ListNode(1), node2 = ListNode(2)
                                              ### node1.next = node2

def solution(list1, list2):
    if list1 is None:         ### Checks if list1 is empty
        return list2          ### If yes returns list2 since merging/adding empty list to anything will return the second value
                              ### Ex: list1 = [],  list2 = [(1), (2), (3)] ------ list1 + list2 ==> [] + [(1), (2), (3)] - > [(1), (2), (3)]

    elif list2 is None:       ### Same here...
        return list1
    else:                     ### If neither of the lists are empty
        dummy = ListNode      ### a dummy Node is created to store the addition of both lists
        head = dummy          ### The head/starting point of the list is set --> None since dummy Node is empty/None

    while list1 and list2 is not None:  ### While the our head/starting point has not yet reached the end which is None
        if list1.val < list2.val:       ### Checks if first value of first Node in list1 is smaller than the first value of first Node in list2
            head.next = list1           ### If yes the head/starting point is now set to that Node ----- so from head = None --> head = (1)
            list1 = list1.next          ### the head/starting point of list1 is now set to the next Node which is (2)
        else:
            head.next = list2           ###
            list2 = list2.next
        head = head.next

    if list1 is not None:
        head.next = list1

    elif list2 is not None:
        head.next = list2

    return dummy.next

