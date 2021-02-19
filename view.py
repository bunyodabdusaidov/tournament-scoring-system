
class View:
    def __init__(self, registered, results):  # initialize registered list and results list
        self.results = results
        self.registered = registered

    def view_registered(self):
        """
        Display the registered participants list in a user-friendly format.
        Iterates through the self.registered list, picks the relevant data (name, type),
        displays the result.
        """
        for mode, content in self.registered.items():
            if mode == 'individuals':
                for student in content:
                    for n, participant in student.items():
                        print(f"{n}) Name: {participant.get('name')}, Type: {participant.get('type')}")
            else:
                for student in content:
                    for n, participant in student.items():
                        print(f"{n}) Name: {participant.get('name')}, Type: {participant.get('type')}")

    def view_results(self):
        """
        Displays the results of the tournament in a user-friendly format after tournament finishes.
        Iterates through the self.results, picks all the data that was updated after the tournament finished,
        displays the results (name, type, events number, events participated, score)
        """
        for type, content in self.results.items():
            for participants in content:
                for num, participant in participants.items():
                    print(f"{num}) {participant['name']}, {participant['type']}, Events: {participant['events_num']}, "
                          f"Types: {participant['events_participated']}, Score: {participant['score']}")

    def view_winners(self):
        """
        Display the winners, 1st, 2nd, 3rd place.
        """

        final_scores = []
        for type, content in self.results.items():
            for participants in content:
                for num, participant in participants.items():
                    final_scores.append(participant['score'])  # accumulates only the scores and adds them to list.

        winners = {'1st': {}, '2nd': {}, '3rd': {}}
        scores = sorted(final_scores, reverse=True)  # sorts the accumulated score list in a descending order.
        for type, content in self.results.items():
            for participants in content:
                for num, participant in participants.items():  # compares the participants' scores
                    if participant['score'] == scores[0]:  # if participant's score is the first item in `score` list
                        winner = {'name': participant['name'], 'type': participant['type'], 'events': participant['events_participated'], 'score': participant['score']}
                        winners['1st'] = winner
                    elif participant['score'] == scores[1]:  # if participant's score is the second item in `score` list
                        winner = {'name': participant['name'], 'type': participant['type'], 'events': participant['events_participated'], 'score': participant['score']}
                        winners['2nd'] = winner
                    elif participant['score'] == scores[2]:  # if participant's score is the third item in `score` list
                        winner = {'name': participant['name'], 'type': participant['type'], 'events': participant['events_participated'], 'score': participant['score']}
                        winners['3rd'] = winner

        for place, winner in winners.items():  # iterates over `winners` dictionary, displays in a user-friendly format
            print(f"{place} - Name: {winner['name']}, Type: {winner['type']}, Events: {winner['events']}, Score: {winner['score']}")



