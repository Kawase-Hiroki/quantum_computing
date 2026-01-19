from interface import QuantumDevice
from simulator import SingleQubitSimulator

def qrng(device: QuantumDevice, n: int) -> bool:
    with device.using_qubit() as q:
        q.h()
        return q.measure()
    
if __name__ == "__main__":
    qsim = SingleQubitSimulator()
    for idx_sample in range(10):
        result = qrng(qsim, 1)
        print(f"Sample {idx_sample}: {result}")