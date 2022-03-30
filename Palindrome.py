class Solution:
    def longestSubstring(self, S):
        # This function checks if a substring is a palindrome
        def Actual(self, indices):
            # n = Number of each letters in the substring; letters = number of letters that form a palindrome;
            # Ans [False: even number of letters; True: odd number of letters]; initial = length of substring
            # This function compares the position of the substring letters to position of letters in the original string S
            n = 0; letters = 0; Ans = 0; initial = indices[1]-indices[0]+1
            # For each letter in the dictionary Letters
            for key in Keys:
                # For each value in the array of positions corresponding to that letter
                for i in Letters[key]:
                    # if a position is contained within the substring, then increment n
                    if i <= indices[1] and i >= indices[0]:
                        n += 1
                # Update letters
                letters += n//2
                # Update Ans
                if n % 2 == 1:
                    Ans += 1 
                if Ans == 2:
                    Letters.pop(key); Keys.remove(key)
                    Ans -= 1
                n = 0
                
            # Total is the length of the longest palindrome possible in the substring
            Total = letters*2
            if Ans > 0:
                Total += 1
            # If Total equals the length of the substring, then the substring is a palindrome 
            if Total == initial:
                return [None, True]
            # Else, the longest palindrome might be of length Total, so return Total to be used to find that palindrome
            else:
                return [Total, False]   
        
        
        # This provides the dictionary of letters in the String which is used by the method Actual
        # xString stores each letter in the string; Letters is the dictionary to be created; Keys stores distinct letters in the string
        xString = []; xString[:0] = S; Keys = []; Letters = {}; N = len(S)
        # Populate the Letters dictionary
        for index in range(N):
            char = S[index]
            # Add the position of the letter to its position array in Letters
            if char in Letters:
                Letters[char].append(index)
            else:
                Letters[char] = [index]
                Keys.append(char)
        
        
        # This is the Main code which decides the longest palindrome possible
        # Mgc_index is the last resort! The length of shortest possible palindrome;
        # change = length of substring to be investigated for palindrome, it is initially set to the length of the string
        Mgc_index = 1; change = N;
        
        while change > 1:
            # Changes stores all the possible lengths of palindromes, so they can be investigated
            Changes = []
            # Iterates over the whole string, investigating substrings of length = change
            for i in range(0, N-change+1, 1):
                indices = [i, i+change-1]
                [Return1, Return2] = Actual(self, indices)
                # If a palindrome is found, return its length
                if Return2 == True:
                    return change
                # If no palindrome is found, update Changes
                Changes.append(Return1)
            
            # Investigate the next longest potential palindrome
            if len(Changes) > 0:
                change = max(Changes)
            else: 
                change -= 1
        return Mgc_index  
          
String = "africa"
S = Solution()
print(S.longestSubstring("vizfcfc"))
    
