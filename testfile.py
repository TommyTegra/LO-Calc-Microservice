# ZeroMQ Functionality Test for income calculator

import zmq

# Create object
obj = zmq.Context()
socket = obj.socket(zmq.REQ)

# Connect to server
socket.connect("tcp://127.0.0.1:5000")

# Test program
while True:
    # Expected value is an integer
    income = input("Income value: ")
    # Expected is a string that is either EXACTLY 'yearly', 'monthly', or 'hourly'
    time_period = input("Pay period, all lowercase, no space: ")

    send_data = (income, time_period)
    socket.send_pyobj(send_data)

    result = socket.recv_pyobj()

    if isinstance(result, str):
        print("Error: " + result)
    else:
        print(f"Monthly income is: {result}")

    print('')
