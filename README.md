# Radloader

A package of dataloaders for radiology reports

## Installation instructions

```
# Python3.7+ needed as coding using dataclasses
python3.7 -m venv .env
source .env/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install .
```

## Structure

A DatasetLoader returns a loader object with the following internal structure:
```
loader
└── documents
    ├── labels
	├── relations
	└── sentences
		├── entities
		├── modifiers
		├── negation
		└── words
```

## Run examples (after install)

### Example of loading the ESS dataset

The script below loads documents in that have been saved in ann.xml files.

See `examples/load_reports.py` for details
```
python examples/load_reports.py --folder /path/to/folder/containing/reports
```
