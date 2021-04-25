#讀取對話紀錄
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as original:
		for o in original:
				lines.append(o)
	return lines			


#文字轉換
def convert(lines):
	new = []
	person = None
	for line in lines:
		if 'Allen' in line:
			person = 'Allen'
			continue
		elif 'Tom' in line:
			person = 'Tom'
			continue
		if person:	
			new.append(person + ': ' + line)
	return new

#寫入檔案
def write_file(filename, lines):
	with open(filename, 'w', encoding='utf-8') as file:
		for line in lines:
			file.write(line)


def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()