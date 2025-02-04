import matplotlib.pyplot as plt

#from . import cerebro_brain_utils as cbu
#from . import cerebro_brain_viewer as cbv

from cerebro import cerebro_brain_utils as cbu
from cerebro import cerebro_brain_viewer as cbv

my_brain_viewer = cbv.Cerebro_brain_viewer()

surface = 'pial'
surface_model = my_brain_viewer.load_template_GIFTI_cortical_surface_models(surface)

cifti_space = my_brain_viewer.visualize_cifti_space(volumetric_structures='subcortex', volume_rendering='spheres_peeled')
"""

stat = 'curvature'
dscalar_file = cbu.get_data_file(f'templates/HCP/dscalars/S1200.{stat}_MSMAll.32k_fs_LR.dscalar.nii')
dscalar_layer = my_brain_viewer.add_cifti_dscalar_layer(dscalar_file=dscalar_file, colormap=plt.cm.Greys_r, opacity=1)


dscalar_file = cbu.get_data_file(f'templates/HCP/dscalars/hcp.gradients.dscalar.nii')
dscalar_layer = my_brain_viewer.add_cifti_dscalar_layer(dscalar_file=dscalar_file, colormap=plt.cm.Spectral, opacity=0.6)

my_brain_viewer.change_view('L')
"""
my_brain_viewer.show()
