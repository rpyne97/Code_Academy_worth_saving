# Input:  Strings Pattern and Text along with an integer d
# Output: A list containing all starting positions where Pattern appears as a substring of Text with at most d mismatches
# This function matches a Pattern sequence to a Test sequence if there are less than or equal to d mismatches
def ApproximatePatternMatching(Text, Pattern, d):
    positions = []
    n = len(Text)
    k = len(Pattern)
    # range is the length of the text minus the k-mer length plus 1
    for i in range(n - k + 1):
        # subroutine HammingDistance function
        # change arguments to match a k-mer pattern against a string instead of a single letter
        # Basically, slide Pattern across Text and append
        distance = HammingDistance((Pattern), (Text[i:i + k]))
        if distance <= d:
            positions.append(i)
    return positions


# Input:  Two strings p and q
# Output: An integer value representing the Hamming Distance between p and q.
def HammingDistance(p, q):
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count


# Print the hamming distance (number of mismatches in two strings) represented here by variable count
print(count)
