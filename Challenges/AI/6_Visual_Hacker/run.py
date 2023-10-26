from transform import transform
from model import L2CS
from PIL import Image



def InitModel(checkpoint_path):
    # Load model
    return None

def get_pitch_yaw(original_img, model):
    # img: PIL.Image
    # model: L2CS
    # return pitch, yaw

    def raw_data_process(gaze_pitch, gaze_yaw):
        # gaze_pitch, gaze_yaw: torch.Tensor
        # return processed pitch, yaw
        return 0, 0

    gaze_pitch, gaze_yaw = model(transform(original_img))
    return raw_data_process(gaze_pitch, gaze_yaw)

def grometry_transform(pitch, yaw):
    # Covert pitch, yaw to intersection point on the input screen
    return 0, 0