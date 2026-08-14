team = {
    'CSK':{
        'captain': 'Dhoni', 
        'players': 18}, 
    'MI': {
        'captain': 'Rohit', 
        'players': 17}
    }

team["GT"]={'captain':'Hardik Pandya',"players":16}

for name, info in team.items():
    print(f"{name}:{info['captain']}")
