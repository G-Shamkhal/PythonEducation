class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None


class Queue:
    def __init__(self):
        self.start = None
        self.end = None

    def pop(self):
        if self.start is None:
            raise IndexError("Очередь пуста")
        val = self.start.data
        self.start = self.start.nref
        if self.start:
            self.start.pref = None
        else:
            self.end = None
        return val

    def push(self, val):
        new_node = Node(val)
        if self.end is None:
            self.start = self.end = new_node
        else:
            self.end.nref = new_node
            new_node.pref = self.end
            self.end = new_node

    def insert(self, n, val):
        if n < 0:
            raise ValueError("Индекс не может быть отрицательным")
        new_node = Node(val)
        if n == 0:
            new_node.nref = self.start
            if self.start:
                self.start.pref = new_node
            self.start = new_node
            if self.end is None:
                self.end = new_node
        else:
            current = self.start
            for _ in range(n - 1):
                if current is None:
                    raise IndexError("Индекс вне диапазона")
                current = current.nref
            if current is None:
                raise IndexError("Индекс вне диапазона")
            new_node.nref = current.nref
            new_node.pref = current
            if current.nref:
                current.nref.pref = new_node
            current.nref = new_node
            if current == self.end:
                self.end = new_node

    def print(self):
        current = self.start
        result = []
        while current:
            result.append(current.data)
            current = current.nref
        print(" <-> ".join(map(str, result)))


# Пример использования
queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.print()
print(queue.pop())
queue.print()
queue.insert(1, 4)
queue.print()
