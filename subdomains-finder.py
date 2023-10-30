import os


os.system(f"amass enum --passive -df domain.txt -o OutPut.txt")



os.system(f"subfinder -dL domain.txt -o subfinder.txt")

os.system(f"cat domain.txt | assetfinder -subs-only | tee assetfinder.txt")


os.system(f"dnsgen domain.txt | tee dnsgen.txt")


os.system(f"cat OutPut.txt assetfinder.txt domain.txt > out.txt")


os.system(f"cat out.txt | httprobe | tee 200.txt")


os.system(f"sort 200.txt | uniq > sub.txt")


with open("sub.txt", 'r') as f:
    print(f.read())
os.system(f"rm OutPut.txt  subfinder.txt assetfinder.txt  dnsgen.txt  out.txt  200.txt")

os.system(f"clear")
os.system(f"open sub.txt")
