# Nepal-Earthquake-Pipeline

> An end-to-end data pipeline that fetches Nepal earthquake data from the USGS API, cleans and transforms it, and loads it into a PostgreSQL database for analysis.

## API Used

USGS Earthquake API : 
https://earthquake.usgs.gov/fdsnws/event/1/

---

## Why This Project?

Nepal experienced devastating earthquakes in 2015 that caused significant loss of life and infrastructure damage. Analyzing earthquake patterns and seismic activity can help better understand earthquake trends and support future disaster preparedness efforts.

---

## Pipeline Overview

The pipeline consists of the following stages:

1. **ingest.py**
   Fetches earthquake data from the API and stores the raw data in a JSON file.

2. **clean.py**
   Selects relevant columns, cleans and transforms the data, and exports the processed data to a CSV file.

3. **load.py**
   Loads the cleaned CSV data into a PostgreSQL database.

4. **pipeline.py**
   Orchestrates the complete ETL pipeline by running all stages sequentially.

---

## Insights

The `queries/` folder contains SQL queries used to analyze the dataset.

### Key Findings

1. **Which years and months had the most earthquake activity?**
   April–May 2015 had the highest activity, with 260 recorded earthquakes due to the Gorkha earthquake and its aftershocks.

2. **Is there a relationship between depth and magnitude?**
   Very weak relationship, with a correlation of `-0.004`.

3. **What was the most destructive earthquake?**
   The April 25, 2015 earthquake with magnitude `7.8` near Gorkha.

4. **Are earthquakes becoming more frequent over time?**
   Earthquake frequency appears relatively stable, excluding the major spike in 2015.

5. **Which areas are affected most often?**
   Bagmati Province recorded the highest number of earthquakes.

6. **What is the typical earthquake depth and magnitude?**
   Average magnitude is approximately `4.5` with an average depth of around `13 km`.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/matinatula/Nepal-Earthquake-Pipeline
cd Nepal-Earthquake-Pipeline
```

Install dependencies using uv:

```bash
uv sync
```

---

## Environment Variables

Create a `.env` file and configure your PostgreSQL credentials:

```env
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_NAME=
```

Project dependencies are managed using `uv` and defined in `pyproject.toml`.

---

## Run the Project

```bash
python pipeline.py
```

## Tech Stack

* Python
* Pandas
* PostgreSQL
* SQLAlchemy

---


