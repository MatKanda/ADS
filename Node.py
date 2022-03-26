class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def get_data(self):
        return self.data

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right
