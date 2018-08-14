import os
import json
import time
from kaggle import api

# smaller than 100 MB
small = [
    "house-prices-advanced-regression-techniques",
    "titanic",
    "competitive-data-science-predict-future-sales",
    "forest-cover-type-kernels-only",
    "whats-cooking-kernels-only",
    "movie-review-sentiment-analysis-kernels-only",
    "demand-forecasting-kernels-only",
    "costa-rican-household-poverty-prediction",
    "youtube8m-2018",
    "inaturalist-2018",
    "imaterialist-challenge-fashion-2018",
    "imaterialist-challenge-furniture-2018",
    "landmark-recognition-challenge",
    "womens-machine-learning-competition-2018",
    "jigsaw-toxic-comment-classification-challenge",
    "nomad2018-predict-transparent-conductors",
    "recruit-restaurant-visitor-forecasting",
    "spooky-author-identification",
    "cdiscount-image-classification-challenge",
    "porto-seguro-safe-driver-prediction",
    "text-normalization-challenge-english-language",
    "nips-2017-non-targeted-adversarial-attack",
    "nips-2017-targeted-adversarial-attack",
    "nips-2017-defense-against-adversarial-attack",
    "nyc-taxi-trip-duration",
    "mercedes-benz-greener-manufacturing",
    "inaturalist-challenge-at-fgvc-2017",
    "sberbank-russian-housing-market",
    "youtube8m",
    "data-science-bowl-2017",
    "march-machine-learning-mania-2017",
    "transfer-learning-on-stack-exchange-tags",
    "leaf-classification",
    "santas-uncertain-bags",
    "facial-keypoints-detection",
    "allstate-claims-severity",
    "melbourne-university-seizure-prediction",
    "ghouls-goblins-and-ghosts-boo",
    "integer-sequence-learning",
    "predicting-red-hat-business-value",
    "shelter-animal-outcomes",
    "kobe-bryant-shot-selection",
    "sf-crime",
    "santander-customer-satisfaction",
    "home-depot-product-search-relevance",
    "bnp-paribas-cardif-claims-management",
    "march-machine-learning-mania-2016",
    "telstra-recruiting-network",
    "prudential-life-insurance-assessment",
    "the-allen-ai-science-challenge",
    "homesite-quote-conversion",
    "cervical-cancer-screening",
    "santas-stolen-sleigh",
    "walmart-recruiting-trip-type-classification",
    "whats-cooking",
    "rossmann-store-sales",
    "deloitte-western-australia-rental-prices",
    "denoising-dirty-documents",
    "coupon-purchase-prediction",
    "introducing-kaggle-scripts",
    "caterpillar-tube-pricing",
    "liberty-mutual-group-property-inspection-prediction",
    "icdm-2015-drawbridge-cross-device-connections",
    "crowdflower-search-relevance",
    "word2vec-nlp-tutorial",
    "predict-west-nile-virus",
    "random-acts-of-pizza",
    "poker-rule-induction",
    "bike-sharing-demand",
    "otto-group-product-classification-challenge",
    "forest-cover-type-prediction",
    "restaurant-revenue-prediction",
    "15-071x-the-analytics-edge-competition-spring-2015",
    "march-machine-learning-mania-2015",
    "15-071x-the-analytics-edge-spring-20152",
    "finding-elo",
    "axa-driver-telematics-analysis",
    "sentiment-analysis-on-movie-reviews",
    "data-science-london-scikit-learn",
    "afsis-soil-properties",
    "criteo-display-ad-challenge",
    "higgs-boson",
    "risky-business",
    "allstate-purchase-prediction-challenge",
    "the-analytics-edge-mit-15-071x",
    "random-number-grand-challenge",
    "pakdd-cup-2014",
    "genentech-flu-forecasting",
    "conway-s-reverse-game-of-life",
    "packing-santas-sleigh",
    "deloitte-churn-prediction",
    "see-click-predict-fix",
    "battlefin-s-big-data-combine-forecasting-challenge",
    "the-seeclickfix-311-challenge",
    "mastercard-data-cleansing-competition-finals",
    "amazon-employee-access-challenge",
    "challenges-in-representation-learning-facial-expression-recognition-challenge",
    "hack-reduce-dunnhumby-hackathon",
    "icdar2013-stroke-recovery-from-offline-data",
    "predict-who-is-more-influential-in-a-social-network",
    "hhp",
    "just-the-basics-the-after-party",
    "RxVolumePrediction",
    "visualize-the-state-of-education-in-colorado",
    "traveling-santa-problem",
    "customer-retention",
    "facebook-ii",
    "us-census-challenge",
    "GEF2012-wind-forecasting",
    "global-energy-forecasting-competition-2012-load-forecasting",
    "acm-sf-chapter-hackathon-small",
    "detecting-insults-in-social-commentary",
    "pf2012-diabetes",
    "msdchallenge",
    "online-sales",
    "twitter-psychopathy-prediction",
    "twitter-personality-prediction",
    "bioresponse",
    "awic2012",
    "emvic",
    "getting-started",
    "DontGetKicked",
    "GiveMeSomeCredit",
    "PhotoQualityPrediction",
    "dunnhumbychallenge",
    "overfitting",
    "ChessRatings2",
    "unimelb",
    "R",
    "socialNetwork",
    "tourism2",
    "chess",
    "informs2010",
    "tourism1",
    "hivprogression",
    "worldcup2010",
    "worldcupconf",
    "Eurovision2010"
]

print(len(small))

errors = []

for c in small:
    path = 'data/{}'.format(c)

    if os.path.isdir(path):
        print("Path {} already exists".format(path))
        continue

    print("Download files for", c)
    time.sleep(1)
    try:
        api.competition_download_files(c, path=path)
    except:
        errors.append(c)
        print("Error downloading files for", c)

print("Errors", errors)

s = json.dumps(errors)

text_file = open("./errors.json", "w")
text_file.write(s)
text_file.close()
