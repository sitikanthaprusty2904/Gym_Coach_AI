from abc import ABC, abstractmethod
import math

class BaseExercise(ABC):
    def __init__(self):
        self.reps=0
        self.stage=None


    def calculate_angle(self, a, b, c):
        ax,ay=a[0]-b[0], a[1]-b[1]
        cx,cy=c[0]-b[0], c[1]-b[1]
        dot=ax*cx+ay*cy
        mag_a=(ax**2+ay**2)**0.5
        mag_c=(cx**2+cy**2)**0.5

        if mag_a*mag_c==0:
            return 0.0
        angle=math.acos(max(-1,min(1,dot/(mag_a*mag_c))))
        return math.degrees(angle)


    def get_point(self, landmark,idx):
        return (landmark[idx].x, landmark[idx].y)

    @abstractmethod
    def process(self, landmark):
        pass

    @abstractmethod
    def reset(self):
        pass

    
