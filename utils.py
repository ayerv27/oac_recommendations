import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import NMF
 
  
def process_data(df):
   
    return df
 
def simpsons_diversity(data,race_counts):
   
    n_races = len(race_counts)
    race_counts = data.filter(like='_popbenrace').apply(pd.to_numeric, errors='coerce').fillna(0).sum()
   
    p_squared = sum((count / sum(race_counts))**2 for count in race_counts if count > 0)
    return 1 - p_squared
 
def custom_diversity_function(data, race_weights, age_weights):
   
    race_diversity = 0
    benefit_diversity = 0
 
    race_data = data.filter(like='_popbenrace').apply(pd.to_numeric, errors='coerce').fillna(0)
    if not race_data.empty and -1 not in race_data.values:
        weighted_race_data = race_data.multiply(race_weights, axis='columns')
        race_counts = weighted_race_data.sum(axis=0)  
        race_diversity = simpsons_diversity(data, race_counts)
 
    age_data = data.filter(like='_popbenage').apply(pd.to_numeric, errors='coerce').fillna(0)
    if not age_data.empty and -1 not in age_data.values:
        weighted_age_data = age_data.multiply(age_weights, axis='columns')
        age_counts = weighted_age_data.sum(axis=0)
        benefit_diversity = sum(age_counts)  
 
    return race_diversity + benefit_diversity
 
 
 
def recommend_events_for_county(county, event_county_matrix, num_recommendations=5):
 
    act_dictionary = {12: 'Arts Instruction',
                             6: 'Exhibition',
                             11: 'Operating Support',
                             5: 'Performance/Reading',
                             20: 'School Residency',
                             13: 'Marketing',
                             8: 'Fair/Festival',
                             29: 'Professional Dev/Training',
                             15: 'Artistic Support',
                             22: 'Seminar/Conference',
                             31: 'Curriculum Dev/Implement',
                             4: 'Artwork Creation',
                             14: 'Administrative Support',
                             25: 'Apprenticeship',
                             33: 'Building Public Awareness',
                             19: 'Research/Planning',
                             16: 'Recording/Filming',
                             21: 'Other Residency',
                             2: 'Audience Services',
                             99: 'None of the Above',
                             -1: 'N/A Not Reported',
                             9: 'Documentation',
                             17: 'Publication',
                             36: 'Broadcasting',
                             26: 'Regranting',
                             34: 'Technical Assistance',
                             18: 'Restoration',
                             1: 'Acquisition'}

    if county in event_county_matrix.index:
        county_preferences = event_county_matrix.loc[county].values.reshape(1, -1)
        county_similarity = cosine_similarity(event_county_matrix, county_preferences)
        county_similarity = county_similarity.flatten()
        similar_counties_indices = county_similarity.argsort()[::-1][1:]  # Exclude the target county itself
        recommendations = []
        for idx in similar_counties_indices:
            similar_county_events = event_county_matrix.iloc[idx].sort_values(ascending=False)
            recommendations.extend(similar_county_events.index.tolist())
            if len(recommendations) >= num_recommendations:
                break
        recommendations = recommendations[:num_recommendations]
        recommended_events = [act_dictionary[acttype] for acttype in recommendations]
    else:
        # Cold start problem: recommend popular events based on average diversity scores
        popular_events = event_county_matrix.mean().sort_values(ascending=False)
        recommendations = popular_events.head(num_recommendations).index.tolist()
        recommended_events = [act_dictionary[acttype] for acttype in recommendations]
        
    return recommended_events