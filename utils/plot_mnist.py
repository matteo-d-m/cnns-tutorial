import matplotlib.pyplot as plt

import torchvision
import torchvision.transforms as transforms


N_CLASSES = 10
SAMPLES_PER_CLASS = N_CLASSES

training_dataset = torchvision.datasets.MNIST(root="classifier data", 
                                              train=True, 
                                              download=True, 
                                              transform=transforms.ToTensor())

samples_to_plot = []
for class_label in range(N_CLASSES):
    class_samples = [sample for sample in training_dataset if sample[1] == class_label]
    samples_to_plot += class_samples[:SAMPLES_PER_CLASS]

_, ax = plt.subplots(figsize=(10,6),
                     nrows=N_CLASSES,
                     ncols=N_CLASSES)
for i in range(ax.size):
    current_axis = ax.flat[i]
    current_axis.imshow(1- samples_to_plot[i][0].squeeze(),
                        cmap="gray")
    current_axis.set_xticks(ticks=[],
                            labels=[])
    current_axis.set_yticks(ticks=[],
                            labels=[])
    current_axis.axis("off")
plt.show()