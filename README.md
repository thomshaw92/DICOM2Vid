# Dicom2Vid
Just a tool to make DICOM folders into videos for participants etc.

This is a Python script that converts a series of DICOM images to a video file.

## Prerequisites

Ensure that you have the following installed:

- Python 3.8 or later
- pip

## Installation

1. Clone this repository: `git clone <repo_url>`
2. Navigate into the cloned repository: `cd <repo_name>`
3. Install the required Python packages: `pip install -r requirements.txt`

## Usage

The script can be run from the command line as follows:

```bash
python dicom_to_video.py --folder <path_to_dicom_folder> --output <output_filename> --orientation <orientation>
Arguments:

--folder: Path to the directory containing the DICOM files.
--output: The filename for the output video file.
--orientation: The orientation of the output video. Options are 'sagittal', 'coronal', 'axial', 'sagittal_flipped', 'coronal_flipped', 'axial_flipped'.
Example
To convert a DICOM series to a sagittal video:

python dicom_to_video.py --folder ./dicom_folder --output output.mp4 --orientation sagittal


###NB
Some of the orientations are flipped and what not. 
Try experimenting, I can't be bothered doing every one
