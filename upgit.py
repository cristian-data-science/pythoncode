import subprocess
process1 = subprocess.Popen(["git", "add","."])
process = subprocess.Popen(["git", "commit","-m", "'Another update'"])
process = subprocess.Popen(["git", "push","-u", "origin", "master"])
print(process1)
process.wait()

#print("Upload completed!")
#process = subprocess.Popen(["git", "status"])
#print = 