import pandas as pd
import numpy as np

# ------------------------------
# FRAUD LEAK AI - CORE ENGINE
# ------------------------------

class FraudLeakAI:
    def __init__(self, threshold=0.7):
        self.threshold = threshold  # Risk score threshold

    def detect_fraud(self, df):
        results = []

        for index, row in df.iterrows():
            risk_score = self.calculate_risk(row)

            results.append({
                "Transaction_ID": row.get("Transaction_ID", index),
                "Amount": row["Amount"],
                "Vendor": row["Vendor"],
                "Department": row["Department"],
                "Risk_Score": round(risk_score, 2),
                "Flagged": "YES" if risk_score >= self.threshold else "NO"
            })

        return pd.DataFrame(results)

    def calculate_fraud_rules(self, row):
        score = 0

        if row["Amount"] > 100000:
            score += 0.4

        if row["Amount"] < 100:
            score += 0.1

        risky_vendors = ["XYZ Pvt Ltd", "FakeVendor Inc", "ShadyCorp"]
        if row["Vendor"] in risky_vendors:
            score += 0.3

        risky_departments = ["Procurement", "Logistics", "Purchasing"]
        if row["Department"] in risky_departments:
            score += 0.2

        return score

    def detect_anomalies(self, df, row):
        score = 0

        amount_mean = df["Amount"].mean()
        amount_std = df["Amount"].std()

        if row["Amount"] > amount_mean + 2 * amount_std:
            score += 0.4

        if row["Amount"] < amount_mean - 2 * amount_std:
            score += 0.2

        return score

    def calculate_risk(self, row):
        rule_score = self.calculate_fraud_rules(row)
        return rule_score


# ------------------------------
# RUNNING THE AI
# ------------------------------

def run_fraudleak_ai():
    print("\n---------------------------------------")
    print(" FRAUDLEAK AI - INTERNAL AUDIT ASSISTANT")
    print("---------------------------------------")

    excel_path = input("\nEnter the path of your transaction Excel file (.xlsx): ")

    try:
        df = pd.read_excel(excel_path)
    except:
        print("\n❌ ERROR: Cannot open the file. Check file name & path.")
        return

    ai = FraudLeakAI(threshold=0.7)

    print("\n⏳ Analyzing transaction data...")
    result = ai.detect_fraud(df)

    output_file = "fraudleak_output.xlsx"
    result.to_excel(output_file, index=False)

    print("\n✅ Analysis Complete!")
    print(f"📌 Fraud report generated: {output_file}")

    print("\nSummary:")
    print(result[result["Flagged"] == "YES"])

# ------------------------------
# MAIN
# ------------------------------

if __name__ == "__main__":
    run_fraudleak_ai()
