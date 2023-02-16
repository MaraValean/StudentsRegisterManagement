from src.exceptions import UndoException


class UndoService:
    def __init__(self):
        # History of program operations
        self._history = []
        # Where are we in the operation history
        self._index = 0

    def undo(self):
        if self._index < 0:
            raise UndoException("There's nothing left to undo!")
        else:
            self._index -= 1
            self._history[self._index].undo()


    def redo(self):
        if self._index + 1 > len(self._history):
            raise UndoException("There's nothing left to redo!")
        else:
            self._history[self._index].redo()
            self._index += 1

    def record(self, operation):

        self._history.append(operation)
        self._index += 1

class Operation:
    def __init__(self, undo_call, redo_call):
        self._undo_call = undo_call
        self._redo_call = redo_call

    def undo(self):
        self._undo_call.call()

    def redo(self):
        self._redo_call.call()


class ComplexOperation:
    def __init__(self, operation):
        self._operations = operation

    def undo(self):
        for operation in self._operations:
            operation.undo()

    def redo(self):
        for operation in self._operations:
            operation.redo()


class Call:
    def __init__(self, function_name, *function_params):
        self._function_name = function_name
        self._function_params = function_params

    def call(self):
        self._function_name(*self._function_params)
