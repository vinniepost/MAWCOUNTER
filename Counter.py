count=0
file = open("Transcription.txt", "rt")
maw =file.readlines()
for line in maw:
    if "met andere woorden" in line:
        count=count+1
print(count)
file.close()