# 24 = Swap Nodes in pairs

if not head:
            return []
        
        actual_head = head
        new_head = head.next
        
        first = head
        while first:
            #create two varaibles first and second
            #remove first from while, rather use head
            #remove both first.next and second.next
            #in the beginning of while loop, get the second item
            second = first.next
            first.next = second.next.next
            second.next = first
            
            first = first.next
            print('now current = ', first)
            if first:
                second = first.next
            else:
                second = None
            
        return new_head
