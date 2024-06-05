class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        intNum1 = 0
        digits = pow(10, len(num1) - 1)
        for ch in num1:
            intNum1 = intNum1 + digits * (ord(ch) - 48)
            digits = digits / 10
        print(intNum1)

        intNum2 = 0
        digits = pow(10, len(num2) - 1)
        for ch in num2:
            intNum2 = intNum2 + digits * (ord(ch) - 48)
            digits = digits / 10
        print(intNum2)

        return (intNum1 * intNum2)


print(Solution().multiply("2", "3"))
print(Solution().multiply("20", "300"))
print(Solution().multiply("123456789", "987654321"))
