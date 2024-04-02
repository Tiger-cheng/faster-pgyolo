# Faster-pgyolo
# Description
We propose a novel hardware-friendly approach utilizing YOLOv8s, specifically designed for detecting floating debris with unmanned cleaning vessels.
# **Experimental** **setup**
This study's experimental configuration was established on a system operating under Windows 10, outfitted with an i5-13600KF CPU and an NVIDIA GeForce RTX 3060 GPU. Experiments were accelerated using CUDA 11.8, based on PyTorch 2.1.0, with identical hyper-parameters for  training and validation. 
# Download
The dataset and models have been released. [Data&Model]( https://pan.baidu.com/s/1qhYJRb5mjvoP3HmhhTjw9w?pwd=vs12 )
- The experiments utilize the unmanned vessel perspective inland water floating debris data  set released by Orcauboat.
- This model includes the redesigned detection layer of the YOLOv8s model, enhancements to the C2f module, the incorporation of a novel attention mechanism, and improvements to the neck feature fusion network. 

### Dataset Directory Structure
~~~
dataset/
├── images
│   ├── train
│   └── val
└── labels
    ├── train
    └── val

-> data/dataset.yaml
~~~
### xml_txt
~~~
import os  
import glob  
import xml.etree.ElementTree as ET  
  
xml_file=r'' #xml_file  
  
l=['bottle']  
  
def convert(box,dw,dh):  
    x=(box[0]+box[2])/2.0  
  y=(box[1]+box[3])/2.0  
  w=box[2]-box[0]  
    h=box[3]-box[1]  
  
    x=x/dw  
    y=y/dh  
    w=w/dw  
    h=h/dh  
  
    return x,y,w,h  
  
def f(name_id):  
    xml_o=open(r''%name_id)  # original xml file path
    txt_o=open(r''%name_id,'w')  # the current txt file
  
    pares=ET.parse(xml_o)  
    root=pares.getroot()  
    objects=root.findall('object')  
    size=root.find('size')  
    dw=int(size.find('width').text)  
    dh=int(size.find('height').text)  
  
    for obj in objects :  
        c=l.index(obj.find('name').text)  
        bnd=obj.find('bndbox')  
  
        b=(float(bnd.find('xmin').text),float(bnd.find('ymin').text),  
  float(bnd.find('xmax').text),float(bnd.find('ymax').text))  
  
        x,y,w,h=convert(b,dw,dh)  
  
        write_t="{} {:.5f} {:.5f} {:.5f} {:.5f}\n".format(c,x,y,w,h)  
        txt_o.write(write_t)  
  
    xml_o.close()  
    txt_o.close()  
  
name=glob.glob(os.path.join(xml_file,"*.xml"))  
for i in name :  
    name_id=os.path.basename(i)[:-4]  
    f(name_id)
~~~
