#A job is delivering a service. Worked on by multiple machines
#An operation is one part of a job executed by one machines


class Operation:

    def __init__(self, machine, time, operationNr):
        self.machine = machine
        self.time = time
        self.operationNr = operationNr

    def __str__(self):
        string = 'Operation number: {}'.format(operation.operationNr) + ' \n'
        string += '\t Machine: {}'.format(operation.machine) + '\n'
        string += '\t Time   : {}'.format(operation.time) + '\n'
        return string
