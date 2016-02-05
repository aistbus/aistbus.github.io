import sys

def load_sched(path):
	departures = []
	with open(path) as f:
		for line in f:
			hmstr, ttype = line.split()
			hstr, mstr = hmstr.split(":")
			sec_from_epoch = int(hstr) * 60 + int(mstr)
			departures.append({"time": sec_from_epoch, "route": ttype})
		#print departures
		return departures;

r0 = load_sched("data/tx.txt")

print sorted(r0, key=lambda x: x["time"])
