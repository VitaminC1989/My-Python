from PIL import Image
import re
optionA=(118,445,598,523)
optionB=(115,560,595,641)
optionC=(120,678,604,758)

save_addrA = 'A.png'
save_addrB = 'B.png'
save_addrC = 'C.png'

def question_machining(img,box,save_addr):
    im = Image.open(img)
    question = im.crop(box)
    question.save(save_addr,'PNG')
    return save_addr

  

def image_machining_options(img):
	question_machining(img, optionA, save_addrA)
	question_machining(img, optionB, save_addrB)
	question_machining(img, optionC, save_addrC)	
