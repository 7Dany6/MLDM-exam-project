All data and additional files are available at https://drive.google.com/drive/folders/1vmfkbtG4s8SLfsyLwO5vDTCfq65n4PPq?usp=sharing

**Attempt_1**

    pipeline: preprocessing -> preparing_for_feature_generation -> feature_extracting -> RandomForest_(first_attempt)

    all calculations were done with the whole train dataset on my local machine

    All ipynbs contain comprehensive comments


    Insights for future work:

    1. Categorical feature encoding. Proposed approach - mean target encoding. Encoded on this way time serieses are more suitable for feature extraction and do not create so much columns as OneHotEncoder

    2. Handling missing values. Investigate ways to fill in missing values for entirely empty time serieses (for separate customers). Maybe consider encoding existing empty serieses as categorical features

    3. Focus on gradient boost implementing

**Attempt_2**
    
    More accurate data preprocessing.
    Custom feature extraction
    Gradient Boosting implementing 
