from torchvision import transforms



transform = transforms.Compose([
    transforms.Resize(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])



# For the preprocess of the image:
#  > NO NEED for face detection or alignment
#  > Only model(transform(original_RGB_image)) is ready to go