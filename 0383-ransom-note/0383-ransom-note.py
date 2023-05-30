class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        noteMap = {}; magMap = {}
        for i in ransomNote:
            if noteMap.get(i):
                noteMap[i] += 1
            else:
                noteMap[i] = 1
        for i in magazine:
            if magMap.get(i):
                magMap[i] += 1
            else:
                magMap[i] = 1
        for i in noteMap:
            if noteMap.get(i) > magMap.get(i):
                return False
        return True
                
        