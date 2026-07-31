
class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded_str = ""
        for s in strs:
            # Format: <length_of_string>#<string>
            encoded_str += f"{len(s)}#{s}"
        return encoded_str

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        res = []
        i = 0
        
        while i < len(s):
            # Find the delimiter '#' starting from index i
            j = i
            while s[j] != '#':
                j += 1
            
            # Extract the length of the next string
            length = int(s[i:j])
            
            # Read the exact number of characters based on length
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            # Move pointer i to the start of the next encoded block
            i = end
            
        return res
