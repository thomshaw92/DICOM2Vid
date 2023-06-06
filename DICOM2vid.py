## TBS 20230606
## take a dicom folder and make into an MP4 (AVI doesn't work b/c codec issues


import os
import argparse
import pydicom
import numpy as np
import cv2

def get_orientation_slice(view, array):
    """
    Given a view and a 3D array, this function returns the slices along the specified view.
    """
    if view == 'sagittal':
        return np.transpose(array, (2, 0, 1))
    elif view == 'coronal':
        return np.rollaxis(array, 0)
    elif view == 'axial':
        return array
    elif view == 'sagittal_flipped':
        return np.flip(np.rollaxis(array, 1))
    elif view == 'coronal_flipped':
        return np.flip(np.rollaxis(array, 0))
    elif view == 'axial_flipped':
        return np.flip(array)

def process_dicom_files(folder_path, output_file, orientation):
    # list containing valid DICOM extensions
    valid_exts = ['.dcm', '.ima']
    
    # list of all valid DICOM files in the directory
    dicom_files = [f for f in os.listdir(folder_path) if os.path.splitext(f)[-1].lower() in valid_exts]
    
    first_file = pydicom.dcmread(os.path.join(folder_path, dicom_files[0]))
    dimensions = (int(first_file.Rows), int(first_file.Columns), len(dicom_files))
    array_3d = np.zeros(dimensions, dtype=first_file.pixel_array.dtype)
    
    for i, file in enumerate(dicom_files):
        try:
            ds = pydicom.dcmread(os.path.join(folder_path, file))
            array_3d[:, :, i] = ds.pixel_array
        except Exception as e:
            print(f"Cannot read file {file}: {e}")
    
    array_3d = cv2.normalize(array_3d, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    orientation_view = get_orientation_slice(orientation, array_3d)
    
    codec = cv2.VideoWriter_fourcc('m','p','4','v') 
    frames_per_second = 20.0
    video = cv2.VideoWriter(output_file, codec, frames_per_second, (orientation_view.shape[2], orientation_view.shape[1]), isColor=False)
    
    for i in range(orientation_view.shape[0]):
        frame = orientation_view[i]
        video.write(frame)
    video.release()

def main():
    parser = argparse.ArgumentParser(description="Convert DICOM images to a video")
    parser.add_argument("--folder", required=True, help="Directory containing DICOM files")
    parser.add_argument("--output", required=True, help="Output video file name")
    parser.add_argument("--orientation", choices=['sagittal', 'coronal', 'axial', 'sagittal_flipped', 'coronal_flipped', 'axial_flipped'], default='sagittal', help="Orientation of the output video. Options are: sagittal, coronal, axial, sagittal_flipped, coronal_flipped, axial_flipped")

    args = parser.parse_args()

    process_dicom_files(args.folder, args.output, args.orientation)

if __name__ == "__main__":
    main()
