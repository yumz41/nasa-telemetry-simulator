import datetime

class SystemLogger:
    def log_alert(self, algorithm_name: str, indices: list[int], values: list[int], target: int):
        # The 'a' parameter means "Append" - it adds to the file without deleting old data
        with open("telemetry_history.log", "a", encoding="utf-8") as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Format a professional system log entry
            log_entry = (
                f"[{timestamp}] ALERT - ENGINE: {algorithm_name} | "
                f"Matched Indices: {indices} | Values: {values} | Total: {target}\n"
            )
            
            # Write it permanently to your hard drive
            file.write(log_entry)
            print("[System Log: Permanent disk backup entry recorded successfully.]")
            