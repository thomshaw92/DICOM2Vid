# Dicom2Vid
Just a tool to make DICOM folders into videos for participants etc.
Output is MP4 as AVI Codec is wacky

## Prerequisites

Ensure that you have the following installed:

- Python 3.8 or later
- pip

## Installation

1. Clone this repository: `git clone https://github.com/thomshaw92/DICOM2Vid.git`
2. Navigate into the cloned repository: `cd DICOM2Vid`
3. Install the required Python packages: `pip install -r requirements.txt`

## Usage

The script can be run from the command line as follows:

```
python dicom_to_video.py --folder <path_to_dicom_folder> --output <output_filename> --orientation <orientation>
```

Arguments:

--folder: Path to the directory containing the DICOM files.

--output: The filename for the output video file.

--orientation: The orientation of the output video. Options are 'sagittal', 'coronal', 'axial', 'sagittal_flipped', 'coronal_flipped', 'axial_flipped'.

Example
To convert a DICOM series to a sagittal video:
```
python dicom_to_video.py --folder ./dicom_folder --output output.mp4 --orientation sagittal
```

###NB
Some of the orientations are flipped and what not. 
Try experimenting, I can't be bothered doing every one
