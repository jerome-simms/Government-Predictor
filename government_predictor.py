class GovernmentPredictor:
    key_definitions = [
        'Party mandate: After the midterm elections, the incumbent party holds more seats in the U.S. House of Representatives than after the previous midterm elections.',
        'No primary contest: There is no serious contest for the incumbent party nomination.',
        'Incumbent seeking re-election: The incumbent party candidate is the sitting president.',
        'No third party: There is no significant third party or independent campaign.',
        'Strong short-term economy: The economy is not in recession during the election campaign.',
        'Strong long-term economy: Real per capita economic growth during the term equals or exceeds mean growth during the previous two terms.',
        'Major policy change: The incumbent administration effects major changes in national policy.',
        'No social unrest: There is no sustained social unrest during the term.',
        'No scandal: The incumbent administration is untainted by major scandal.',
        'No foreign or military failure: The incumbent administration suffers no major failure in foreign or military affairs.',
        'Major foreign or military success:	The incumbent administration achieves a major success in foreign or military affairs.',
        'Charismatic incumbent: The incumbent party candidate is charismatic or a national hero.',
        'Uncharismatic challenger: The challenging party candidate is not charismatic or a national hero.'
    ]

    boolean_keys = [False for i in range(13)]

    def ask_questions(self):
        for i, val in enumerate(self.key_definitions):
            print(f'{i+1}) {val}')
            response = input('Do you agree? (y for agree, n for disagree): ')
            response = response.lower()
            while response not in ['y', 'n']:
                response = input('Please enter only "y" or "n": ')
                response = response.lower()
            self.boolean_keys[i] = True if response == 'y' else False

    def print_predicted_result(self):
        if self.make_prediction():
            print('\n\nThe incumbent government remains in power')
        else:
            print("\n\nThere will be a change of government")

    def make_prediction(self):
        """This function will return True if 6 or more of the keys are True"""
        count = 0
        for val in self.boolean_keys:
            count += 1 if val else 0
        return count >= 6
    
    def reset_keys(self):
        self.boolean_keys = [False for i in range(13)]