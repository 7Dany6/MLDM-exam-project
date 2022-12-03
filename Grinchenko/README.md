All data is available at https://drive.google.com/drive/folders/1vmfkbtG4s8SLfsyLwO5vDTCfq65n4PPq?usp=sharing

pipeline: preprocessing -> preparing_for_feature_generation -> feature_extracting -> RandomForest_(first_attempt)

All ipynbs contain comprehensive comments


Insights for future work:

1. Categorical feature encoding. Proposed approach - mean target encoding. Encoded on this way time serieses are more suitable for feature extraction and do not creates so much columns as OneHotEncoder

2. Handling missing values. Investigate ways to fill in missing values for entirely empty time serieses (for separate customers). Maybe consider encoding existing empty serieses as categorical features

3. Focus on gradient boost implementing
