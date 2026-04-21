
import numpy as np
from torch.utils.data import Dataset

class FashionDataset(Dataset):
    """User-defined class to build a dataset using PyTorch's Dataset class."""

    def __init__(self, data, transform=None):
        """Initialize variables."""
        self.fashion_MNIST = list(data.values)
        self.transform = transform

        label = []
        image = []

        for row in self.fashion_MNIST:
            # first column is the label
            label.append(row[0])
            image.append(row[1:])
        self.labels = np.asarray(label)
        # Image dimensions: 28 x 28 x 1 (grayscale).
        self.images = np.asarray(image).reshape(-1, 28, 28, 1).astype("float32")

    def __getitem__(self, index):
        label = self.labels[index]
        image = self.images[index]

        if self.transform is not None:
            image = self.transform(image)

        return image, label

    def __len__(self):
        return len(self.images)
