import robot

r = robot.rmap()
r.lm('task4')


def task():
        while r.fr():
                r.rt()
                
        while r.fu():
                r.up()
        r.dn()
        r.lt()
        
        for _ in range(3):
                for _ in range(5):
                        r.pt()
                        r.dn()
                        r.lt()
                r.rt(5)
                r.up(3)


r.start(task)
