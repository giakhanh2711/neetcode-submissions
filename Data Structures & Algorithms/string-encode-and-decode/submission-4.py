class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + " " + s
        return encoded

    def decode(self, s: str) -> List[str]:
        print(s)
        decoded = []
        i = 0
        while i < len(s):
            l = ""
            while s[i] != " ":
                l += s[i]
                i += 1

            l = int(l)
            decoded.append(s[i + 1:i + 1 + l])
            i += l + 1
        
        return decoded
