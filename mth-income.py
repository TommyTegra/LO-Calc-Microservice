# Monthly income calculator microservice

import zmq

# Creates zmq object
obj = zmq.Context()
socket = obj.socket(zmq.REP)

# Establishes server
socket.bind("tcp://127.0.0.1:5000")

# Program functionality
while True:
    # Wait for an input/message and receives it
    data = socket.recv_pyobj()

    # Tuple unpacking
    income, time_period = data

    # Input validation
    err_msg = None
    income_int = None
    # Checks income
    try:
        income_int = int(income)
    except ValueError:
        err_msg = "Income is not an integer value."
    # Checks time period
    time_set = {"yearly", "monthly", "hourly"}
    if time_period not in time_set:
        if err_msg is None:
            err_msg = "Pay period is not valid."
        else:
            temp = err_msg + " Also, pay period is not valid."
            err_msg = temp
    # Sends a message to client if one or both input is invalid
    if err_msg is not None:
        socket.send_pyobj(err_msg)
        continue        # Restarts loop

    # Performs calculations
    if time_period == "yearly":
        mth_val = income_int / 12
    elif time_period == "hourly":
        mth_val = (income_int * 40 * 50) / 12
    else:
        mth_val = income_int

    # Sends results
    socket.send_pyobj(mth_val)







