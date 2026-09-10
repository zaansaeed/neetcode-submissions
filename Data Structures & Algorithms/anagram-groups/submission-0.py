class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alpha_to_idx = defaultdict(list)
        for i, string in enumerate(strs):
            key = [0]*26
            for char in string:
                
                key[ord(char)-97] += 1
            key = tuple(key)
            alpha_to_idx[key].append(i)
        
        answers = []

        for key, val in alpha_to_idx.items():
            temp_answer = []
            for idx in val:
                temp_answer.append(strs[idx])
            answers.append(temp_answer)
        return answers
        