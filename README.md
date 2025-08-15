# object-recognition-model

sudo apt update && sudo apt upgrade -y
sudo apt install -y build-essential git curl wget unzip pkg-config


# Descargar e instalar Miniconda (x86_64)
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
bash ~/miniconda.sh  # seguir prompts (aceptar, instalar a $HOME/miniconda3)
source ~/.bashrc
conda update -n base -c defaults conda -y


conda create -n vision_proj python=3.10 -y
conda activate vision_proj
python -m pip install --upgrade pip setuptools wheel

# antes de instalar TF, instalar utilidades comunes
conda install -c conda-forge cmake pkg-config -y
pip install opencv-python-headless==4.* numpy pandas matplotlib tqdm scikit-learn jupyterlab
# herramientas que requieren compilación:
sudo apt install -y libgl1-mesa-glx libglib2.0-0
# pycocotools (puede requerir cython & build tools)
pip install cython
pip install git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI


pip install mlflow albumentations seaborn
# Detector YOLO (ultralytics)
pip install ultralytics
# If using detectron2 / faster rcnn: follow their install guide (conda + torch + detectron2)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu  # CPU fallback
# Para TensorFlow:
pip install tensorflow
