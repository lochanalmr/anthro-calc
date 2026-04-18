# AnthroCalc Program Guide
AnthroCalc is a command-line body composition metrics calculator program to _**calculate and classify**_ **body composition related metrics**. Simply run the executable file, and provide the necessary inputs. When using 'Metric' units, feel free to use either cm or m, but correctly mention whether cm or m was used, when prompted. For measurements that use 'Imperial' units, by default, it is considered that all lengths are in inches, and weight is in lbs. Inches and lbs are converted to metric units before calculation, if used.
No pre-requisites are required to run the executable. (Executable only available for Windows)

## Functions
### Implemented metrics
- BMI: Body Mass Index
- BAI: Body Adiposity Index
- WHR: Waist to Hip Ratio
- MM: MultiMeasure

### Metrics to be implemented
- WHTR: Waist to Height Ratio
- RFM: Relative Fat Mass

'MultiMeasure' feature is designed to collect all supported measurements, and calculate + classify body composition metrics supported in the program at once. Ability to export the MultiMeasure report as a text file is also available. The text file will be exported to the same folder as the program ran from, with a timestamp. A 'Help' function will be introduced to show information about the supported functions.

## Roadmap
- Implementation of WHTR, RFM functions
- Data storing function - in progress
- Data retrieval & analysis graph export
- Web interface
- Historical data analysis on web interface