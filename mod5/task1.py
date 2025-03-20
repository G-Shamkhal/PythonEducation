class Node:
    def __init__(self, data):
        self.data = data
        self.pref = None


class Stack:
    def __init__(self):
        self.end = None

    def pop(self):
        if self.end is None:
            raise IndexError("Стек пуст")
        val = self.end.data
        self.end = self.end.pref
        return val

    def push(self, val):
        new_node = Node(val)
        new_node.pref = self.end
        self.end = new_node

    def print(self):
        current = self.end
        result = []
        while current:
            result.append(current.data)
            current = current.pref
        print(" -> ".join(map(str, result[::-1])))


# Пример использования
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.print()
print(stack.pop())
stack.print()
