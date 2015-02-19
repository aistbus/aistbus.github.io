import sys

def load_sched(path, route):
	departures = []
	with open(path) as f:
		for line in f:
			for hmstr in line.split():
				hstr, mstr = hmstr.split(":")
				#print int(hstr), int(mstr)
				sec_from_epoch = int(hstr) * 60 + int(mstr)
				departures.append({"time": sec_from_epoch, "route": route})

		#print departures
		return departures;

r0 = load_sched("data/namiki.txt", 0)
r1 = load_sched("data/ara.txt", 1)
r2 = load_sched("data/sakura.txt", 2)
r3 = load_sched("data/minami-junkan-east.txt", 3)
r4 = load_sched("data/aist.txt", 4)
#print r1,r2,r3,r4

allroutes = r0 + r1 + r2 + r3 + r4

print sorted(allroutes, key=lambda x: x["time"])
