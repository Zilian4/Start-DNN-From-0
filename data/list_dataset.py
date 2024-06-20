from torch.utils.data import Dataset
import cv2
import numpy as np
class ListDataset(Dataset):
    def __init__(self,args,is_train):
        super(self,ListDataset)

        if is_train:
            data_list = args.train_list
        else:
            data_list = args.val_list
        
        infos = [line.split() for line in open(data_list).readlines()]
        self.img_paths = [info[0] for info in infos]
        self.label_paths = [info[1] for info in infos]

    def preprocess(self,img,label):
        img = img.transpose((2,0,1).astype(np.float32))
        return img,label
    
    def __len__(self):
        return len(self.img_paths)
    
    def __getitem__(self, index):
        img = cv2.imread(self.img_paths[index])
        label = cv2.imgread(self.label_paths[index])
        img, label = self.preprocess(img, label)
        return img, label