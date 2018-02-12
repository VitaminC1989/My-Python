#image_to_text2.0 此版本功能简单，追求运行速度
from PIL import Image
import subprocess

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

#将Android手机截屏并把所截图片发送至电脑本地保存
def adb():
     #subprocess.check_output("adb shell screencap -p /sdcard/screen.png")
     subprocess.check_output("adb shell screencap -p /sdcard/screen.png")
     subprocess.check_output("adb pull /sdcard/screen.png")



#剪裁出图片中包含问题的部分，保存为question.png
def image_machining(img,box):
    im = Image.open(img)
    question = im.crop(box)
    question.save('question.png','PNG')


img = 'screen.png' 
box = (53,346,1020,634)
url = ''
adb()
image_machining(img, box)
wd = image_to_string('question.png',True,'-l chi_sim')
wd = wd.replace('\n','')
wd = wd.replace(' ','')
cmd  = 'start chrome https://www.baidu.com/s?wd='+wd[2:-1]
subprocess.check_output(cmd,shell=True)  