from interface import Qubit, QuantumDevice

def prepare_classical_message (bit: bool, q: Qubit) -> None:
    if bit:
        q.x()

def eve_measure (q: Qubit) -> bool:
    return q.measure()

def send_classicalbit(device: QuantumDevice, bit: bool) -> bool:
    with device.using_qubit() as q:
        prepare_classical_message(bit, q)
        result = eve_measure(q)
        q.reset()
    assert result == bit

def prepare_classical_message_plusminus (bit: bool, q: Qubit) -> None:
    if bit:
        q.x()
    q.h()

def eve_measure_plusminus (q: Qubit) -> bool:
    q.h()
    return q.measure()

def send_classical_bit_plusminus(device: QuantumDevice, bit: bool) -> bool:
    with device.using_qubit() as q:
        prepare_classical_message_plusminus(bit, q)
        result = eve_measure_plusminus(q)
        assert result == bit