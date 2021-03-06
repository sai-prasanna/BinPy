from BinPy.Gates import *
""" Examples for OR class """
print "\n---Initializing the OR class--- "
print "gate = OR(0, 1)"
gate = OR(0, 1)
print "\n---Output of the OR gate----"
print "gate.output()"
print gate.output()
print "\n---Input changes---"
print "gate.setInput(1, 0) #Input at index 1 is changed to 0"
gate.setInput(1, 0)
print "\n---New Output of the OR gate---"
print gate.output()
print "\n---Changing the number of inputs---"
print "No need to set the number, just change the inputs"
print "gate.setInputs(1, 1, 1, 1)"
gate.setInputs(1, 1, 1, 1)
print "\n---To get the input states---"
print "gate.getInputStates()"
print gate.getInputStates()
print "\n---New output of the OR gate---"
print gate.output()
print "\n\n---Using Connectors as the input lines---"
print "Take a Connector"
print "conn = Connector()"
conn = Connector()
print "\n---Set Output of gate to Connector conn---"
print "gate.setOutput(conn)"
gate.setOutput(conn)
print "\n---Put this connector as the input to gate1---"
print "gate1 = OR(conn, 0)"
gate1 = OR(conn, 0)
print "\n---Output of the gate1---"
print "gate1.output()"
print gate1.output()
