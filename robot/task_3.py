import robot

r = robot.rmap()
r.lm('task3')


def task():
        for _ in range (3):
                r.rt()
                r.rt()
                r.dn()
                r.up()
        r.rt()
        r.rt()

        
r.start(task)

