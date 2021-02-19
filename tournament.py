import random


class Start:
    def __init__(self, registered, events, scores):  # initialize registered participants, event types, scores
        self.registered = registered
        self.events = events
        self.scores = scores

    def start(self):
        """
        Starts the tournament. Iterated through the registered participants dictionary, selects each participant,
        updates score, events number, events participated.
        Event types are selected randomly from self.events and appended to 'events_participated' list.
        Scores are selected randomly from self.scores and multiplied to randomly selected number from 50-100.
        This process is repeated until the 'events_num' reaches 5. In each iteration, 'events_num' is accumulated by 1.
        :return: self.registered => updated dictionary of participants with results
        (events number, events participated, score)
        """
        for mode, content in self.registered.items():
            for participants in content:
                for number, participant in participants.items():
                    while participant['events_num'] != 5:
                        current_event = random.choice(self.events)
                        participant['score'] = round(random.choice(self.scores) * random.randint(50, 100))
                        participant['events_participated'].append(current_event)
                        participant['events_num'] += 1
        return self.registered










