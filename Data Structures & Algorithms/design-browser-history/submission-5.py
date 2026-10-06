class ListNode:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next


class BrowserHistory:
    #Two stakcs problem
    # def __init__(self, homepage: str):
    #     self.back_history = [homepage]
    #     self.front_history = []
        
    # def visit(self, url: str) -> None: #visit url from the current page 
    #     self.back_history.append(url)
    #     self.front_history = []
        
    # def back(self, steps: int) -> str: #Move step back in the history
    #     while steps and len(self.back_history)>1:
    #         self.front_history.append((self.back_history.pop()))
    #         steps -=1
    #     return self.back_history[-1]

    # def forward(self, steps: int) -> str: 
    #     while steps and self.front_history:
    #         self.back_history.append(self.front_history.pop())
    #         steps -= 1
    #     return self.back_history[-1]

    #Doubly Linked List

    def __init__(self, homepage:str):
        self.cur = ListNode(homepage)

    def visit(self, url: str) -> None: 
        #visit url from the current page
        self.cur.next = ListNode(url, self.cur)
        self.cur = self.cur.next

    def back(self, steps: int) -> str: 
        #Move step back in the history
        while self.cur.prev and steps>0:
            self.cur = self.cur.prev
            steps -=1
        return self.cur.val

    def forward(self, steps: int) -> str:
        while self.cur.next and steps>0:
            self.cur = self.cur.next
            steps -=1
        return self.cur.val 



