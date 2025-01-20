import pickle

# race_weights = {
#   'N_popbenrace': 0.10,  # Native Americans
#   'W_popbenrace': 0.67,  # White
#   'B_popbenrace': 0.08,  # Black
#   'H_popbenrace': 0.12,  # Hispanic
#   'P_popbenrace': 0.003, # Pacific Islanders
#   'A_popbenrace': 0.027, # Asians
#   'G_popbenrace': 0.5,   # High race diversity
#   '-1_popbenrace': 0,
# }


# age_weights = {
#   '1_popbenage': 0.267,  # Age group 1
#   '2_popbenage': 0.07,   # Age group 2
#   '3_popbenage': 0.502,  # Age group 3
#   '4_popbenage': 0.161,  # Age group 4
#   '9_popbenage': 1,      # High age diversity
#   '-1_popbenage': 0,
# }

def load_data():
    
    with open('data/event_county_matrix.pickle', 'rb') as f:
        event_county_matrix = pickle.load(f)

    return event_county_matrix

def write_race():
    
    with open("race_weights.pickle", "wb") as pickle_file:
    
        pickle.dump(race_weights, pickle_file)

def write_age():

    with open("age_weights.pickle", "wb") as pickle_file:

        pickle.dump(age_weights, pickle_file)

if __name__ == "__main__":
    write_race()
    write_age()