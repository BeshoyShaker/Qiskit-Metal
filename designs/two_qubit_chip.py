from qiskit_metal import designs
from qiskit_metal.qlibrary.qubits.transmon_pocket import TransmonPocket
from qiskit_metal.qlibrary.tlines.straight_path import RouteStraight
from qiskit_metal.qlibrary.tlines.meandered import RouteMeander

design = designs.DesignPlanar()

# Chip
design.chips.main.size['size_x'] = '12mm'
design.chips.main.size['size_y'] = '12mm'
design.chips.main.size['size_z'] = '500um'
design.chips.main.material = 'silicon'

# Qubits
TransmonPocket(
    design,
    'Q1',
    options=dict(
        pos_x='-500um',
        pos_y='0um',
        pad_width='200um',
        pad_height='90um',
        pocket_width='450um',
        pocket_height='650um',
        jj_length='0.2um'
    )
)

TransmonPocket(
    design,
    'Q2',
    options=dict(
        pos_x='500um',
        pos_y='0um',
        pad_width='200um',
        pad_height='90um',
        pocket_width='450um',
        pocket_height='650um',
        jj_length='0.21um'
    )
)

# Bus resonator
RouteStraight(
    design,
    'bus',
    options=dict(
        start_pin=dict(component='Q1', pin='drive'),
        end_pin=dict(component='Q2', pin='drive'),
        trace_width='10um',
        trace_gap='6um'
    )
)

# Readout resonators
RouteMeander(
    design,
    'readout_Q1',
    options=dict(
        start_pin=dict(component='Q1', pin='readout'),
        total_length='5800um',
        trace_width='10um',
        trace_gap='6um',
        meander_spacing='20um'
    )
)

RouteMeander(
    design,
    'readout_Q2',
    options=dict(
        start_pin=dict(component='Q2', pin='readout'),
        total_length='6200um',
        trace_width='10um',
        trace_gap='6um',
        meander_spacing='20um'
    )
)
