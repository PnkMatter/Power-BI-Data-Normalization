# Power BI Data Normalization

This project performs data cleaning and normalization on a CSV file containing multi-level headers. The processed data is reshaped and formatted for seamless use in Power BI or other BI tools.

## Features

- Combines multi-index headers into single column names
- Removes unnecessary columns and renames headers
- Converts wide data to long format using `melt`
- Extracts `year`, `type`, and `metric` from column names
- Formats and prepares the final dataset for BI consumption

## Folder Structure


- Combines multi-index headers into single column names
- Removes unnecessary columns and renames headers
- Converts wide data to long format using `melt`
- Extracts `year`, `type`, and `metric` from column names
- Formats and prepares the final dataset for BI consumption

## Folder Structure

```
project-root/
├── data/
│ └── example.csv # (optional) Sample dataset
├── src/
│ └── data_cleaning.py # Main data processing script
├── README.md
└── requirements.txt
```


## How to Use

1. Clone the repository:
```bash
git clone https://github.com/your-username/powerbi-data-normalization.git
cd powerbi-data-normalization
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Adjust the path to your CSV file inside src/data_cleaning.py and run the script:

```
python src/data_cleaning.py
```

## Output Structure

```
country	plant	brand	line	year	type	metric	          value
BR	SP	XYZ	A	2023	ABC	Net-Sales	  10234.5
...	...	...	...	...	...	Intercompany %	  7.8
```

##Requirements

    Python 3.8+

    pandas

    re (standard library)

👨‍💻 Author

Developed by PnkMatter

Feel free to connect with me on LinkedIn or check out my projects on GitHub

📃 License

This project is licensed under the MIT License.
