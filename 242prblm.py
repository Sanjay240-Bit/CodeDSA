class Solution:
    def isAnagram(self, s, t):
        hashMap = {}

        for x in t:
            if x in hashMap:
                hashMap[x] = hashMap[x] + 1
            else:
                hashMap[x] = 1

        for x in s:
            if x in hashMap:
                hashMap[x] = hashMap[x] - 1
            else:
                return False

        for x in hashMap:
            if hashMap[x] != 0:
                return False

s = input("Enter first string: ")
t = input("Enter second string: ")


solution = Solution()
result = solution.isAnagram(s, t)

print(f"they are {result} anagrams")