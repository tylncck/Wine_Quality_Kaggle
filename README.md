# Wine Quality Kaggle Competition 
Tabular Wine Quality Dataset

**Contributors:** *Onur Taylan Cicek, Ahmet Tunahan Tas*

## Dataset
The dataset provided with an Open License. More descriptions can be found [here](https://www.kaggle.com/competitions/playground-series-s3e5/data)

## Feature Generation
The original dataset comes with 27 columns (22 decimals, 2 integers and 3 id columns). Using all relevant variables inside the dataset, we generated new features by pairwise adding, dividing or multplying existing variables. More details about the feature generation can be found in notebooks_scripts\scripts\data_load.py file. 

## Model Training
We tried different classification models with hyperparameter tuning. During the parameter tuning, we generated our own scorer (namely Quadratic Weighted Kappa) to decide on the best parameters. 

The best model appears to be XGBoost and we suppose due to huge number of new features generated, model overfits in the training dataset. However, our scorer on own test dataset returned QWK very close to 0.5. Therefore, we stopped searching for further development for the model. The result is not ideal for us but it's better to know where to stop because there is no room for the model to improve further as it has Accuracy = 1 and QWK = 1.