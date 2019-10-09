#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
from flask import Flask,render_template,request,send_from_directory
from conv import conv
import numpy as np
from PIL import Image
import imageio
app=Flask(__name__)
width_quality=640
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
@app.route("/",methods=['GET'])
def index():
        return render_template("upload.html")

@app.route("/upload", methods=['POST'])
def upload():
        target=os.path.join(APP_ROOT,"images/")
        print(target)
        if not os.path.isdir(target):
                os.mkdir(target)


        for file in request.files.getlist("file"):
                print(file)
                filename=file.filename
                destination= "/".join([target,"test.jpg"])
                print(destination)
                file.save(destination)
                print('this',destination)
                i=Image.open(destination)
                dim=i.size[0]/width_quality
                i = np.asarray(i.resize((width_quality,int(i.size[1]/dim)),Image.ANTIALIAS).convert("RGB"))
                #convert to gray
                img_gray=np.mean(i,axis=2,dtype=np.uint)
                edge_detection=([[2,1,2],[-0.5,0,0.5],[-2,-1,-2]])
                # Convert array to Image
                x=conv(img_gray,edge_detection)
                #imsave("/".join([target,"test.jpg"]),x)
                imageio.imwrite("/".join([target,"modifed_"+filename]), x)
        return send_from_directory("images","modifed_"+filename,as_attachment=True)


        
if __name__ == '__main__':
        app.run(port=5050,debug=True)


#%%
