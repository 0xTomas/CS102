class MaxHeap:
    # Initialise MaxHeap class, starting with an empty list and a count of zero.
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    # HEAP HELPER METHODS: indicate indices of parent and children within tree

    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1

    def child_present(self, idx):
        return self.left_child_idx(idx) <= self.count

    # END OF HEAP HELPER METHODS

    # Add elements to the heap by appending to the heap list.
    def add(self, element):
        self.count += 1
        print("Adding: {0} to {1}".format(element, self.heap_list))
        self.heap_list.append(element)
        self.heapify_up()

    # Reorganises list so that parent is not less than child.
    def heapify_up(self):
        print("Heapifying up")
        idx = self.count
        while self.parent_idx(idx) > 0:
            # The child is the last element, and the parent is its parent.
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]
            if parent < child:
                print("swapping {0} with {1}".format(parent, child))
                # The index of the child (the last) becomes the smaller parent value.
                self.heap_list[idx] = parent
                # The index of the parent now becomes the larger child value.
                self.heap_list[self.parent_idx(idx)] = child
            # Set the current index to that of the parent to move up the list.
            idx = self.parent_idx(idx)
        print("Heap Restored {0}".format(self.heap_list))

    def retrieve_max(self):
        if self.count == 0:
            print("No items in heap")
            return None
        # Max value is the root of the list (first element)
        max_value = self.heap_list[1]
        print("Removing: {0} from {1}".format(max_value, self.heap_list))
        # The root becomes the last element.
        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1
        # Remove the last element, now store at the root.
        self.heap_list.pop()
        print("Last element moved to first: {0}".format(self.heap_list))
        # Reorganise the list so that parents are larger than their children.
        self.heapify_down()
        return max_value

    def heapify_down(self):
        idx = 1
        # While there are children:
        while self.child_present(idx):
            print("Heapifying down!")
            larger_child_idx = self.get_larger_child_idx(idx)
            child = self.heap_list[larger_child_idx]
            parent = self.heap_list[idx]
            # In the case that the parent is small, swap these values.
            if parent < child:
                self.heap_list[idx] = child
                self.heap_list[larger_child_idx] = parent
            idx = larger_child_idx
        print("HEAP RESTORED! {0}".format(self.heap_list))
        print("")

    def get_larger_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            print("There is only a left child")
            return self.left_child_idx(idx)
        else:
            left_child = self.heap_list[self.left_child_idx(idx)]
            right_child = self.heap_list[self.right_child_idx(idx)]
            if left_child > right_child:
                print("Left child " + str(left_child) + " is larger than right child " + str(right_child))
                return self.left_child_idx(idx)
            else:
                print("Right child " + str(right_child) + " is larger than left child " + str(left_child))
                return self.right_child_idx(idx)