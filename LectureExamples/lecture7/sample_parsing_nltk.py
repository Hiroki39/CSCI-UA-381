import nltk

sentence = 'scientists think that any habitable areas on the planet are in the border region'.split(' ')

## sentence = 'scientists think that any scientists think in areas'.split(' ')

scientist_grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> NNS | DT NN | DT NNS | DT JJ NNS| DT NN NN | NP PP
VP -> VBP SBAR | VBP PP 
SBAR -> IN S
PP -> IN NP
DT -> 'any' | 'the'
NNS -> 'scientists' | 'areas'
NN -> 'planet' | 'border' | 'region'
JJ -> 'habitable'
VBP -> 'think' | 'are'
IN -> 'that' | 'on' | 'in'
""")

parser = nltk.ChartParser(scientist_grammar)

for tree in parser.parse(sentence):
	print(tree)

