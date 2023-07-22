# Arguments: key, value
# Returns: nothing
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def display(self):
       pass

class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None] * size

    def _hash(self, key):
        """
            key: The key to be hashed.
        """
        return hash(key) % self.size

    def set(self, key, value):
        index = self._hash(key)

        if self._buckets[index] is None:
          self._buckets[index] = Node(key, value)
          self.size += 1
        else:
          current = self._buckets[index]
          while current:
              if current.key == key:
                  current.value = value
                  return
              current = current.next
          new_node = Node(key, value)
          new_node.next = self._buckets[index]
          self._buckets[index] = new_node
          self.size += 1

    def get(self, key):
        index = self.hash(key)

        current = self._buckets[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next

        raise KeyError(key)

    def has(self, key):
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def keys(self):
        keys_list = []
        for node in self._buckets:
            current = node
            while current:
                keys_list.append(current.key)
                current = current.next
        return keys_list



"""
Arguments: key
Returns: value
"""
# hash the key

""" check if there is no data (node) at the index in the hashtable (self.buckets). If index is empty, the key is not present in the hashtable, and the method should return None. """
""" if there is at least one node present at the index, there is the possibility of a collision. Traverse the linked list at that index to find the key/value pair.
"""
""" create current variable and initialize it to the first node in the linked list at the index. This allows traversal of the linked list from the head node to find the key/value match.
"""
