import krpc
import time

conn = krpc.connect(name='Hello World')
vessel = conn.space_center.active_vessel

flight_info = vessel.flight(reference_frame = vessel.orbit.body.reference_frame)

ref1 = vessel.orbit.body.reference_frame
ref2 = vessel.surface_velocity_reference_frame
ref3 = vessel.surface_reference_frame

#altitude = conn.add_stream(getattr, flight_info, "mean_altitude")
#speed = conn.add_stream(getattr, flight_info, "speed")
#heading = conn.add_stream(getattr, flight_info, "heading")
#pitch = conn.add_stream(getattr, flight_info, "pitch")
#roll = conn.add_stream(getattr, flight_info, "roll")
#yaw = conn.add_stream(getattr, flight_info, "sideslip_angle")

print(vessel.name)

while True:
    time.sleep(.5)
    altitude = vessel.flight(ref1).mean_altitude
    speed = vessel.flight(ref1).speed
    heading = vessel.flight(ref1).heading
    pitch = vessel.flight(ref3).pitch
    roll = vessel.flight(ref2).roll
    yaw = vessel.flight(ref2).sideslip_angle
    print(altitude, "\t", speed, "\t", heading)
    print(pitch, "\t", roll, "\t", yaw)