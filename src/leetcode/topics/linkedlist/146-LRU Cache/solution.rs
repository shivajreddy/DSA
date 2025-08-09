struct Node {
    key: i32,
    val: i32,
    next: Option<Box<Node>>,
    prev: Option<Box<Node>>,
}

impl Node {
    fn new(key: i32, val: i32) -> Self {}
}

struct DoubleLinkedList {}

struct LRUCache {}

impl LRUCache {}
