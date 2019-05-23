'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

# Input:  Strings Genome and symbol
# Output: SymbolArray(Genome, symbol). This symbol array will show the number of bases (Symbol) between each index. By running this 'window' shaped search
## pattern through the whole genome, we can find where C is lowest and so potentially the leading strand. 
Genome = "AAAAGGGG"
symbol = "A"
def SymbolArray(Genome, symbol):
    # type your code here)
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return array



## PatternCount searches for a particular string within a larger string, and returns the number of occurences. 
##If integrated into a for loop, it will look for that string within a repeating window moving through a yet larger string.
def PatternCount(symbol, ExtendedGenome):
    
    count = 0
    for i in range(len(ExtendedGenome)-len(symbol)+1):
        if ExtendedGenome[i:i+len(symbol)] == symbol:
            count = count+1
    return count 
