# -*- coding: utf-8 -*-

from PIL import Image
import os, cv2, random

def add_hat(img, out, factor=1.4):
	hats = ['data/hats/'+fn for fn in os.listdir('data/hats/') if fn.endswith('.png')]
	face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
	faces = face_cascade.detectMultiScale(
	    cv2.cvtColor(cv2.imread(img),cv2.COLOR_BGR2GRAY),
	    scaleFactor=factor,minNeighbors=1,minSize=(5,5),flags=cv2.CASCADE_SCALE_IMAGE)
	bg = Image.open(img)
	for (x,y,w,h) in faces:
		idx = random.randint(0,len(hats)-1)
		hat = Image.open(hats[idx]).convert('RGBA')
		hat = hat.resize((int(w*factor),int(h*factor)))
		pos = (x,y-int(h*factor/2))
		bg.paste(hat,pos,hat)
	bg.save(out)

if __name__ == '__main__':
	add_hat('data/img.jpg','data/out.png')
