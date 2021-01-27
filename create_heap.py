class MinHeap:
  def __init__(self):
    self.heap_list = [None]
    self.count = 0
    
  def add(self, element):
    print("Adding {element} to {list}.".format(element = element, list = self.heap_list))
    self.count +=1
    self.heap_list.append(element)
    self.heapify_up()
