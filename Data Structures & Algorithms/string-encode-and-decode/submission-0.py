class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for s in strs:
            encodedStr += str(len(s)) + "#" + s
        return encodedStr

    def decode(self, s: str) -> List[str]:
        print(s)
        strsArray = []
        pos = 0;
        while (pos < len(s)):
            hashIndex = s.find("#", pos)
            length = int(s[pos:hashIndex])
            currStr = s[(hashIndex +1):(hashIndex+1+length)]
            strsArray.append(currStr)
            pos = hashIndex + length + 1
        return strsArray
