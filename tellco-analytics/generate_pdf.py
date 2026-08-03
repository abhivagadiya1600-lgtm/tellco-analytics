import os
from weasyprint import HTML

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sales Forecasting - Technical Blog Report</title>
    <style>
        @page {
            size: A4;
            margin: 18mm 15mm;
            @bottom-right { content: "Page " counter(page) " of " counter(pages); font-size: 8pt; color: #64748b; }
            @bottom-left { content: "Rossmann Pharmaceuticals Sales Forecasting Report"; font-size: 8pt; color: #64748b; }
        }
        body { font-family: 'Helvetica Neue', Arial, sans-serif; color: #1e293b; line-height: 1.55; font-size: 10pt; }
        .header-banner { margin: -18mm -15mm 20px -15mm; padding: 25px 20mm; background: linear-gradient(135deg, #0f172a, #1e3a8a); color: #fff; }
        .header-banner h1 { font-size: 20pt; margin: 0 0 6px 0; }
        .subtitle { font-size: 11pt; color: #93c5fd; margin-bottom: 12px; }
        h2 { font-size: 13pt; color: #0f172a; border-left: 4px solid #2563eb; padding-left: 10px; margin-top: 20px; }
        table { width: 100%; border-collapse: collapse; margin: 12px 0; font-size: 8.5pt; }
        th { background-color: #1e293b; color: #fff; padding: 8px; text-align: left; }
        td { padding: 7px 8px; border-bottom: 1px solid #e2e8f0; }
        .code-block { background: #0f172a; color: #f1f5f9; padding: 10px; font-family: monospace; font-size: 8.5pt; border-radius: 4px; }
    </style>
</head>
<body>
    <div class="header-banner">
        <h1>Sales Forecasting Across Multiple Retail Stores</h1>
        <div class="subtitle">Technical Blog & Final Report — Rossmann Pharmaceuticals</div>
    </div>

    <h2>1. Executive Summary & Business Need</h2>
    <p>Rossmann Pharmaceuticals required an automated end-to-end sales forecasting model to predict daily turnover across 1,115 stores up to 6 weeks in advance.</p>

    <h2>2. Key Exploratory Data Analysis Insights</h2>
    <ul>
        <li><strong>Promotions:</strong> Active daily promos increased sales by +38.4% with high customer response spikes.</li>
        <li><strong>Holiday Dynamics:</strong> Strong pre-holiday stocking behavior followed by closure on state holidays.</li>
    </ul>

    <h2>3. Machine Learning & Preprocessing Pipeline</h2>
    <p>Engineered temporal date features (IsWeekend, Month, WeekOfYear) and trained a RandomForestRegressor pipeline.</p>
    <table>
        <tr><th>Model</th><th>MAE ($)</th><th>RMSE ($)</th></tr>
        <tr><td>Random Forest Pipeline</td><td>1376.34</td><td>1919.47</td></tr>
    </table>

    <h2>4. Deep Learning Approach (LSTM)</h2>
    <p>Transformed daily sales into stationary time-series data via first-order differencing and built a 2-layer stacked LSTM network.</p>
    <div class="code-block">
Layer 1: LSTM (64 units, Dropout 0.2)<br>
Layer 2: LSTM (32 units)<br>
Dense Output: Linear Sales Prediction
    </div>

    <h2>5. Project Deliverables</h2>
    <p><strong>GitHub Repo:</strong> https://github.com/abhivagadiya1600-lgtm/tellco-analytics</p>
</body>
</html>
"""

# Save HTML and generate PDF
with open("blog_report.html", "w", encoding="utf-8") as f:
    f.write(html_content)

HTML("blog_report.html").write_pdf("Rossmann_Final_Submission_Report.pdf")
print("PDF generated successfully: Rossmann_Final_Submission_Report.pdf")
