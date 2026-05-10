class Solution:

    def encode(self, strs: List[str]) -> str:
        count = ""
        encoded = ""
        idx = 0

        for s in strs:
            encoded += s
            count += str(len(s)) + " "
            idx += len(s)

        encoded += count + str(idx)
        return encoded


    def decode(self, s: str) -> List[str]:
        idx = 0
        k = 1
        for i in range(len(s) - 1, 0, -1):
            if s[i] == " ":
                break
            idx += int(s[i]) * k
            k *= 10
        
        count = s[idx:].split(" ")
        count.pop()
        count = list(map(int, count))
        print(count)

        decoded = []
        i = 0
        for c in count:
            decoded.append(s[i:i + c])
            i += c
        
        return decoded

