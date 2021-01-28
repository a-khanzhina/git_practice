class MinHeap:
  def __init__(self):
    self.heap_list = [None]
    self.count = 0
    
  # HEAP HELPER METHODS
  def parent_idx(self, idx):
    return idx // 2

  def left_child_idx(self, idx):
    return idx * 2

  def right_child_idx(self, idx):
    return idx * 2 + 1

  # END OF HEAP HELPER METHODS  
  
  def add(self, element):
    print("Adding {element} to {list}.".format(element = element, list = self.heap_list))
    self.count +=1
    self.heap_list.append(element)
    self.heapify_up()
    
  
