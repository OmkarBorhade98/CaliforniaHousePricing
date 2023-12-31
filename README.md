# CaliforniaHousePricing
This project intends to build a ML Model to predict House Prices in California bsaed on dataset [California housing dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html). Exploratory Data Analysis was performed on this dataset to identify possible outliers and to understand the relation between the given independant features. A linear regression model was trained to fit through the dataset. A webpage with an interface which demands input values of independent features to predict the possible house price is also included in the scope of this project.

### Software and Tools Requirement
1. [anaconda](https://www.anaconda.com/)
2. [python](https://www.python.org/)
3. [scikit-learn](https://scikit-learn.org/stable/)
4. [numpy](https://numpy.org/)
5. [pandas](https://pandas.pydata.org/)
6. [seaborn](https://seaborn.pydata.org/index.html)
7. [jupyter](https://jupyter.org/)
8. [ipykernel](https://ipython.readthedocs.io/en/stable/index.html#)
9. [pickle](https://docs.python.org/3/library/pickle.html)
10. [flask](https://flask.palletsprojects.com/en/3.0.x/)
11. [matplotlib](https://matplotlib.org/)

### Installation
create conda environment will all requirements by command:
```
conda env create -f environment.yml
```

### Folder structure
```
CaliforniaHousePricing
│   .gitignore
│   app.py
│   environment.yml
│   LICENSE
│   README.md
│   regmodel.pkl
│   Regression_Impl.ipynb
│   scaling.pkl
├───templates
│       debug.log
│       index.html

```

### File info
- ```Regression_Impl.ipynb``` Jupyter notebook implementing EDA and Linear Regression
- ```app.py``` Webpage backend
- ```templates\index.html``` Webpage Frontend