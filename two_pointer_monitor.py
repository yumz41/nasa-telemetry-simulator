class DataStreamOptimizer:
    def find_target_pair_sorted(self, data: list[int], target: int) -> list[int]:
        # Place pointers at the absolute boundaries
        left = 0
        right = len(data) - 1
        
        # Keep searching until the pointers meet in the middle
        while left < right:
            current_sum = data[left] + data[right]
            
            # Scenario A: We hit the exact target match
            if current_sum == target:
                return [left, right]
            
            # Scenario B: Sum is too large, move the right pointer to a smaller value
            elif current_sum > target:
                right -= 1
                
            # Scenario C: Sum is too small, move the left pointer to a larger value
            else:
                left += 1
                
        return [] # No matching boundaries found

# Verification Simulation Block
if __name__ == "__main__":
    optimizer = DataStreamOptimizer()
    
    # A pre-sorted stream (e.g., chronological timestamps or sequential transactions)
    sorted_telemetry = [1020, 2300, 3110, 4500, 5900, 8000]
    critical_limit = 7610 
    
    indices = optimizer.find_target_pair_sorted(sorted_telemetry, critical_limit)
    
    print("--- SYSTEM OPTIMIZATION MONITOR ---")
    if indices:
        print(f"✅ Match found at Index {indices[0]} ({sorted_telemetry[indices[0]]}) "
              f"and Index {indices[1]} ({sorted_telemetry[indices[1]]}) = {critical_limit}")
    else:
        print("❌ Stream within safe operating boundaries.")