import random


class Register:
    def __init__(self, students, types, events, scores):  # initialize registration data
        self.students = students
        self.types = types
        self.events = events
        self.scores = scores
        self.registered = {'individuals': [], 'teams': []}  # initialize ready data

    def register(self):
        """
        Iterates through self.types, selects the type, iterates over 20 and 4 numbers
        and constructs ready registered participants data (dictionary: list).
        Names are selected randomly from self.students list.
        :return: self.registered => dictionary of registered participants
        """
        for type in self.types:
            if type == 'Individual':  # if type == 'Individual' => count 20 members
                for n in range(1, 21):
                    self.registered['individuals'].append({n: {'name': random.choice(self.students), 'type': type,
                                                          'score': 0, 'events_num': 0, 'events_participated': []}})
            elif type == 'Team': # if type == 'Team' => count 4 teams
                for n in range(1, 5):
                    self.registered['teams'].append({n: {'name': f"Team {n}", 'type': type,
                                                         'score': 0, 'events_num': 0, 'events_participated': []}})
        return self.registered



