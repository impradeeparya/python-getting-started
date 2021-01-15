class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.limit = 10000
        self.hash_set = [[] for bucket in range(self.limit)]

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucket_number = key % self.limit
        bucket = self.hash_set[bucket_number]
        is_present = key in bucket
        if not is_present:
            bucket.append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucket_number = key % self.limit
        bucket = self.hash_set[bucket_number]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        bucket_number = key % self.limit
        bucket = self.hash_set[bucket_number]
        return key in bucket


obj = MyHashSet()
obj.add(1)
print(obj.contains(1))
obj.remove(2)
print(obj.contains(1))
