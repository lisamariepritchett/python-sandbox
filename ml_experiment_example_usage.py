from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import seaborn as sns

# Model Pre-Processing & Imputation
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, KBinsDiscretizer, Binarizer, OneHotEncoder, OrdinalEncoder, FunctionTransformer, OneHotEncoder, LabelBinarizer
from sklearn.impute import SimpleImputer

# Classification Models
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV

# Internal Libraries
from feature_encoding import greater_than_zero, is_true
from ml_experiment import MLData, MLExperiment, get_xgboost_gridsearch

#%% Set Up Global Experiment Conditions
# High level functions for this experiment
def get_data():
    return sns.load_dataset('titanic').reset_index()

#### Global Variables ####
# These are values used in the ML Model that are not expected to change between individual experiment conditions
# Multiple experiment conditions can be run to test, these global values are shared between them and not expected to change
EXPERIMENT_ID = 422
MODEL_NAME = 'prob_survival'
# get dates when splitting by date
# anchor_date = datetime.strptime('2022-10-30', '%Y-%m-%d').date()
# START_DATE = anchor_date - timedelta(days=180)
# VAL_START = anchor_date - timedelta(days=60)
# TEST_START = anchor_date - timedelta(days=30)
# END_DATE = anchor_date - timedelta(days=1)

TARGET = 'survived'
PKEY = 'index'

#%% Experiment 1: Initial Run of this Experiment
##### EXPERIMENT 1 : XGBOOST INITAL RUN #####
DESCRIPTION = 'Initial Run of this Experiment'

# These are names of columns that will be used in this iteration of the model
FLOAT_COLS = ['age', 'fare']
INT_COLS = ['sibsp', 'parch', 'pclass']
BOOL_COLS = ['adult_male', 'alone']
STRING_COLS = ['sex', 'embarked', 'who', 'deck', 'embark_town']

# build preprocessor
float_transformer = Pipeline(steps = [
  ('imputer', SimpleImputer(strategy="mean"))
])

integer_transformer = Pipeline(steps = [
  ('imputer', SimpleImputer(strategy="constant", fill_value = 0))
  , ('function_greater_than_zero', FunctionTransformer(np.vectorize(greater_than_zero), validate=False))
])

boolean_transformer = Pipeline(steps = [
  ('function_is_true', FunctionTransformer(np.vectorize(is_true), validate=False))
])

string_transformer = Pipeline(steps = [
  ('one_hot_encoder', OneHotEncoder(drop='if_binary'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ("float_transformer", float_transformer, FLOAT_COLS),
        ("integer_transformer", integer_transformer, INT_COLS),
        ("boolean_transformer", boolean_transformer, BOOL_COLS),
        ("string_transformer", string_transformer, STRING_COLS)
        ])

# Specify the function to get column names based on global variables & the preprocessor (
def get_all_col_names_in():
    return FLOAT_COLS + INT_COLS + BOOL_COLS + STRING_COLS

# can skip get_column_names_transformed function if the transformer is not nested and if the default method of getting column names is used)
def get_column_names_transformed(preprocessor):
    """ Customize this function to get the columns from preprocessor - depending on the attributes of the preprocessor this will look different. Pass this function to the MLExperiment """
    string_cols_transformed = list(preprocessor.named_transformers_['string_transformer'] \
                             .named_steps['one_hot_encoder'] \
                              .get_feature_names_out(STRING_COLS))
 
    col_names_transformed = FLOAT_COLS + INT_COLS + BOOL_COLS + string_cols_transformed
    
    return col_names_transformed


# build estimator
estimator = XGBClassifier(max_depth=3, learning_rate = 0.05, seed = 422)

# build ml datasets
full_df = get_data()
ml_data = MLData(df = full_df, target = TARGET, X_vars = get_all_col_names_in())
ml_data.split_random()
ml_data.describe()

#%% Run Experiment 1


# run ml experiment condition
ml_exp1 = MLExperiment(ml_data, preprocessor=preprocessor, estimator=estimator, transformer_col_function=get_column_names_transformed)

ml_exp1.fit_preprocessor()
ml_exp1.fit_estimator()
print(ml_exp1.auc_score_train)
print(ml_exp1.auc_score_test)

ml_exp1.feature_importances
ml_exp1.show_roc_train()


#%% Set Up And Run Experiment 2 - Grid Search of XGBoost
##### EXPERIMENT 2 : TRY GRID SEARCH XGBOOST #####
### Everything will be the same as Experiment 1 except things explicitly changed here
DESCRIPTION = 'Grid Search of XGBoost'

# build estimator
estimator = get_xgboost_gridsearch()

# build ml datasets
full_df = get_data()
ml_data = MLData(df = full_df, target = TARGET, X_vars = get_all_col_names_in())
ml_data.split_random()
ml_data.describe()


# run ml experiment condition
ml_exp1 = MLExperiment(ml_data, preprocessor=preprocessor, estimator=estimator, transformer_col_function=get_column_names_transformed)

ml_exp1.fit_preprocessor()
ml_exp1.fit_estimator()
print(ml_exp1.auc_score_train)
print(ml_exp1.auc_score_test)

ml_exp1.feature_importances
ml_exp1.show_roc_train()
