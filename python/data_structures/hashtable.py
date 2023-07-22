# Arguments: key, value
# Returns: nothing
class Node:
    def __init__(self, key, value):
        """
        Initialize a Node object.

        Args:
            key: The key for the node.
            value: The value associated with the key.
        """
        self.key = key
        self.value = value
        self.next = None

    def display(self):
        """
        The display method generates a formatted string containing the key and value of the Node.
        It is primarily used for debugging purposes and to visualize the content of the Node.

        Returns:
            str: A string representation of the Node in the format "[key, value]".
        """
        return f"[{repr(self.key)}, {repr(self.value)}]"


class Hashtable:
    def __init__(self, size=1024):
        """
        Initialize a Hashtable object.

        Args:
            size (int): The size of the hashtable (default is 1024).
        """
        self.size = size
        self._buckets = [None] * size

    def _hash(self, key):
        """
        Hashes the given key to an index within the range of the hashtable size.

        Args:
            key: The key to be hashed.

        Returns:
            int: The hashed index.
        """
        return hash(key) % self.size

    def set(self, key, value):
        """
        Sets the value associated with the given key in the hashtable.

        If the key already exists in the hashtable, its value will be updated.
        If there is a collision, a new node will be created and added to the linked list at the hashed index.

        Args:
            key: The key to be set.
            value: The value to be associated with the key.

        Returns:
            None
        """
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
        """
        Retrieve the value associated with the given key from the hashtable.

        Args:
            key: The key for which the value needs to be retrieved.

        Returns:
            The value associated with the key.

        Raises:
            KeyError: If the key is not found in the hashtable.
        """
        index = self._hash(key)

        current = self._buckets[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next

        raise KeyError(key)

    def has(self, key):
        """
        Check if the given key exists in the hashtable.

        Args:
            key: The key to check for existence in the hashtable.

        Returns:
            bool: True if the key is found, False otherwise.
        """
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def keys(self):
        """
        Get a list of all keys in the hashtable.

        Returns:
            list: A list containing all keys in the hashtable.
        """
        keys_list = []
        for node in self._buckets:
            current = node
            while current:
                keys_list.append(current.key)
                current = current.next
        return keys_list
