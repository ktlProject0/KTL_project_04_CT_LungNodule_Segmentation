# 04_Lung_Nodule_Segmentation

      ./KTL_project_04_CT_Lung_Nodule_Segmentation/
      |-- Code
      |   |-- .ipynb_checkpoints
      |   |   |-- 01.\ Training-checkpoint.ipynb
      |   |   |-- 02.\ Evaluation-checkpoint.ipynb
      |   |   |-- Preprocessing-checkpoint.py
      |   |   `-- _utils_torch-checkpoint.py
      |   |-- 01.\ Training.ipynb
      |   |-- 02.\ Evaluation.ipynb
      |   |-- Preprocessing.py
      |   |-- __pycache__
      |   |   |-- Preprocessing.cpython-39.pyc
      |   |   |-- _utils_torch.cpython-39.pyc
      |   |   |-- loss.cpython-39.pyc
      |   |   |-- model_torch.cpython-39.pyc
      |   |   `-- modules_torch.cpython-39.pyc
      |   |-- _utils_torch.py
      |   |-- loss.py
      |   |-- model_torch.py
      |   |-- modules_torch.py
      |   `-- output
      |       |-- model_final.pth
      `-- Data
          |-- RIDER-1129164940
          |   |-- img.nii
          |   `-- mask.nii
          |-- RIDER-1225316081
          |   |-- img.nii
          |   `-- mask.nii
          |-- RIDER-1286684383
          |   |-- img.nii
          |   `-- mask.nii
          |-- ...
          |   |-- ...
          |   `-- ...


## Data Description
1. 학습용 데이터 (/Data/...)
   - 원본 CT 영상 (/Data/RIDER-######/img.nii)
   - 폐 결절 분할 마스크 (/Data/RIDER-######/mask.nii)

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
