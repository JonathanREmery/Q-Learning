import numpy as np

R = np.matrix([[-1, -1, 0, -1, -1, -1],
			   [-1, -1, -1, 0, 0, 100],
			   [0, -1, -1, 0, 0, -1],
			   [-1, 0, 0, -1, -1, 100],
			   [-1, 0, 0, -1, -1, -1],
			   [-1, 0, -1, 0, -1, 100]])

Q = np.matrix(np.zeros([6, 6]))

gamma = 0.8

def available_actions(state):
		current_state_row = R[state]
		avail_actions = np.where(current_state_row >= 0)[1]
		return avail_actions

def sample_next_action(av_actions):
		next_action = int(np.random.choice(av_actions, 1))
		return next_action

def update(current_state, action, gamma):
	max_index = np.where(Q[action] == np.max(Q[action]))[1]

	if max_index.shape[0] > 1:
		max_index = int(np.random.choice(max_index, size=1))
	else:
		max_index = int(max_index)
	max_value = Q[action, max_index]

	Q[current_state, action] = R[current_state, action] + gamma * max_value

def best_action(state):
	ba = np.where(Q[state] == np.max(Q[state]))[1]
	if ba.shape[0] > 1:
		ba = int(np.random.choice(ba, size=1))
	else:
		ba = int(ba)
	return ba

initial_state = 1

available_act = available_actions(initial_state)

action = sample_next_action(available_act)

update(initial_state, action, gamma)

for i in range(10000):
	current_state = np.random.randint(0, int(Q.shape[0]))
	available_act = available_actions(current_state)
	action = sample_next_action(available_act)
	update(current_state, action, gamma)

for i in range(5):
	if best_action(i) != 5:
		a = best_action(i)
		b = [best_action(i)]
		while a != 5:
			a = best_action(a)
			b.append(a)
		print b
	else:
		print best_action(i)
