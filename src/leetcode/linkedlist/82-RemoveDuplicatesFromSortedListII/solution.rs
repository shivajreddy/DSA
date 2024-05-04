#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { val, next: None }
    }
}

struct Solution {}

impl Solution {
    pub fn delete_duplicates(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut prev = &mut head;
        let mut curr = head.as_mut().map(|node| &mut node.next);

        while let Some(node) = curr {
            if let Some(nxt) = remove_duplicates(node) {
                *prev = Some(Box::new(ListNode {
                    val: node.val,
                    next: nxt,
                }));
                prev = &mut prev.as_mut().unwrap().next;
            }
            curr = curr.as_mut().and_then(|node| node.next.as_mut());
        }
        head
    }
}

fn remove_duplicates(mut node: &mut ListNode) -> Option<Box<ListNode>> {
    let mut prev = node;
    let mut curr = &mut prev.next;

    while let Some(nxt) = curr {
        if nxt.val == prev.val {
            prev.next = nxt.next.take();
        } else {
            prev = nxt;
        }
        curr = prev.next.as_mut();
    }

    Some(Box::new(ListNode {
        val: nxt.val,
        next: nxt.next.take(),
    }))
}

fn main() {
    println!("going to run Solution");
}
