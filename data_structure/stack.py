from typing import Any

class Stack():
    def __init__(self) -> None:
        self.arr = []
        self.top = -1

    def is_empty(self) -> bool:
        return self.top == -1

    def push(self, x) -> str:
        self.arr.append(x)
        self.top += 1
        return "Success"

    def peek(self) -> Any:
        if self.is_empty():
            return None
        return self.arr[self.top]

    def pop(self) -> Any:
        if self.is_empty():
            return None
        ans = self.arr[self.top]
        self.top -= 1
        del self.arr[-1]
        return ans

    def size(self) -> int:
        return self.top+1


if __name__ == '__main__':
    stk = Stack()
    print('Peek stack: ', stk.peek())
    print('Pop stack: ', stk.pop())
    print('Push stack: ', stk.push(1))
    print('Stack size: ', stk.size())
    print('Peek stack: ', stk.peek())
    print('Push stack: ', stk.push('Hello'))
    print('Push stack: ', stk.push({'One': '1'}))
    print('Stack size: ', stk.size())
    print('Pop stack: ', stk.pop())
    print('Pop stack: ', stk.pop())
    print('Pop stack: ', stk.pop())
    print('Pop stack: ', stk.pop())
    print('Stack size: ', stk.size())
