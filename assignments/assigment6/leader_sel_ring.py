# Ring Algorithm for Leader Election

# Number of processes in the ring
num_processes = 5


# Process class representing each process in the ring
class Process:
    def __init__(self, process_id):
        self.process_id = process_id
        self.coordinator = False

    def start_election(self):
        # Process initiates the election process
        max_id = self.process_id
        print(f"Process {self.process_id}: Initiating election")

        # Passes an election message to the next process in the ring
        next_process = (self.process_id + 1) % num_processes
        while next_process != self.process_id:
            print(f"Process {self.process_id}: Sending election message to Process {next_process}")
            if next_process > max_id:
                max_id = next_process
            next_process = (next_process + 1) % num_processes

        # Election completed, the process with the highest ID becomes the coordinator/leader
        if max_id == self.process_id:
            self.coordinator = True
            print(f"Process {self.process_id}: Elected as coordinator")
        else:
            print(f"Process {self.process_id}: Process {max_id} elected as coordinator")


# Create processes
processes = [Process(i) for i in range(num_processes)]

# Start the election process by initiating the first process
processes[0].start_election()
