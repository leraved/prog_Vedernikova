import robot

r = robot.rmap()
r.lm('task2')


def task():
	pass
	for _ in range(5):
		r.up()
		r.pt()
		r.up()
		r.rt()
		r.pt()
		r.rt()
		r.dn()
		r.pt()
		r.dn()
		r.lt()
		r.pt()
		r.rt()
		r.rt()


r.start(task)

