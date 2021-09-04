'''move state check to state object '''
class Connection:#statemachine
    def __init__(self):
        self.new_state(ClosedConnectionState)
    def new_state(self, newstate):
        self._state = newstate
    # Delegate to the state class
    def read(self):
        return self._state.read(self)
    def write(self, data):
        return self._state.write(self, data)
    def open(self):
        return self._state.open(self)
    def close(self):
        return self._state.close(self)

# Connection state base
class ConnectionState:
    @staticmethod
    def read(conn):
        raise NotImplementedError()

    @staticmethod
    def write(conn, data):
        raise NotImplementedError()

    @staticmethod
    def open(conn):
        raise NotImplementedError()

    @staticmethod
    def close(conn):
        raise NotImplementedError()

# Implementation of different states
class ClosedConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        raise RuntimeError('Not open')
    @staticmethod
    def write(conn, data):
        raise RuntimeError('Not open')
    @staticmethod
    def open(conn):
        conn.new_state(OpenConnectionState)
    @staticmethod
    def close(conn):
        raise RuntimeError('Already closed')

class OpenConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        print('reading')
    @staticmethod
    def write(conn, data):
        print('writing')
    @staticmethod
    def open(conn):
        raise RuntimeError('Already open')
    @staticmethod
    def close(conn):
        conn.new_state(ClosedConnectionState)

c = Connection()
print( c._state )
try:
    c.read()
except Exception as ex:
    print( ex )

c.open()
print( c._state )
c.read()
c.write('Hello')
c.close()
print( c._state )
c.open()
print( c._state )