import os
import numpy as np
import random
import pyvista as pv

# Reset random seeds
def reset_random_seeds(seed_value):
    
    """
    Reset random seeds for reproducibility.

    This function sets the seed value for random number generation to ensure
    reproducibility of results. It affects the Python built-in `random` module,
    NumPy's random number generator, and the hash seed for Python objects.

    Parameters:
    seed_value (int): The seed value to set for random number generators.
    """

    os.environ['PYTHONHASHSEED'] = str(seed_value)
    random.seed(seed_value)
    np.random.seed(seed_value)



def visual_3d(input_model: np.ndarray | np.ma.MaskedArray,
              spacing: tuple[float] = (1,1,1), # micro-meter in x-,y-,z-directions
              origin: tuple[float] = (0,0,0),
              cmap:str = 'viridis',
              show_edges:bool = False,
              save_html: str = None):
    # Generate random data for demonstration; replace with actual voxel data
    # Data could represent intensities or any scalar field you have.
    
    data = input_model[::-1,:,::-1].T # this is due to sequence of data array

    # Define the spacing and origin (optional)
    spacing = spacing  # Define spacing between voxels
    origin = origin   # Define origin if needed

    # Create the uniform grid
    grid = pv.ImageData()

    # Set the grid dimensions
    nx, ny, nz = data.shape
    grid.dimensions = np.array([nx, ny, nz])

    # Set the grid spacing and origin
    grid.spacing = spacing
    grid.origin = origin

    # Add the data to the grid as 'values'
    grid.point_data["values"] = data.flatten(order="F")  # Flatten to 1D in Fortran order

    # Start the plotter
    plotter = pv.Plotter()
    plotter.add_mesh(grid, 
                    show_edges = show_edges, 
                    cmap=cmap)# , opacity="sigmoid")
    # Save to HTML if specified
    if save_html:
        plotter.export_html(save_html)
        print(f"Visualization saved as {save_html}")
    # Add some lighting and interactivity options
    plotter.show()