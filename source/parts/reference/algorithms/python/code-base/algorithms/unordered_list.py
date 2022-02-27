class UnorderedList:
  # constructor
  def __init__(self):
    self.head = None
  
  # check if the list is empty
  def isEmpty(self):
    return self.head == None
 
  # insert item to be the first item of the list   
  def add(self, item):
    temp = Node(item)
    temp.setNext(self.head)
    self.head = temp
   
  # size of the list  
  def size(self):
    current = self.head
    count = 0
    while current != None:
      count += 1
      current = current.getNext()
      
    return count
    
  # find if item is in the list  
  def search(self, item):
    current = self.head
    found = False
    while current != None and not found:
      if current.getData() == item:
        found = True
      else:
        current = current.getNext()
        
    return found
    
  # remove item from the list  
  def remove(self, item):
    current = self.head
    previous = None
    found =False
    
    while not found:
      if current.getData() == item:
        found = True
      else:
        previous = current
        current = current.getNext()
        
    if previous == None:
      self.head = current.getNext()
    else:
      previous.setNext(current.getNext())

  # insert the item to be last element of list 
  def append(self, item):
    current = self.head
    temp = Node(item)
    while current != None:
      current = current.getNext()
    
    current.setNext(temp)
  
  # insert item in the pos-th of the list
  def insert(self, pos, item):
    current = self.head
    previous = None
    index = 0
    temp = Node(item)
    
    while current != None and index < pos:
      previous = current
      current = current.getNext()
      index += 1
    
    if pos == 0:
      temp.setNext(self.head)
      self.head = temp      
    else:
      if current == None:
        previous.setNext(temp)
      else:
        temp.setNext(current)
        previous.setNext(temp)
   
  # get index of item in the list    
  def index(self, item):
    current = self.head
    found = False
    index = 0
    
    while current != None and not found:
      if current.getData() != item:
        index +=1
        current = current.getNext()
      else:
        found = True
        
    if found:
      return index
    else:
      return "Not Found"
  
  # remove last item of the list     
  def pop(self):
    current = self.head
    previous = None
    
    if current == None:
      return "No item in list"
    
    while current.getNext() != None:
      previous = current
      current = current.getNext()
    
    previous.setNext(None)
    return current.getData()
      
  # remove item from the pos-th of the list
  def delete(self, pos):
    current = self.head
    previous = None
    index = 0
    
    if current == None:
      return "No item in list"
    
    while index < pos and current != None:
      previous = current
      current = current.getNext()
      index += 1
      
    if current == None:
      return "No item in list"
    else:
      if previous == None:
        self.head = current.getNext()
      else:
        previous.setNext(current.getNext())
      return current.getData()