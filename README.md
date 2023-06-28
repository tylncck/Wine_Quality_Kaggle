# Wine Quality Kaggle Competition 
Tabular Wine Quality Dataset

**Contributors:** *Onur Taylan Cicek, Ahmet Tunahan Tas*

## Dataset
The dataset provided with an Open License. More descriptions can be found [here](https://www.kaggle.com/competitions/playground-series-s3e5/data)

## Feature Generation
The original dataset comes with 27 columns (22 decimals, 2 integers and 3 id columns). Using all relevant variables inside the dataset, we generated new features by pairwise adding, dividing or multplying existing variables. More details about the feature generation can be found in notebooks_scripts\scripts\data_load.py file. 

## Model Training
We tried different classification models with hyperparameter tuning. During the parameter tuning, we generated our own scorer (namely Quadratic Weighted Kappa) to decide on the best parameters. 