class Stack:

    def __init__(self):
        self.__length=0
        self.__stacks=[]
        
    def push(self,data):
        self.__stacks.insert(self.__length,data)
        self.__length+=1
        
    def pop(self):
        if self.__length==0:
            return "Stack is empty: Can't POP"
        data=self.__stacks[self.__length-1]
        self.__length-=1
        return data
        
    def peek(self):
        if self.__length==0:return -1
        return self.__stacks[self.__length-1]
    
    def print_stack(self):
        if self.__length==0:
            return "stack is empty:"
        for i in range(self.__length):
            print(self.__stacks[i])
            
    def size(self):
        return self.__length
    
    def isEmpty(self):
        return True if self.__length==0 else False
		
def next_greater(arr):
    for i in arr:
        if st.peek()==-1:
            st.push(i)
        elif i>st.peek():
            while st.peek()<i and st.peek()!=-1:
                print(st.peek(),i)
                st.pop()
            st.push(i)
        else:
            st.push(i)
		
