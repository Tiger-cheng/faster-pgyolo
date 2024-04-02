import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('') # select your model.pt path
    model.predict(source='',         #  loading the image to be detected
                project='runs/detect',
                name='exp',
                save=True,
                visualize=True # visualize model features maps
                )
