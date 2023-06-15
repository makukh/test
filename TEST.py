def everesting (segment_length, elevation, avg_speed_up, avg_speed_down, goal_elevation):
    count = 0
    count = goal_elevation / elevation
    total_length = 2 * count * segment_length / 1000
    total_time = (round(count, 1) * segment_length / 1000 / avg_speed_down + round(count, 1) *
                  segment_length / 1000 / avg_speed_up)
    print(f"Total length to gain elevation {goal_elevation} m is {round(total_length, 2)} km. You need to climb {round(count, 1)} times. You need {round(total_time, 1)} hours")

everesting(880, 52, 12, 45, 8848) # Kosmos
everesting(2150, 114, 12, 45, 8848) # Heroiv Krut