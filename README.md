# 04_Lung_Nodule_Segmentation

![tree_image-0](https://github.com/user-attachments/assets/f1899150-a622-4b2d-b6a3-663e27150dd0)
![tree_image-1](https://github.com/user-attachments/assets/5d74f149-064f-4464-a5f6-090355f8714a)

## Data Description
1. 학습용 데이터 (/Data/...)
   - 원본 CT 영상 (/Data/LCTSC-Test-##-###/###.nii)
   - 폐 결절 분할 마스크 (/Data/LCTSC-Test-##-###/###-label.nii)

## Code Description
## Training.ipynb
  - 네트워크 학습 코드
## Evaluation.ipynb
  - 네트워크 성능 평가 및 척추 분할 결과 가시화
  - 학습완료 된 모델 가중치 (/Code/output/model_final.pth)
## model_torch.py
  - Residual UNet 아키텍쳐 빌드
## Preprocessing.py
  - Intensity windowing
  - 입력 이미지 해상도 조정
## _utils_torch.py
  - 네트워크를 구성에 필요한 부속 코드
  - Preprocessing 이후 데이터를 모델에 입력하기 위한 처리
## modules.torch.py
  - 네트워크를 구성에 필요한 부속 코드
## loss.py
  - 학습용 loss 함수 코드
  - Dice loss
  - Focal loss
