struct ListNode {
    val: i32,
    next: Option<Box<ListNode>>,
}

fn reverse_linked_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    // let mut prev: Option<Box<ListNode>> = None;
    let mut prev = None;

    let mut curr = head;

    while let Some(node) = curr {
        // Move curr to curr.enxt
        curr = node.next.take();

        // prev <- node
        node.next = prev;

        // prev now points to curr-node
        prev = Some(node);
    }

    prev
}
