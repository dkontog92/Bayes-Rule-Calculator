#Bayes Rule calculator with specific hypothesis
import numpy as np

def GetHypothesis():
	flag = True
	while flag:
		try:
			NumOfHypothesis = int(input('Enter the number of hypothesis: '))
			flag = False
		except ValueError:
			print('Oops!  That was no valid number.  Try again...')
	
	print('\nNumber of hypotheses are %d.\n' % NumOfHypothesis)
	return NumOfHypothesis


def GetPriors(num_hypothesis):
	Priors = []
	print('Prior probabilities need to sum to 1! Make sure they do!\n')

	for i in range(num_hypothesis):
		Priors.append(float(input('Enter prior probability for hypothesis %d P(H%d): '%((i+1),(i+1)))))
	
	print('\nThe prior probabilities are:')
	print(Priors)
	
	return np.array(Priors)

def GetEventConditionals(num_hypothesis):
	
	conditionals = np.zeros(num_hypothesis)
	for i in range(len(conditionals)):
		conditionals[i] = float(input('Enter the probability of the event given hypothesis %d P(E|H%d): '% ((i+1),(i+1))))
	
	print(conditionals)
	return conditionals
	
	
def MoreEvents(posterior, num_hypothesis):
	flag = True
	while flag:
		moreEvents = input('Is there another event (y/n)? ')
		if moreEvents == 'y':
			conds = GetEventConditionals(num_hypothesis)
			posterior = posterior*conds/np.sum(posterior*conds)
			print('\nThe new posterior probabilities for the hypotheses are:')
			print(posterior)
		elif moreEvents == 'n':
			flag = False
		else:
			print('Wrong input. Answer again with "y" or "n".')



if __name__ == '__main__':
	
	num_hypothesis = GetHypothesis()
	priors = GetPriors(num_hypothesis)
	conds = GetEventConditionals(num_hypothesis)
	
	posterior = priors*conds/np.sum(priors*conds)
	print('\nThe posterior probabilities for the hypotheses are:')
	print(posterior)
	
	MoreEvents(posterior, num_hypothesis)
	

			
			
	
	
	
	

