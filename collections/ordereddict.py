from collections import OrderedDict



def main():
	sportTeams = [
		("royals", (18, 12)),
		("rockets", (24, 6)),
		("cardinalls", (20, 10)),
		("dragons", (22, 8)),
		("kings", (15, 15)),
		("chargers", (20, 10)),
		("jets", (16, 14)),
		("warriors", (25, 5)),
	]

	sortedTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True)

	teams = OrderedDict(sortedTeams)
	print(teams)

	tm, wl = teams.popitem(False)
	print("top team: ", tm, wl)

	for i, team, in enumerate(teams, start=1):
		print(i, team)
		if i == 4:
			break

	a = OrderedDict({"a": 1, "b": 2, "c": 3,})
	b = {"a": 1, "c": 3, "b": 2,}
	print("equality test: ", a == b)



if __name__ == "__main__":
	main()
