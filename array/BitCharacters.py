class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        bits_set = ('0', '10', '11')
        is_one_bit = False
        index = 0
        while index < len(bits):
            if index + 1 < len(bits):
                character = str(bits[index]) + str(bits[index + 1])
                if character not in bits_set:
                    index += 1
                else:
                    index += 2
            elif str(bits[index]) in bits_set:
                is_one_bit = True
                index += 1
            else:
                index += 1

        return is_one_bit


print(Solution().isOneBitCharacter([1, 0, 0]))
