def read_next_line(lyrics):
    f = open(lyrics)
    f.seek(20)
    data=f.readlines()
    f.close()
    return data

print(read_next_line("lyrics.txt"))