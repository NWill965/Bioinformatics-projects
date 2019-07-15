'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

#FrequentWords finds which strings of length k are most frequent in the Genome (Text).
def FrequentWords(Text, k):
    words=[]
    freq = FrequencyMap (Text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key]==m:
            words.append(key)
    return words
    
#FrequencyMap creates a dictionary of strings of length k appearing in the genome, and the number of times they appear.
def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
        for i in range(n-k+1):
            if Text[i:i+k] == Pattern:
                freq[Pattern] = freq[Pattern] + 1

    return freq


