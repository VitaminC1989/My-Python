import os
from PIL import Image
from selenium import webdriver
import subprocess
import question_operation
import  re

box=(36,256,680,430)
MI3_box=(53,346,1020,634)
HUWEI_Phone_box=(37,193,682,430)
Redmi_Note_4X_box=(52,339,1028,643)
#box=Redmi_Note_4X_box
box=HUWEI_Phone_box

save_addrA = 'A.png'
save_addrB = 'B.png'
save_addrC = 'C.png'
cmd = ''

#打开浏览器 输入URL进行搜索
def search(cmd):
    subprocess.check_output(cmd,shell=True)  

#使用Tesseract识别图片中文字
def image_to_string(img, cleanup=True, plus=''):
    # cleanup为True则识别完成后删除生成的文本文件
    # plus参数为给tesseract的附加高级参数
    subprocess.check_output('tesseract ' + img + ' ' +
                            img + ' ' + plus, shell=True)  # 生成同名txt文件
    text = ''
    with open(img + '.txt', 'r',encoding='utf-8') as f:
        text = f.read().strip()
    #if cleanup:
        #os.remove(img + '.txt')
    return text

#过滤识别出的字符串 去掉无效字符
def text_filter(text):
    str = text
    res = re.findall(r'[1-9]\d*.', str)
    str = str.replace(res[0],'')
    str = str.replace('?','')
    str = str.replace(' ','')
    str = str.replace('\n','')
    #return str[2:] 
    return str



#剪裁出图片中包含问题的部分，保存为question.png
def image_machining(img,box):
    im = Image.open(img)
    question = im.crop(box)
    save_addr = 'question.png'
    question.save(save_addr,'PNG')
    return save_addr

def question_machining(img,box,save_addr):
    im = Image.open(img)
    question = im.crop(box)
    question.save(save_addr,'PNG')
    return save_addr

#截图screen.png中的A B C 三个选项并分别保存为A.png、B.png、C.png
def image_machining_options(img):
    optionA=(118,445,598,523)
    save_addrA = 'A.png'
    question_machining(img, optionA, save_addrA)

    optionB=(115,560,595,641)
    save_addrB = 'B.png'
    question_machining(img, optionB, save_addrB)

    optionC=(120,678,604,758)
    save_addrC = 'C.png'
    question_machining(img, optionB, save_addrC)     

#将Android手机截屏并把所截图片发送至电脑本地保存
def adb():
     subprocess.check_output("adb shell screencap -p /sdcard/screen.png")
     subprocess.check_output("adb shell screencap -p /sdcard/screen.png")
     subprocess.check_output("adb pull /sdcard/screen.png")


#截取出问题部分并识别其中的文字 
def run_question(img):
    save_addr = image_machining(img, box)
    text = image_to_string(save_addr,True,'-l chi_sim')
    return text_filter(text)

#截取出3个选项部分并识别其中的文字 
def run_option(img):
    question_operation.image_machining_options(img)
    qa = image_to_string(save_addrA,True,'-l chi_sim')
    qb = image_to_string(save_addrB,True,'-l chi_sim')
    qc = image_to_string(save_addrC,True,'-l chi_sim')


adb()
img = 'screen.png'
wd = run_question(img)
#run_option(img)

cmd  = 'start chrome https://www.baidu.com/s?wd='+wd
search(cmd)














    