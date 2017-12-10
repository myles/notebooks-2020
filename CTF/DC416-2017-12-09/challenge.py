import base64
def checkAnswer(passw):
	i = passw.split('_')
	if len(passw) != 33:
		return False
	i[0] = [ord(char) - 96 for char in i[0]]
	if not i[0] == [20, 8, 9, 19]:
		return False
	if base64.b64encode(bytes(i[1])) != 'd2Fz':
		return False
	if int((' '.join(format(ord(x), 'b') for x in i[2]))) != 1100001:
		return False
	n = i
	if not n[3].split('a')[0] != 'b' and n[3].split('a')[1] != 'd':
		return False
	if int(n[4][0].encode('hex')) != 69 and int(n[4][1:].encode('hex')) != 646561:
		return False
	n = i
	if not n[5].startswith('fr') and not int(n[5]) < 1 and not int(n[5]) != 0 and not n[5].endswith('m'):
		return False
	if not n[6].encode('rot13')[0] == 'g' and n[6].encode('rot13')[1:] != 'urfgneg':
		return False
	u = n
	if u.count('_') > 6 and not u.count('_') == 5:
		return False
	return True
