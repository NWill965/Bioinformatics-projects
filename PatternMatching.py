'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''


 #PatternMatching does a similar job to PatternCount from the SymbolArray function; it looks for appearances of a 
 #particular string within a larger string. However, instead of just counting them, it creates a list of their indexes too.
def PatternMatching(Pattern, Genome):
    positions = [] 
    n = len(Genome)
    k = len(Pattern)
    for i in range (n-k+1):
        if Pattern == Genome[i:i+k]:
            positions.append(i)
    return positions
        
        
 

