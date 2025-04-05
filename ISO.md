**ISO/GTBC 1001:2025**
*Trade Balance Coding and Fee Adjustment Standard (TBF-101)*

---

### **INTERNATIONAL STANDARD**

**ISO/GTBC 1001:2025**
Issued: April 2025\
Draft Version: 0.2\
Prepared by: International Standards Organization for Global Trade (ISO-GTBC)

---

## **Contents**

1. Scope
2. Normative References
3. Terms and Definitions
4. Code Structure
5. Functional Logic
6. Encoding Scheme
7. Application Examples
8. Ledger Integration
9. Implementation Guidance
10. Annex A: Reference Tables
11. Annex B: Schedule B and HS Integration
12. Bibliography

---

## **1. Scope**

This standard establishes a structured format and data model for coding and expressing trade balance adjustments in international trade transactions. Known as the Trade Balance Formula (TBF-101), this specification supports the standardized representation of tariffs, subsidies, non-tariff barriers, and contextual overrides applied to cross-border commodity flows.

TBF-101 is designed to:

- Enable uniform representation of fee adjustments
- Support multi-level context encoding (adjustment & commodity)
- Facilitate integration with customs systems, blockchains, and API infrastructure
- Reduce financial arbitrage and improve transparency

---

## **2. Normative References**

- ISO 3166-1: Country Code Standard
- Harmonized System (HS) 2025 Edition – World Customs Organization
- United States Census Schedule B 2025
- OECD Glossary of Statistical Terms: Trade Subsidies & Tariffs
- WTO Tariff Profiles

---

## **3. Terms and Definitions**

- **Trade Balance Code (TBC):** A structured alphanumeric identifier representing a specific fee, tariff, subsidy, or regulatory adjustment applied to international trade.
- **Fee-Adjusted Trade Balance (FAB):** The net difference between export and import values, adjusted by applicable TBCs.
- **Context Function (CF):** A two-character code representing contextual logic for combining or overriding multiple TBCs.
- **Adjustment Granularity:** The level of detail applied to the policy or fee condition.
- **Commodity Granularity:** The level of detail applied to the product categorization (Schedule B/HS).

---

## **4. Code Structure**

### **Formal Syntax**

```
[GF][GT]-[T][CC].[SS].[DDDD]-[CF][HS]
```

### **Segment Definitions**

| Field | Description                                                                       |
| ----- | --------------------------------------------------------------------------------- |
| GF    | Geographic From – ISO 3166-1 alpha-2 country code (origin)                        |
| GT    | Geographic To – ISO 3166-1 alpha-2 country code (destination)                     |
| T     | Type – One-letter code for Tariff (T), Subsidy (S), NTB (N), Relief (R)           |
| CC    | Category Code – Two-digit numeric high-level classification                       |
| SS    | Subcategory Code – Two-digit numeric subcategory                                  |
| DDDD  | Detailed Condition – Four-digit numeric condition code (e.g. policy or exception) |
| CF    | Context Function – Two-character code defining combination logic                  |
| HS    | Harmonized System code (Schedule B-compatible commodity reference)                |

---

## **5. Functional Logic**

Each TBC is applied to a trade value and affects the FAB (Fee-Adjusted Trade Balance) using context-aware functions:

### **Context Prefix**

| Code | Description                         |
| ---- | ----------------------------------- |
| A    | Adjustment context is more granular |
| C    | Commodity context is more granular  |
| B    | Both contexts are granular          |

### **Function Types**

| Code | Operation |
| ---- | --------- |
| A    | Minimum   |
| Z    | Maximum   |
| S    | Sum       |
| V    | Average   |
| M    | Multiply  |
| D    | Divide    |
| O    | Override  |

---

## **6. Encoding Scheme**

TBCs are composable and can reflect:

- General application (universal codes)
- Product-specific rules (via HS codes)
- Scenario-based exceptions (e.g., wartime, high demand)

Sample Code:

```
USCN-T01.01.1001-AS85
```

> U.S. to China tariff, MFN classification, high demand exception applied, affects HS 85 (electrical)

---

## **7. Application Examples**

- **Basic Tariff:** `USCN-T01.01.9999-CS72`
- **High-Demand Subsidy Exception:** `CNUA-S02.01.1001-AS85`
- **Medical Supply Steel Override:** `USCN-T01.01.3002-BO7216`

---

## **8. Ledger Integration**

Each TBC may be attached to transaction records:

```json
{
  "transaction_id": "TXN-001",
  "value_usd": 1000000,
  "exporter": "CN",
  "importer": "US",
  "hs_code": "7216",
  "adjustments": [
    {
      "code": "USCN-T01.01.3002-BO7216",
      "value": -0.00
    },
    {
      "code": "USCN-S02.01.1001-AS85",
      "value": 50000
    }
  ],
  "FAB_value": 1050000
}
```

---

## **9. Implementation Guidance**

- Maintain a central TBC registry (publicly accessible)
- Map HS codes to legal references, WTO bindings, and subsidy lists
- Support versioning for policy shifts
- Ensure compatibility with customs and logistics APIs

---

## **10. Annex A: Reference Tables**

- T Code Index
- Category/Subcategory Tables
- Common Detail Codes (DDDD)
- Sample Context Functions

## **11. Annex B: Schedule B and HS Integration**

- HS Chapter-to-TBC examples
- Cross-reference logic for multi-category goods

## **12. Bibliography**

- WTO: Trade Profiles 2024
- WCO: Harmonized System Explanatory Notes
- OECD: Trade Statistics Glossary
- ISO 3166-1
- U.S. Census Schedule B Index (2025)

---

**End of Document**

