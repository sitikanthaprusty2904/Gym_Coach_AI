from core.base_exercise import BaseExercise

class SquatDetector(BaseExercise):
    DOWN_THRESHOLD=100
    UP_THRESHOLD=160
    MIN_VISIBILITY=0.7

    LEFT_HIP=23
    LEFT_KNEE=25
    LEFT_ANKLE=27
    LEFT_SHOULDER=11
    RIGHT_HIP=24
    RIGHT_KNEE=26
    RIGHT_ANKLE=28
    RIGHT_SHOULDER=12

    def __init__(self):
        super().__init__()

    def reset(self):
        self.reps=0
        self.stage=None

    def process(self, landmark):
        l_hip=self.get_point(landmark,self.LEFT_HIP)
        l_knee=self.get_point(landmark,self.LEFT_KNEE)
        l_ankle=self.get_point(landmark,self.LEFT_ANKLE)
        l_angle=self.calculate_angle(l_hip,l_knee,l_ankle)

        r_hip=self.get_point(landmark,self.RIGHT_HIP)
        r_knee=self.get_point(landmark,self.RIGHT_KNEE)
        r_ankle=self.get_point(landmark,self.RIGHT_ANKLE)
        r_angle=self.calculate_angle(r_hip,r_knee,r_ankle)

        left_visibility=landmark[self.LEFT_HIP].visibility
        right_visibility=landmark[self.RIGHT_HIP].visibility

        if left_visibility > right_visibility :
            knee_angle=l_angle
            hip_idx,knee_idx,ankle_idx,shoulder_idx=self.LEFT_HIP,self.LEFT_KNEE,self.LEFT_ANKLE,self.LEFT_SHOULDER
        else:
            knee_angle=r_angle
            hip_idx,knee_idx,ankle_idx,shoulder_idx=self.RIGHT_HIP,self.RIGHT_KNEE,self.RIGHT_ANKLE,self.RIGHT_SHOULDER

        if knee_angle<90 and self.stage!="down":
            self.stage="down"
        elif knee_angle>=90 and self.stage=="down":
            self.stage="up"
            self.reps+=1

        shulder=self.get_point(landmark,shoulder_idx)
        hip=self.get_point(landmark,hip_idx)
        knee=self.get_point(landmark,knee_idx)
        back_angle=self.calculate_angle(shulder,hip,knee)


        key_landmarks_visibility=min(landmark[hip_idx].visibility, landmark[knee_idx].visibility, landmark[shoulder_idx].visibility) >= self.MIN_VISIBILITY

        if key_landmarks_visibility:
            if knee_angle<self.DOWN_THRESHOLD:
                self.stage="down"
            elif knee_angle>self.UP_THRESHOLD and self.stage=="down":
                self.stage="up"
                self.reps+=1
            
        if self.stage=="down":
            depth_status="Good" if knee_angle<self.DOWN_THRESHOLD else "Too high"
        elif self.stage=="up":
            depth_status="Good" if knee_angle>self.UP_THRESHOLD else "Too Deep"
        else :
            depth_status="N/A"

        return {
            "rep_count": self.reps,
            "knee_angle": int(knee_angle),
            "back_angle": int(back_angle),
            "depth_status": depth_status
        }

        

    
    