import random

class TelemetryMonitor:
    # Notice the 4 spaces of indentation before "def"
    def find_critical_sensor_pair(self, sensor_readings: list[int], danger_threshold: int) -> list[int]:
        # Notice the 8 spaces of indentation inside the function
        reading_to_index = {}
        
        for index, reading in enumerate(sensor_readings):
            complement = danger_threshold - reading
            
            if complement in reading_to_index:
                return [reading_to_index[complement], index]
            
            reading_to_index[reading] = index
            
        return []

# This block stays all the way to the left because it is the main program script
if __name__ == "__main__":
    monitor = TelemetryMonitor()
    
    # Simulating a stream of data
    mars_rover_stream = [3400, 4500, 3110, 5200, 2900]
    critical_target = 7610  
    
    print("--- NASA MARS ROVER TELEMETRY MONITOR ---")
    
    alert_indices = monitor.find_critical_sensor_pair(mars_rover_stream, critical_target)
    
    if alert_indices:
        idx1, idx2 = alert_indices
        print(f"⚠️ CRITICAL ALERT: Combined structural load threshold reached!")
        print(f"Sensor Index {idx1} ({mars_rover_stream[idx1]}) + Sensor Index {idx2} ({mars_rover_stream[idx2]}) = {critical_target}")
    else:
        print("✅ Telemetry nominal. No critical pairs detected.")