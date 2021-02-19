from data import students, types, events, scores
from register import Register
from tournament import Start
from view import View

register = Register(students, types, events, scores)  # initialize the Register instance (register object)
registered = register.register  # registration process function

start = Start(registered(), register.events, register.scores)  # initialize the Start instance (start object)
started = start.start  # tournament start function

view = View(registered(), started())  # initialize View instance (view object)

INPUT = """
Options:
- 'r' to start registration process
- 'v' to view registered students
- 's' to start the tournament
- 't' to view the results
- 'f' to view the winners
- 'q' to quit the app
Enter a letter: """

# easier way of working with inputs
inputs = {
    'r': registered,
    'v': view.view_registered,
    's': started,
    't': view.view_results,
    'f': view.view_winners
}


def menu():
    user_input = input(INPUT)

    while user_input != 'q':  # loop repeats until the input equals to 'q' (user wants to quit the app)
        if user_input in inputs:  # gets input, verifies its existence in `inputs` list
            selected_input = inputs[user_input]  # if True => selects the corresponding function according to input
            selected_input()  # calls the function by just adding brackets ()
        else:
            print('Unknown command! Please try again.')

        user_input = input(INPUT)


menu()


