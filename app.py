# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 13:23:54 2025

@author: Zeynep
"""

from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)


API_KEY = "a0d62e295724221e7536a8fb2c3059094c1854386e992e164b2dfd7348cddfe9fb92dd0c0c49ce96"

def check_ip(ip):
    """ IP adresini AbuseIPDB üzerinden kontrol eder """
    url = f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip}"
    headers = {
        "Key": API_KEY,
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()["data"]
        score = data.get("abuseConfidenceScore", 0)
        reports = data.get("totalReports", 0)

        if score > 50:
            return f"⚠️ Tehlikeli! Tehdit skoru: {score}, Rapor sayısı: {reports}"
        else:
            return f"✅ Güvenli görünüyor. Tehdit skoru: {score}, Rapor sayısı: {reports}"
    else:
        return "❌ API'ye bağlanırken hata oluştu!"


html_code = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IP Tehdit Kontrolü</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="container mt-5">
    <h2>IP Tehdit Analizi</h2>
    <form method="POST">
        <input type="text" name="ip" placeholder="IP adresini girin" class="form-control mb-2" required>
        <button type="submit" class="btn btn-primary">Kontrol Et</button>
    </form>

    {% if result %}
        <div class="mt-3">
            <p><strong>Sonuç:</strong> {{ result }}</p>
        </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        ip = request.form["ip"]
        result = check_ip(ip)
    return render_template_string(html_code, result=result)

if __name__ == "__main__":
    app.run(debug=True)
