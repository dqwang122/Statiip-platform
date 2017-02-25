from numpy import *

def load():
	a1 = 0.921731890092
	a2 = 0.517412935323
	three_state = [[0.35294118,0.97880184,0.41538462],[0.40909091,0.94821429,0.72972973],[0.37894737,0.96326531,0.52941176]]
	name = ['Recall', 'Precision', 'F']
	five_state = [[0.53125,0.33939394,0.55047319,1.,0.54395604],[0.42805755,0.33939394,0.87688442,0.00729927,0.43421053],[0.47410359,0.33939394,0.67635659,0.01449275,0.48292683]]
	return a1, a2, name, three_state, five_state