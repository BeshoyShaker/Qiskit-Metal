from qiskit_metal import designs
from qiskit_metal.qlibrary.qubits.transmon_pocket import TransmonPocket

design = designs.DesignPlanar()

design.chips.main.size['size_x'] = '15mm'
design.chips.main.size['size_y'] = '6mm'
design.chips.main.size['size_z'] = '500um'
design.chips.main.material = 'silicon'

JJ_LENGTHS = [0.18, 0.20, 0.22, 0.24]  
x = -3000

for i, jj in enumerate(JJ_LENGTHS):
    TransmonPocket(
        design,
        f'Q{i}',
        options=dict(
            pos_x=f'{x}um',
            pos_y='0um',
            pad_width='200um',
            pad_height='90um',
            pocket_width='450um',
            pocket_height='650um',
            jj_length=f'{jj}um'
        )
    )
    x += 2000