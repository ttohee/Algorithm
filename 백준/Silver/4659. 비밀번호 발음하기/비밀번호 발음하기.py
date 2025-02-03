import sys

arr = sys.stdin.read().split()[:-1]
vowels = ['a', 'e', 'i', 'o', 'u']

def notContainVowel(p):
    return not any(v in p for v in vowels)
        
def threeInARow(p):
    for i in range(1, len(p)-1):
        if (p[i-1] in vowels) == (p[i] in vowels) == (p[i+1] in vowels):
            return True
    return False

def twoSameWord(p):
    for i in range(1, len(p)):
        if p[i] == p[i-1] and p[i] not in ['e', 'o']:
            return True
    return False

for p in arr:
    if notContainVowel(p) == threeInARow(p) == twoSameWord(p):
        print(f'<{p}> is acceptable.')
    else:
        print(f'<{p}> is not acceptable.')