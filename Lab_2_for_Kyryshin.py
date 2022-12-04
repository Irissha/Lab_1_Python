import json
filename = "user_settings.txt"
myfile = open(filename, mode = 'w', encoding = 'Latin-1')

player1 = {
  'PlayerName': "Donald Trump",
  'Score': 345,
  'awards': ["OR", "NV", "NY"]
}

player2 = {
  'PlayerName': "Clinton Hillary",
  'Score': 346,
  'awards': ["WI", "TX", "MI"]
}
myplayears = []
myplayears.append(player1)
myplayears.append(player2)

# ---------- SAVE by JSON -----------

json.dump(myplayers, myfile)
myfile.close()
