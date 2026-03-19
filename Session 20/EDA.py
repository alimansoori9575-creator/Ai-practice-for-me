###  Basics of EDA (Exploratry data analysis)
# first we need to understand How typical workflow works(means agents banane ki steps kya hai)

'''
1. Data collection: This is the first step where you gather data from various sources. 
    This could be from databases, APIs, web scraping, or even manual entry.
2. EDA (Exploratory Data Analysis): In this step, you analyze the data to understand its structure, identify patterns, 
    and detect any anomalies. This involves visualizations, summary statistics, and correlation analysis.
3. Data Preprocessing: After understanding the data, you need to clean and preprocess it. 
    This includes handling missing values, encoding categorical variables, and scaling numerical features.
4. Model training: Once the data is ready, you can train your machine learning model using the preprocessed data. 
    This involves selecting an appropriate algorithm, tuning hyperparameters, and evaluating the model's performance.
5. Model evaluation: After training the model, you need to evaluate its performance using metrics such as accuracy, 
    precision, recall, and F1-score. This helps you understand how well your model is performing on unseen data.
6. Model deployment: If the model performs well, you can deploy it to a production environment where it can make predictions on new data. 
    This involves setting up an API or integrating the model into an application.'''

# Now we will focus on EDA part

# EDA is a crucial step in the data analysis process as it helps you understand the data, identify patterns, 
# and make informed decisions about how to preprocess the data for modeling. Here are some common techniques used in EDA:

# Some steps of EDA are:

# 1. understanding the data structure.
#     a. what does each column represent?
#     b. what are the data types of each column?
#     ex : Use df.shape, it gives you the number of rows and columns in the dataset. 
#     ex : Use df.columns, it gives you the names of all the columns in the dataset.

# 2. inspecting the data quality.
#     a. are there any missing values?
#     b. are there any duplicate records?
#     c. incorect data types?
#     d. unrealistic values?
#     ex : Use df.info(), it gives you a summary of the dataset including the number of non-null values in each column.
#    ex : Use df.isnull().sum(), it gives you the count of missing values in each column.
#    ex : Use df.duplicated().sum(), it gives you the count of duplicate records in the dataset.
##          We will Remove raws or fill missing valuse 

# 3. study distribution of data.
#     a. We will use Graphs like histograms, box plots, and density plots to visualize the distribution of numerical variables.
#       like we will watch where most values lies and where data skewed, where extreame value exists, etc.

# 4. identify outliers
#    a. We will use box plots and scatter plots to identify outliers in the data. 
#           Outliers can significantly affect the performance of machine learning models, 
#           so it's important to identify and handle them appropriately.

# 5. analyze relationships between variables.
#    corelation heatmap: means if we change one variable how other variable will change,
#    is there any relation between them or not, etc.
#     it has three types of corelation:
#     a. (+1)positive correlation: means if one variable increases then other variable also increases, and if one variable decreases then other variable also decreases.
#     b. (-1)negative correlation: means if one variable increases then other variable decreases, and if one variable decreases then other variable increases.
#     c. (0)no correlation: means there is no relationship between the two variables, and changes in one variable do not affect the other variable.
#            we will use df.corr() to calculate the correlation between numerical variables 
#            and imshow() to visualize the correlation matrix as a heatmap.
#  
# 6. visualize the data\ generate insights
#       Aster all this we will use various visualization techniques to generate insights from the data.