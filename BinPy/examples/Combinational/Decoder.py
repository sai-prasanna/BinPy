from BinPy.Combinational.combinational import *
""" Examples for Decoder class """
print "\n---Initializing the Decoder class--- "
print "mux = Decoder(0, 1)"
decoder = Decoder(0, 1)
print "\n---Output of decoder"
print "decoder.output()"
print decoder.output()
print "\n---Input changes---"
print "decoder.setInput(1, 0) #Input at index 1 is changed to 0"
decoder.setInput(1, 0)
print "\n---New Output of the decoder---"
print decoder.output()
print "\n---Changing the number of inputs---"
print "No need to set the number, just change the inputs"
print "Input must be power of 2"
print "decoder.setInputs(1, 0, 0)"
decoder.setInputs(1, 0, 0)
print "\n---To get the input states---"
print "decoder.getInputStates()"
print decoder.getInputStates()
print "\n---New output of decoder---"
print decoder.output()
print "\n\n---Using Connectors as the input lines---"
print "Take a Connector"
print "conn = Connector()"
conn = Connector()
print "\n---Set Output of decoder to Connector conn---"
print "decoder.setOutput(conn)"
decoder.setOutput(1, conn)
print "\n---Put this connector as the input to gate1---"
print "gate1 = AND(conn, 0)"
gate1 = AND(conn, 1)
print "\n---Output of the gate1---"
print "gate1.output()"
print gate1.output()
