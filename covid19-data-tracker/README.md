# 🦠 Real-Time COVID-19 Data Tracker

This project demonstrates how to collect real-time COVID-19 data using an open API (`disease.sh`) and visualize it using **Power BI**. It automates the data collection process with Python and enables interactive data exploration across countries.

---

## 📌 Features

- ✅ Real-time COVID-19 data collection using API
- ✅ Python script to automate daily data pulls
- ✅ CSV export of cleaned data
- ✅ Power BI dashboard with visual insights:
  - Total cases, deaths, recoveries, active cases
  - Daily new cases and deaths
  - Country-wise trends and global distribution

---

## 🛠 Tech Stack

| Tool          | Purpose                        |
|---------------|--------------------------------|
| Python        | Data extraction & automation   |
| Requests      | API calls                      |
| Pandas        | Data manipulation              |
| Power BI      | Data visualization             |
| disease.sh API| Real-time COVID data source    |

---

## 📂 Folder Structure

```
covid19-data-tracker/
├── covid19.py              # Python script to fetch and save data
├── covid_data.csv          # Output data file (auto-generated)
├── covid_dashboard.pbix    # Power BI dashboard
└── README.md               # Project documentation
```

---

## ▶️ How to Run This Project

1. **Install Python dependencies**:

```bash
pip install requests pandas
```

2. **Run the script** to get the latest COVID-19 data:

```bash
python covid19.py
```

This will save a CSV file (`covid_data.csv`) containing live data.

3. **Open the Power BI file** (`covid_dashboard.pbix`) and click **Refresh** to load the latest data.

---

## 📊 Dashboard Visuals

| Visualization Type | Fields Used                             | Purpose                            |
|--------------------|------------------------------------------|------------------------------------|
| Bar Chart          | Country (Axis), Total Cases (Values)     | Compare country-wise totals        |
| Map                | Country (Location), Cases (Size)         | Visualize geographic spread        |
| Stacked Column     | Country (Axis), Today Cases & Deaths     | Analyze daily trends               |
| Cards              | Cases, Deaths, Active, Recovered         | Display global KPIs                |
| Slicer             | Country                                  | Interactive filtering              |

---

## 🌐 API Reference

- **API URL**: [`https://disease.sh`](https://disease.sh)
- Endpoint used:  
  `https://disease.sh/v3/covid-19/countries`

---

## 🤝 Connect With Me

If you found this project helpful or have any questions, feel free to connect with me on [LinkedIn](https://www.linkedin.com/) or check out more of my work!

---

**#Python #PowerBI #DataAnalytics #Covid19 #RealTimeData #OpenToWork**
