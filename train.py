import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO
from ultralytics import RTDETR

if __name__ == '__main__':
    model = YOLO('') # loading configuration files
    model.load('') # loading pretrain weights
    model.train(data='',  # loading the dataset profile
                cache=False,
                imgsz=640,
                epochs=300,
                batch=32,
                patience=200,
                close_mosaic=10,
                workers=0,
                optimizer='SGD', # using SGD
                # resume='', # last.pt path
                # amp=False # close amp
                # fraction=0.2,
                project='', # loading the generation path
                name='',
                )
