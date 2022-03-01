types = ['german', 'japanese', 'vegetarian', 'french', 'african', 'american', 'barbecue', 'czech', 'chinese', 'thai',
         'mexican', 'indian', 'cafe', 'pizza', 'italian']

restaurant_data = [['cafe', "Kinneret", '3', '3', '15 Power Ave.'],
                   ['japanese', 'Robatayaki Hachi','4', '5', '8 Hawthorne Ln.'],
                   ['vegetarian', 'BBQ Tofu Paradise', '2', '1', '22A King West'],
                   ['french', 'Le Bateau Rouge', '5', '4', '2 South Park Dr.'],
                   ['african', 'Khartoum Khartoum', '3', '2', '1566 Maple Rd.'],
                   ['american', "Sally's Diner", '4', '3', '96 College Blvd.'],
                   ['barbecue', 'Saucy Piggy', '3', '2', '623 Industrial Rd.'],
                   ['czech', 'Czech Point', '1', '4', '5567 Queen-Mary Rd'],
                   ['german', 'Der Speisewagen', '3', '5', '402 College Blvd.'],
                   ['chinese', 'Beijing Express', '2', '4', '38 Teutonic Ave.'],
                   ['thai', 'Satay Village', '4', '2', '12 High St.']]


# Create a base class to represent a linked list.
class LinkedList:
    def __init__(self):
        self.head = None

    def get_head_node(self):
        return self.head

    def visualise(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next_node
        nodes.append("None")
        print(" -> ".join(nodes))

    def insert_first(self, new_node):
        new_node = Node(new_node)
        new_node.set_next_node(self.head)
        self.head = new_node

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next_node


# Create a class that represents the nodes of the linked list.
class Node:
    def __init__(self, value, next_node=None):
        # Holds data:
        self.value = value
        # Points to next node:
        self.next_node = next_node

    # Gets the value of node:
    def get_value(self):
        return self.value

    # Gets the next node:
    def get_next_node(self):
        return self.next_node

    # Sets the next node:
    def set_next_node(self, next_node):
        self.next_node = next_node


# Insert food types into a linked list.
food_types_list = LinkedList()
for food_type in types:
    food_types_list.insert_first(food_type)


# Insert restaurant data into a linked list.
restaurant_data_list = LinkedList()
restaurant_sublist = LinkedList()

for food_type in types:

    for restaurant in restaurant_data:
        if restaurant[0] == food_type:
            print("Adding {0} to restaurant sublist.".format(restaurant[1]))
            restaurant_sublist.insert_first(restaurant)
        restaurant_data_list.insert_first(restaurant_sublist)

print("\nThese are the available restaurants:")
for node in restaurant_sublist:
    rest = node.get_value()
    print(rest[1])

selected_food_type = ""

# User interaction starts here:
while len(selected_food_type) == 0:
    user_input = str(input("\nWhat type of food would you like?\nType the beginning of that food type.").lower())
    matching_type = []
    food_type_head = food_types_list.get_head_node()
    while food_type_head is not None:
        if str(food_type_head.get_value()).startswith(user_input):
            matching_type.append(food_type_head.get_value())
        food_type_head = food_type_head.get_next_node()

    # Print list of matching food types:
    for food in matching_type:
        print(food)

    if len(matching_type) == 1:
        select_type = str(input("\nThe only matching types for your input is " + matching_type[0] +
                                ".\nDo you want to look at " + matching_type[0] + " restaurants? "
                                "Enter y for yes and n for no")).lower()

        if select_type == 'y':
            selected_food_type = matching_type[0]
            print("Selected Food Type: " + selected_food_type)
            for node in restaurant_sublist:
                rest = node.get_value()
                if rest[0] == selected_food_type:
                    print("--------------------------")
                    print("Name: " + rest[1])
                    print("Price: " + rest[2] + "/5")
                    print("Rating: " + rest[3] + "/5")
                    print("Address: " + rest[4])
                    print("--------------------------\n")