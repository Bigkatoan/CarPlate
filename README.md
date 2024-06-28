# CarPlate

Test on python 3.9.15, using anaconda.

## How to use.

create new environment name yolo.
```
conda create -n yolo python=3.9.15 -y
```
activate environment.
```
conda activate yolo
```

clone the project.
```
git clone https://github.com/Bigkatoan/CarPlate.git
```

move to project.
```
cd CarPlate
```

install environment.
```
pip install -r requirements.txt
```

run jupyter
```
jupyter-lab
```

# Fix Issue.

if you run on windows or not working put this line in head.
```
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
```
