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
  
  def retrieve_min(self):
    if self.count == 0:
      print("No items in heap")
      return None
  	
    min = self.heap_list[1]
    print("Removing: {0} from {1}".format(min, self.heap_list))
    self.heap_list[1] = self.heap_list[self.count]
    self.heap_list.pop()
    self.count -= 1
    print("Last element moved to first: {0}".format(self.heap_list))
    return min
  
  def add(self, element):
    print("Adding {element} to {list}.".format(element = element, list = self.heap_list))
    self.count +=1
    self.heap_list.append(element)
    self.heapify_up()
    
  def heapify_up(self):
    print("Heapifying up")
    idx = self.count
    while self.parent_idx(idx) > 0:
      child = self.heap_list[idx]
      parent = self.heap_list[self.parent_idx(idx)]
      if parent > child:
        print("swapping {0} with {1}".format(parent, child))
        self.heap_list[idx] = parent
        self.heap_list[self.parent_idx(idx)] = child
      idx = self.parent_idx(idx)
    print("Heap Restored {0}".format(self.heap_list))
  
