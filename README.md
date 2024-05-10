# python-sandbox

## ML Experiment Module
The ml_experiment module provides two objects for streamlining machine learning development experiment workflows.

The MLData class takes a Pandas dataframe with target and X fields specified and splits it into Train, Validation, and Test sets. This allows the Data Scientist to have one object containing all the data sets.

The MLExperiment class takes a MLData, a sklearn preprocessor and an estimator and has methods to run ML training and validation steps. This allows a Data Scientist to run iterations of ML Experiments where they change components of the processor or model and test the performance with minimal additional code.


## Other Modules

 - Data Structures: Data Strucutre Objects used in algorithms
 - Databricks Utilites: Functions for working on Databricks and saving/getting data from the database
 - Feature Encoding: Functions used for cleaning/encoding features used within the ML Experiment Module
 - Pandas Utilites: Functions used for operating on Pandas Dataframes/Series 
