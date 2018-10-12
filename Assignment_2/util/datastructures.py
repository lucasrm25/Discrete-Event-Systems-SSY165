from collections import namedtuple

Transition = namedtuple(typename='Transition', field_names=['source', 'event', 'target'])


class Automaton(object):

    def __init__(self, states, init, events, trans, marked=None, forbidden=None):
        """
        This is the constructor of the automaton.

        At creation, the automaton gets the following attributes assigned:
        :param states: A set of states
        :param init: The initial state
        :param events: A set of events
        :param trans: A set of transitions
        :param marked: (Optional) A set of marked states
        :param forbidden: (Optional) A set of forbidden states
        """
        self.states = self._validate_set(states)
        self.init = self._validate_init(init)
        self.events = self._validate_set(events)
        self.trans = self._validate_transitions(trans)
        self.marked = self._validate_subset(marked) if marked else set()
        self.forbidden = self._validate_subset(forbidden) if forbidden else set()

    def __str__(self):
        return 'states: \n\t{}\n' \
               'init: \n\t{}\n' \
               'events: \n\t{}\n' \
               'transitions: \n\t{}\n' \
               'marked: \n\t{}\n' \
               'forbidden: \n\t{}\n'.format(
            self.states, self.init, self.events,
            '\n\t'.join([str(t) for t in self.trans]), self.marked, self.forbidden)

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    @staticmethod
    def _validate_set(states):
        """
        Checks that states is a set and the states in it are strings or integers.
        """
        assert isinstance(states, set)
        for state in states:
            assert isinstance(state, str) or isinstance(state, int), 'A state must be either of type string or integer!'
        return states

    def _validate_subset(self, subset):
        """
        Validates the set and checks whether the states in the subset are part of the state set.
        """
        subset = self._validate_set(subset)
        assert subset.issubset(self.states), 'Marked and forbidden states must be subsets of all states!'
        return subset

    def _validate_init(self, state):
        """
        Checks whether the state is part of the state set.
        """
        assert isinstance(state, str) or isinstance(state, int), 'The initial state must be of type string or integer!'
        assert state in self.states, 'The initial state must be member of states!'
        return state

    def _validate_transitions(self, transitions):
        """
        Checks that all transition elements are part in the respective sets (states, events).
        """
        assert isinstance(transitions, set)
        for transition in transitions:
            assert isinstance(transition, Transition)
            assert transition.source in self.states
            assert transition.event in self.events
            assert transition.target in self.states
        return transitions
