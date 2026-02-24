from qiskit_metal import designs
from qiskit_metal.qlibrary.qubits.transmon_pocket import TransmonPocket
from qiskit_metal.qlibrary.tlines.meandered import RouteMeander
from qiskit_metal.qlibrary.terminations.launchpad_wb import LaunchpadWirebond
from qiskit_metal.qlibrary.tlines.straight_path import RouteStraight

# Create design
design = designs.DesignPlanar()

# Chip definition
design.chips.main.size['size_x'] = '10mm'
design.chips.main.size['size_y'] = '10mm'
design.chips.main.size['size_z'] = '500um'
design.chips.main.material = 'silicon'

# Transmon qubit
TransmonPocket(
    design,
    'Q1',
    options=dict(
        pos_x='0um',
        pos_y='0um',
        orientation='90',
        pad_width='200um',
        pad_height='90um',
        pocket_width='450um',
        pocket_height='650um',
        jj_length='0.2um'
    )
)

# Readout resonator
RouteMeander(
    design,
    'readout_Q1',
    options=dict(
        start_pin=dict(component='Q1', pin='readout'),
        total_length='6000um',
        trace_width='10um',
        trace_gap='6um',
        meander_spacing='20um',
        fillet='50um'
    )
)

# Launchpad
LaunchpadWirebond(
    design,
    'LP1',
    options=dict(
        pos_x='-4500um',
        pos_y='3000um',
        orientation='0',
        pad_width='300um',
        pad_height='300um',
        trace_width='10um',
        trace_gap='6um'
    )
)

# Feedline connection
RouteStraight(
    design,
    'feedline',
    options=dict(
        start_pin=dict(component='LP1', pin='tie'),
        end_pin=dict(component='readout_Q1', pin='end'),
        trace_width='10um',
        trace_gap='6um'
    )
)