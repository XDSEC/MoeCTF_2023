from secret import flag
from attachments import salt

from torchvision import transforms
from PIL import Image



def get_img_by_label(label) -> Image.Image:
    pass


def init_model():
    pass


labels = []
for i in range(len(flag)):
    labels.append((ord(flag[i]) + salt[i])%1000)

model = init_model()

normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    normalize,
])

for i, label in enumerate(labels):
    img = get_img_by_label(label)
    img.save('imgs/' + str(i) + '.png')
    img_tensor = transform(img).unsqueeze(0)
    assert model(img_tensor).argmax().item() == label

print('Data generation finished.')



# Hints:

#  > You don't need to train your own model.

#  > Nearly half of the flag content is meaningful, no need for flag submission if your flag is meaningless.

#  > Please wrap your flag with moectf{} manually.

#  > If you're not getting the correct flag, try to use a more accurate model.
#    In my testing, Bottleneck3463 worked but the inferior one didn't.
#    Or, maybe you should think about converting numeric labels to human-readable text labels,
#    and check if your model is working properly.