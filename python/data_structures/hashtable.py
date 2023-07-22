# Arguments: key, value
# Returns: nothing
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        """
        Initialize a Node object.

        Args:
            key: The key for the node.
            value: The value associated with the key.
        """


class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None] * size

    def _hash(self, key):
        return hash(key) % self.size
        """
            int: The hashed index.

        Sets the value associated with the given key in the hashtable.

        If the key already exists in the hashtable, its value will be updated.
        If there is a collision, a new node will be created and added to the linked list at the hashed index.

        Args:
            key: The key to be set.
            value: The value to be associated with the key.

        Returns:
            None
        """
    def set(self, key, value):
        index = self._hash(key)

        if self._buckets[index] is None:
            self._buckets[index] = Node(key, value)
        else:
            current = self._buckets[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next

            new_node = Node(key, value)
            print(new_node)
            current.next = new_node



        """
        Retrieve the value associated with the given key from the hashtable.

        Args:
            key: The key for which the value needs to be retrieved.

        Returns:
            The value associated with the key.

        Raises:
            KeyError: If the key is not found in the hashtable.
        """
    def get(self, key):
        index = self._hash(key)

        current = self._buckets[index]
        while current:
            if current.key == key:
                print(current.value)
                return current.value
            current = current.next

        raise KeyError(key)



        """
        Check if the given key exists in the hashtable.

        Args:
            key: The key to check for existence in the hashtable.

        Returns:
            bool: True if the key is found, False otherwise.
        """
    def has(self, key):
        try:
            self.get(key)
            return True
        except KeyError:
            return False

        """
        Get a list of all keys in the hashtable.

        Returns:
            list: A list containing all keys in the hashtable.
        """
    def keys(self):
        keys_list = []
        for node in self._buckets:
            current = node
            while current:
                keys_list.append(current.key)
                current = current.next
        return keys_list

if __name__== "__main__":
    pass
