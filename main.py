import sys
from telemetry_monitor import TelemetryMonitor
from two_pointer_monitor import DataStreamOptimizer
from data_logger import SystemLogger

def run_dashboard():
    print("\n=============================================")
    print("   NASA TELEMETRY CENTRAL COMMAND INTERFACE  ")
    print("=============================================")
    
    raw_data = [2, 7, 11, 15]
    target_threshold = 9
    
    print(f"Current Data Stream: {raw_data}")
    print(f"Target Threshold: {target_threshold}\n")
    print("Select Engine Architecture:")
    print("1. Hash Map Core Engine    [O(n) Time / O(n) Space]")
    print("2. Two-Pointer Core Engine  [O(n) Time / O(1) Space]")
    print("3. Exit System")
    
    choice = input("\nEnter choice (1-3): ").strip()
    logger = SystemLogger()
    
    if choice == "1":
        print("[System Log: Initializing Hash Map Algorithm...]")
        monitor = TelemetryMonitor()
        results = monitor.find_critical_sensor_pair(raw_data, target_threshold)
        display_results(results, raw_data, target_threshold)
        if results:
            logger.log_alert("Hash Map O(n)", results, [raw_data[results[0]], raw_data[results[1]]], target_threshold)
        
    elif choice == "2":
        print("[System Log: Initializing Two-Pointer Algorithm...]")
        optimizer = DataStreamOptimizer()
        results = optimizer.find_target_pair_sorted(raw_data, target_threshold)
        display_results(results, raw_data, target_threshold)
        if results:
            logger.log_alert("Two-Pointer O(1) Space", results, [raw_data[results[0]], raw_data[results[1]]], target_threshold)
        
    elif choice == "3":
        print("\nShutting down Command Interface. Exiting.")
        sys.exit()
    else:
        print(f"\n❌ Choice '{choice}' is not a recognized configuration code.")

def display_results(results, data, target):
    if results:
        print("\n=========================================")
        print("⚠️  CRITICAL DANGER ALERT LEVEL REACHED  ⚠️")
        print(f"Target matched at index {results} ({data[results[0]]}) and index {results} ({data[results[1]]}) = {target}")
        print("=========================================")
    else:
        print("\n✅ Status Nominal: No anomalies detected in data stream.\n")

if __name__ == "__main__":
    run_dashboard()