import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('runs/train/exp2/weights/best.pt')
    model.predict(source='',         #  loading the image to be detected
                project='runs/detect',
                name='exp',
                save=True,
                visualize=True # visualize model features maps
                )
