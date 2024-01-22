n = "Janhvi@5"
n.split()
c = 0
s = '[@_!#$%^&*()<>?/\|}{~:]' 
for i in range(len(n)):
	if n[i] in s:
		c += 1 
if c:
	print("string is not accepted")
else:
	print("string accepted")


