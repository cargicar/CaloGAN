import uproot
import h5py
import numpy as np
import os

def root_to_hdf5(input_root_file, output_hdf5_file, tree_name=None):
    """
    Converts a ROOT TTree to an HDF5 file.

    Args:
        input_root_file (str): Path to the input .root file.
        output_hdf5_file (str): Path to the output .hdf5 file.
        tree_name (str): Name of the TTree to convert.
    """
    try:
        with uproot.open(input_root_file) as root_file:
            if tree_name not in root_file:
                print(f"Error: TTree '{tree_name}' not found in '{input_root_file}'")
                return

            tree = root_file[tree_name]
            branches = tree.keys()
            data = tree.arrays(branches)

            with h5py.File(output_hdf5_file, 'w') as hdf5_file:
                for branch in branches:
                    # Convert ROOT's awkward arrays to NumPy arrays for h5py
                    if isinstance(data[branch], np.ndarray):
                        hdf5_file.create_dataset(branch, data=data[branch])
                    else:
                        # Handle cases where the branch might be a list of arrays
                        numpy_data = np.array(data[branch].tolist())
                        hdf5_file.create_dataset(branch, data=numpy_data)

        print(f"Successfully converted '{input_root_file}:{tree_name}' to '{output_hdf5_file}'")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = "plz_work_kthxbai_t0.root"  # Replace with the path to your .root file
    output_file = "t0.hdf5" # Replace with the desired name for your .hdf5 file
    tree_to_convert = "fancy_tree"  # Replace with the name of the TTree you want to convert

    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input ROOT file '{input_file}' not found.")
    else:
        root_to_hdf5(input_file, output_file, tree_to_convert)