rivers = {
	'nile':'egypt',
	'mississippi':'america',
	'seine':'france',
	'yucatan':'mexico'
}

for k,v in rivers.items():
	print(f"The {k.title()} is in {v.title()}")
print('\n')

for k in rivers:
	print(k.title())

print('\n')
for v in rivers.values():
	print(v.title())