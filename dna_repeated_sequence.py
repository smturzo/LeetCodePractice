# LeetCode Problem asked at GenBio AI.
def findRepeatedDnaSequences(s: str):
    seen, repeated = set(), set()
    print('Length of sequence: ',len(s))
    for i in range(len(s) - 9):
        # first part is getting the substring of length 10
        substring = s[i:i+10]
        print(substring)
        # second part is checking if it has been seen before
        # if seen, add to a set called repeated
        if substring in seen:
            # for the first nothing is in seen, nothing gets added to repeated
            repeated.add(substring)
        # else, add to a set called seen
        # for the first iteration, it adds the first 10 characters to seen
        seen.add(substring)
    # third part is returning the list of repeated sequences
    return list(repeated)

# Test Usage
s1 = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
findRepeatedDnaSequences(s1)

s2 = "AAAAAAAAAAAAA"
print(findRepeatedDnaSequences(s2))
