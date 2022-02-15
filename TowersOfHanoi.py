# Set up node class

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value


# Set up stack class


class Stack:
    def __init__(self, name):
        self.size = 0
        self.top_item = None
        self.limit = 1000
        self.name = name

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            print("No more room!")

    def pop(self):
        if self.size > 0:
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        print("This stack is totally empty.")

    def peek(self):
        if self.size > 0:
            return self.top_item.get_value()
        print("Nothing to see here!")

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def get_name(self):
        return self.name

    def print_items1(self):
        pointer = self.top_item
        print_list = []
        while (pointer):
            print_list.append(pointer.get_value())
            pointer = pointer.get_next_node()

        return "{0} Stack: ".format(self.get_name())
        #print("{0} Stack:\n {1}".format(self.get_name(), print_list))


    def print_items2(self):
        pointer = self.top_item
        print_list = []
        while (pointer):
            print_list.append(pointer.get_value())
            pointer = pointer.get_next_node()
        print_list.reverse()
        return "{}".format(print_list)


print("\nLet's play Towers of Hanoi!!")

# Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

# Set up the Game
num_disks = int(input("\nHow many disks do you want to play with? \n"))
while num_disks < 3:
    num_disks = int(input("\nEnter a number greater than or equal to 3. \n"))

for n in range(num_disks, 0, -1):
    left_stack.push(n)

num_optimal_moves = 2 ** num_disks - 1
print("\nThe fastest you can solve this game is in {x} moves.".format(x=num_optimal_moves))


# Check disks in left stack: left_stack.print_items()

# Get User Input
def get_input():
    choices = [stack.get_name()[0] for stack in stacks]

    while True:

        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print("Enter {letter} for {name}.".format(letter=letter, name=name))

        user_input = input("").upper()

        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]


# Play the Game

num_user_moves = 0

while (right_stack.get_size() != num_disks):
    print("\n\n\n... Current Stacks ...\n")
    left1 = left_stack.print_items1()
    left2 = left_stack.print_items2()
    mid1 = middle_stack.print_items1()
    mid2 = middle_stack.print_items2()
    right1 = right_stack.print_items1()
    right2 = right_stack.print_items2()

    print(left1, mid1, right1)
    print(left2, "       ", mid2, "        ", right2)

    while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input()
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()

        if from_stack.get_size() == 0:
            print("\n\nInvalid Move. Try Again.")
        elif to_stack.get_size() == 0 or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        else:
            print("\n\nInvalid Move. Try Again.")

print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(num_user_moves,
                                                                                               num_optimal_moves))
