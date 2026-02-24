from qiskit_metal import designs
from qiskit_metal.qlibrary.qubits.transmon_pocket import TransmonPocket
from qiskit_metal.qlibrary.tlines.meandered import RouteMeander
from qiskit_metal.qlibrary.tlines.straight_path import RouteStraight
from qiskit_metal.qlibrary.terminations.launchpad_wb import LaunchpadWirebond

# Design Initialization
design = designs.DesignPlanar()

design.chips.main.size['size_x'] = '15mm'
design.chips.main.size['size_y'] = '12mm'
design.chips.main.size['size_z'] = '500um'
design.chips.main.material = 'silicon'

# Global CPW parameters
TRACE_W = '10um'
TRACE_G = '6um'

# Qubit placement (linear chain)
x_positions = [-3000, -1000, 1000, 3000]

qubits = []

for i, x in enumerate(x_positions):
    q = TransmonPocket(
        design,
        f'Q{i+1}',
        options=dict(
            pos_x=f'{x}um',
            pos_y='0um',
            pad_width='200um',
            pad_height='90um',
            pocket_width='450um',
            pocket_height='650um',
            jj_length='0.2um'
        )
    )
    qubits.append(q)

# Nearest-neighbor coupling buses
for i in range(len(qubits)-1):
    RouteStraight(
        design,
        f'bus_Q{i+1}_Q{i+2}',
        options=dict(
            start_pin=dict(component=f'Q{i+1}', pin='drive'),
            end_pin=dict(component=f'Q{i+2}', pin='drive'),
            trace_width=TRACE_W,
            trace_gap=TRACE_G
        )
    )

# Readout resonators (frequency detuned)
readout_lengths = ['5600um', '5800um', '6000um', '6200um']

for i, length in enumerate(readout_lengths):
    RouteMeander(
        design,
        f'readout_Q{i+1}',
        options=dict(
            start_pin=dict(component=f'Q{i+1}', pin='readout'),
            total_length=length,
            trace_width=TRACE_W,
            trace_gap=TRACE_G,
            meander_spacing='20um',
            fillet='40um'
        )
    )

# Multiplexed feedline
LaunchpadWirebond(
    design,
    'Feedline_Left',
    options=dict(
        pos_x='-7000um',
        pos_y='4000um',
        orientation='0',
        trace_width=TRACE_W,
        trace_gap=TRACE_G
    )
)

LaunchpadWirebond(
    design,
    'Feedline_Right',
    options=dict(
        pos_x='7000um',
        pos_y='4000um',
        orientation='180',
        trace_width=TRACE_W,
        trace_gap=TRACE_G
    )
)

RouteStraight(
    design,
    'main_feedline',
    options=dict(
        start_pin=dict(component='Feedline_Left', pin='tie'),
        end_pin=dict(component='Feedline_Right', pin='tie'),
        trace_width=TRACE_W,
        trace_gap=TRACE_G
    )
)