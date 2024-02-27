# LO-Calc-Microservice
A microservice for Josh Pulattie's Loan Application and Qualifying Calculator. Built to take a tuple input of (income, pay_period) and return an integer value that represents a client's monthly income. Also, has input validation; a string describing the error will be returned if input is invalid.

## Communication Contract
[Communication Contract pdf](./Communication%20Contract.pdf)

## Required Library
ZeroMQ is required as stated in the requirements.txt.

## Requesting data
To request data from the microservice. Given that the microservice server is already up and running. One must then first connect to the server via ZeroMQ object creation.
```
# Create object
obj = zmq.Context()
socket = obj.socket(zmq.REQ)

# Connect to server
socket.connect("tcp://127.0.0.1:5000")
```
Then create a tuple as (income, pay_period) where income is an integer, and pay_period is a string of either "yearly", "monthly", or "hourly". 
```
request_data = (income, pay_period)
socket.send_pyobj(request_data)
```
This will send the tuple and begin requesting data from the microservice.

An example call of a valid tuple would be:
```
# Create object
obj = zmq.Context()
socket = obj.socket(zmq.REQ)

# Connect to server
socket.connect("tcp://127.0.0.1:5000")

# Request data
income = 75000
pay_period = "yearly"
request_data = (income, pay_period)
socket.send_pyobj(request_data)
```

## Receiving data
Once data has been requested from the microservice, one can then receive the processed data. 
```
result = socket.recv_pyobj()
```
The result is a variable that will hold either the monthly income value as a integer, or a string that describes the error message(s) based on the invalid input.

## UML Sequence Diagram
![UML Diagram](./UML.png)
