import os

	
def read_file(filename):
	chat = []
	#編碼改為utf-8-sig為去除編碼訊息\ufeff
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for c in f:
			chat.append(c.strip().split(' '))
	return chat		
	

def recover(chat):
	rchat = []
	allen_words_count = 0
	allen_sticker_count = 0
	allen_picture_count = 0
	viki_words_count = 0
	viki_sticker_count = 0
	viki_picture_count = 0
	for c in chat:
		time = c[0]
		name = c[1]
		if name == 'Viki':
			for m in c[2:]:
				if m == '貼圖':
					viki_sticker_count += 1
				elif m == '圖片':
					viki_picture_count += 1
				else:
					viki_words_count += len(m)
		elif name == 'Allen':
			for m in c[2:]:
				if m == '貼圖':
					allen_sticker_count += 1
				elif m == '圖片':
					allen_picture_count += 1
				else:
					allen_words_count += len(m)
	print('Viki說了', viki_words_count,'個字' )
	print('傳送了', viki_sticker_count,'個貼圖' )
	print(viki_picture_count,'張圖片' )
	print('Allen說了', allen_words_count,'個字' )
	print('傳送了', allen_sticker_count,'個貼圖' )
	print(allen_picture_count,'張圖片' )

		
def main(filename):
	chat = read_file(filename)
	rchat = recover(chat)


while True:
	filename = input('請輸入您要查詢的檔名(或輸入q結束）: ')
	if filename == 'q' :
		break
	elif filename == 'Q':
		break
	else:
		filename = filename + '.txt'
		if os.path.isfile(filename):
			print('找到檔案了')
			main(filename)
		else:
			print('沒有找到檔案喔')
			break