import model_torch
import modules_torch
import _utils_torch
from _utils_torch import *
import loss

def preprocessing(base_dir, train_dir, test_dir):
    data_dir = base_dir
    
    X_train = []
    Y_train = []
    for item in tqdm(train_dir):
        sam_img = data_dir + '/' + item + '/img.nii'
        sam_mask = sam_img.replace('img', 'mask')
    
        sam_img = sitk.ReadImage(sam_img)
        sam_mask = sitk.ReadImage(sam_mask)
    
        assert sam_img.GetSize() == sam_mask.GetSize()
    
        sam_img = sitk.GetArrayFromImage(sam_img)
        sam_mask = sitk.GetArrayFromImage(sam_mask)
        sam_img = normalize_dcm(sam_img)
        print(sam_img.min(), sam_img.max(), sam_img.dtype)
        
        for _slice in range(len(sam_img)):
            X_train.append(sam_img[_slice,...])
            Y_train.append(sam_mask[_slice,...])
    
    X_test = []
    Y_test = []
    for item in tqdm(test_dir):
        sam_img = data_dir + '/' + item + '/img.nii'
        sam_mask = sam_img.replace('img', 'mask')
    
        sam_img = sitk.ReadImage(sam_img)
        sam_mask = sitk.ReadImage(sam_mask)
    
        assert sam_img.GetSize() == sam_mask.GetSize()
    
        sam_img = sitk.GetArrayFromImage(sam_img)
        sam_mask = sitk.GetArrayFromImage(sam_mask)
        sam_img = normalize_dcm(sam_img)
        print(sam_img.min(), sam_img.max(), sam_img.dtype)
        
        for _slice in range(len(sam_img)):
            X_test.append(sam_img[_slice,...])
            Y_test.append(sam_mask[_slice,...])
    
    X_train = np.array(X_train)
    Y_train = np.array(Y_train)
    
    X_test = np.array(X_test)
    Y_test = np.array(Y_test)

    return X_train, Y_train, X_test, Y_test