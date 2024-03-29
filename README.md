# pkg_pyknnclassifier

![Logo](https://raw.githubusercontent.com/UBC-MDS/Group16_knnmodel/main/img/logo_reduced.png)

[![Documentation Status](https://readthedocs.org/projects/pkg-pyknnclassifier/badge/?version=latest)](https://pkg-pyknnclassifier.readthedocs.io/en/latest/?badge=latest)
![ci-cd](https://github.com/UBC-MDS/Group16_knnmodel/actions/workflows/ci-cd.yml/badge.svg)
[![codecov](https://codecov.io/gh/UBC-MDS/Group16_knnmodel/branch/main/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/Group16_knnmodel)

## 📄 About 
Our package, named "pkg_pyknnclassifier," is a comprehensive toolkit for k-Nearest Neighbors (k-NN) modeling and evaluation. It offers a set of functions designed to facilitate various aspects of working with k-NN algorithms, from loading the data, calculating distances to making predictions and assessing model performance. We aim to simplify the process by providing essential functionalities for data manipulation, model evaluation, and scaling.

Our documentaion: (https://pkg-pyknnclassifier.readthedocs.io/en/latest/)

## 📦 Functions
This package consists of six functions and explained as below:
- `data_loading(str_of_path, target_column)`: This function loads data from a file path and split into features and target.
- `scaling(df, impute_strategy, scale_method)`: This function allows user to choose the method of data imputation and scaling, and apply to the data.
- `calculate_distance(obs_1, obs_2, method = "Euclidean")`: This function calculates the Euclidean distance between two observations for the KNN model to find the similarity score.
- `find_neighbors(labeled_arraies, unlabeled_array, k)`: This function finds the indices of the 'k' nearest neighbors in a collection of labeled arrays to a given unlabeled array. 
- `predict(train_X, train_y, unlabel_df, pred_method, k)`: This function predicts the labels of the unlabled observations based on the similarity score calculated from Euclidean distance.
- `evaluate(y_true, y_pred, metric='accuracy')`: This function calculates evaluation metrics such as accuracy, precision, recall, and F1 score for a k-NN model based on true labels and predicted labels.

## 🛠️ Installation

### Option 1 (For Users)
_The package has been published to PYPI, we could use pip install_
1. Create and activate a virtual environment using conda
```bash
$ conda create --name <env_name> pip -y
$ conda activate <env_name>
```
2. Install the package using the command below
```bash
$ pip install pkg_pyknnclassifier
```

### Option 2 (For Developers)
_To sucessfully run the following commands of installation, we would need `conda` and `poetry`, guide included in the link ([conda](https://docs.conda.io/projects/miniconda/en/latest/), [poetry](https://python-poetry.org/docs/))_

1. Clone this repository
``` bash
$ git clone git@github.com:UBC-MDS/Group16_knnmodel.git
```
2. Direct to the root of this repository
3. Create a  virtual environment in Conda with Python by the following commands at terminal and activate it:
```bash
$ conda create --name pyknnclassifier python=3.11 -y
```
```bash
$ conda activate pyknnclassifier
```
4. Install this package via poetry, run the following command. 
```bash
$ poetry install
```

## ✅ Testing
To test this package, please run the following command from the root directory of the repository:
```bash
$ pytest tests/
```
- branch coverage could be viewed with the following command:
```bash
$ pytest --cov-branch --cov=pkg_pyknnclassifier
```

## Usage
To successfully use our knn model to predict the target, please first ensure you have followed the instruction of installation, and then run the following line in a python notebook.
```python
from pkg_pyknnclassifier.data_loading import data_loading
from pkg_pyknnclassifier.scaling import scaling
from pkg_pyknnclassifier.predict import predict
from pkg_pyknnclassifier.evaluate import evaluate

features, target = data_loading('data/toy_dataset.csv', 'Target')
X_scaled = scaling(features, 'median', 'StandardScaler')
pred = predict(X_scaled, target, X_scaled, 'hard', 3)
accuracy_result = evaluate(target, pred, metric='accuracy')
print("Accuracy:", accuracy_result)
```

## 📚 Package Integration within the Python Ecosystem
`pkg_pyknnclassifier`, while acknowledging the robustness and the capabilities of [scikit-learn's KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html), aims to offer a specialized and streamlined toolkit tailored explicitly for k-Nearest Neighbors classification tasks. As a lightweight and focused alternative, `pkg_pyknnclassifier` serves users who seek a concise package that offers calculating distances, making predictions, and evaluating k-NN models functions. While scikit-learn covers a broader spectrum of machine learning algorithms, `pkg_pyknnclassifier` provides a more specialized package, potentially appealing to those who prefer a tailored implementation of their k-NN workflows. 

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## 📜 License

`pkg_pyknnclassifier` was created by "Bill Wan, Sho Inagaki, Shizhe Zhang, Weiran Zhao". It is licensed under the terms of the MIT license.

## 📚 Credits

`pkg_pyknnclassifier` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
