# Keys to the white house driver code

from predictor.government_predictor import GovernmentPredictor


opening_message = """
The Keys to the White House, also known as the 13 keys, is a prediction system for determining the outcome of presidential elections in the United States.
It was developed by American historian Allan Lichtman and Russian geophysicist Vladimir Keilis-Borok in 1981, 
adapting methods that Keilis-Borok designed for earthquake prediction. 
"""
   
        
if __name__ == "__main__":
    print(opening_message)
    input()

    predictor = GovernmentPredictor()
    predictor.ask_questions()
    predictor.print_predicted_result()
