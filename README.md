# MLDM-exam-project
American Express - Default Prediction


25.11 - Daniil Sulimov: set the idea of reducing memory complexity of the given data, stated approach to tackle data with 'dask' library. Tha advantage of 'dask' in compasion with 'pandas' is that 'dask' uses parallel computing, which allows to give boost in loading and preprocessing data. 
But the problem has arised: to work with data we need the functionality of 'pandas', which is wider "dask" ' s abilities. But when converting to usual pd.DataFrame we encounter with the disability of such thing. So, the experiment has been aknowledged as unsuccessful.

26.11 - Daniil Sulimov: in order to reduce the memory complexity of the data and be able to work with the pd.DataFrame, the following approach has been stated:

1) read data by chunks;

2) save to different files of smaller size;

3) preprocess them in order to reduce the overall complexity;

4) merge these files together to get one dataframe - **this step in not appropriate, we can iterate through all chunks and it will accelarate the process of preprocessong/learning model and so on**.

For preprocessing, first of all, we need to know types of columns. After the investigation, it was found that the majority of columns have the type of 'float64', which can be easily transformed to 'float32'. Also, we can preproccess given categorical variables.
After the preproccessing, we have decreased the memory usage in two times. When coming to merging chunks in one dataframe, computational power of the computer did not allow to do this.
Also, the following idea has popped into the mind: to check minimum and maximum date for the customers. It will allow to take futher decisions. For that the very first chunk was taken.

27.11 - Daniil Sulimov: in terms of the future model comes more precise interest in the given data. Let's start with the categorical features as the possible application of One-Hot Encoding in the future. For that the following things have been done:
1) for each column we got the frequency of values and also their counts. 
2) for each column of categorical feature a bar plot was built.
It was found that in the column D_66 NAN values take almost 90% of the data. This is the highest level among all categorical features. But if we use model based on the tree-algorithms, then it tackles with the NAN values itself. In general, the maximum amount of unique values among categorical features is 8, it means that One-Hot Encoding will suit the model.
Also as an idea of dropping some columns, which correlate with each other in a high level, I propose to work with the correlation matrix.

28.11 - Alina Mikhaylenko: Built a gradient boosting model on one of the data chunks. After analyzing the results, I'm going to try to train the model on several chunks at once and see how the quality of the model changes for its further development.

29.11 - Dmitriy Grinchenko: trying a new approach of data tackling. The fact is that given data is an unbalanced panel. Standard well-known machine learning algorithms involve working with tabular data. To this end, I proposed the approach of "collapsing" the panel into a cross-sectional data. This approach assumes a transition from time series for each customer to new features extracted from these time series. Thus, an essential task of modeling is feature generation and selection. 
Also, all data chunks were converted using the pickle library. It helps to save memory and decrease time of loading data.
Insights for future implementation: fill missing values according to a two-tier strategy. Firstly, fill na's inside each time series based on its structure (e.g. ffill: propagate last valid observation forward to next valid backfil). Secondly, if for some customer, for some for some feature, there was no whole time series (all - na's) - use the values of the generated feature averaged over the entire sample (see the approach to generating features).

last version of train_data is available at https://drive.google.com/drive/folders/1vmfkbtG4s8SLfsyLwO5vDTCfq65n4PPq?usp=share_link

29.11 - Daniil Sulimov: **Due to the computational power of my laplop, futher experiments will be conveyed on the several chunks**. All worth approaches wil be extrapolated to all dataframe. So, the first ideas popped into my mind: 
1. Conduct a research related to outliers;
2. Normalize data if outliers were found;
3. Tackle categorical features (e.g. One-Hot Encoding);
4. Fill NaN values. For example, for each client we can take a mean or median of the column;
5. Collapse time series;
Thinking about data featuring, it seems reasonable to group data by a customer and apply aggregating functions to the columns. Perhaps, these should be separate experiments - with centring data and not.

30.11 - Daniil Sulimov: After building a distribution of train labels, it was found out that we have more than 74% for target '0' and only 26% for '1'. It means, that we're dealing with imbalanced data and we should keep it in mind. For example, this is a case of using resampling. We can oversample minority class or undersaple the majority and get a balaced dataset eventually. 
Histograms of numerical features have shown that two columns - 'B_31' and 'D_87' are binary and should be excluded from the list of numerical features. Talking about outliers, a lot of columns show a certain kind of skewness. I think, to tackle them we should use scaling. But the whole picture is not that dramatic, as the majority of data is distributed before 0 and 1 or in smaller intervals and ,hence, deviation will not that huge. The computations have shown: Total deviation before scaling data is: 60.932323658918094. The next step was to develop features: the data was grouped by 'customer_ID' and several aggregation functions were applied. The total number of columns after that became 875 with 8294 rows (only first chunk was used). 
UPD: futher the preprocessing of data implied work with categorical features, since aggregate functions for numerical columns do not fit. And, finally, generated features were united together in one dataframe.

02.12 - Daniil Sulimov: After data engineering work, comes the process of learning the model. At first, RandomForestClassifier was picked. The only parameter,which was adjusted - 'class_weight', but keeping in mind that we have imbalanced classes - we need to optimize parameters. Missing values were solved in the most explicit way - they were filled with 0 values. Definitely, the dataset was divided into train and test parts with the ratio of 0.3. The results of the modelling in this way are presened in the file results_randomforest#1.jpg. The model could be enhanced by: 
1) cross-validation;
2) optimizing the parameters;
3) tackling missing values in more sophisticated way.
Again, the question of resampling arises.
