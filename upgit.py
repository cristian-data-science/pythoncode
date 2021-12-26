import subprocess
process = subprocess.Popen(["git", "add","."])
process = subprocess.Popen(["git", "commit","-m", "'Another update'"])
process.wait()

print("Completed!")