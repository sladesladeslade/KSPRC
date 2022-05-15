import krpc

# fxn to connect to krpc server
conn = krpc.connect(
    name = "Test",
    address = "192.168.56.1",
    rpc_port = 5000,
    stream_port = 5001)

# print status of connection
print(conn.krpc.get_status().version)

# add vessel
vessel = conn.space_center.active_vessel
vessel.name = "TestVessel"

# get flight info and print
flight_info = vessel.flight()
print(flight_info.mean_altitude)

# add stream for data
altitude = conn.add_stream(getattr, flight_info, "mean_altitude")
while True:
    print(altitude())