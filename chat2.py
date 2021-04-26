#讀取對話紀錄
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as original:
		for o in original:
				lines.append(o.strip())
	return lines				

#文字計算
def count(lines):
	allen_word_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_image_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1		
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1	
			else:
				for m in s[2:]:
					viki_word_count += len(m)
	print('Allen 總共說了', allen_word_count, '個字')
	print('Allen 總共傳了', allen_sticker_count, '個貼圖')
	print('Allen 總共傳了', allen_image_count, '張圖片')

	print('Viki 總共說了', viki_word_count, '個字')
	print('Viki 總共傳了', viki_sticker_count, '個貼圖')
	print('Viki 總共傳了', viki_image_count, '張圖片')	
	

#寫入檔案
def write_file(filename, lines):
	with open(filename, 'w', encoding='utf-8') as file:
		for line in lines:
			file.write(line)


def main():
	lines = read_file('LINE-Viki.txt')
	lines = count(lines)
	#write_file('output.txt', lines)

main()	
