from qiskit_metal import designs
from qiskit_metal.qlibrary.qubits.transmon_pocket import TransmonPocket

def build_transmon(
    design,
    name,
    x,
    y,
    pad_w,
    pad_h,
    jj_len
):
    TransmonPocket(
        design,
        name,
        options=dict(
            pos_x=f'{x}um',
            pos_y=f'{y}um',
            pad_width=f'{pad_w}um',
            pad_height=f'{pad_h}um',
            pocket_width='450um',
            pocket_height='650um',
            jj_length=f'{jj_len}um'
        )
    )


design = designs.DesignPlanar()

build_transmon(
    design,
    name='Q1',
    x=0,
    y=0,
    pad_w=200,
    pad_h=90,
    jj_len=0.2
)
from qiskit_metal import designs
from qiskit_metal.qlibrary.qubits.transmon_pocket import TransmonPocket
from qiskit_metal.qlibrary.tlines.meandered import RouteMeander

design = designs.DesignPlanar()

# --- Qubit ---
TransmonPocket(
    design,
    'Q1',
    options=dict(
        pos_x='0um',
        pos_y='0um',
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
        total_length='6000um',      # sets resonance frequency
        trace_width='10um',
        trace_gap='6um',
        meander_spacing='20um',
        fillet='50um'
    )
)