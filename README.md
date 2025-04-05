# OpenTrade Specification Framework
An open specification for standardized and interoperable contextual trade balance evaluation and expression built on today's ISO and international trade standards.

## Keywords:
- Trade Balance Transparency Framework
- Trade Balance Normalization Formula
- Trade Balance Formula
- Interoperable Trade Adjustment Framework
- OpenTrade Interoperability Standards
- TradeFlux: OpenTrade Transparency Dashboard
  - Realtime Trade Valuations based on Open Standards
  - Trade and Economy Simulations 

---

# 📄 **TBF-101 (Draft v0.2)**

### **Trade Balance Coding and Fee Adjustment Standard**

#### A specification for standardized, contextual trade balance evaluation and expression

**Proposed under:** *International Standards Organization for Global Trade (ISO-GTBC)*\
**Status:** Draft Proposal\
**Version:** 0.2\
**Editor:** Chris Heney (Author)\
**Last updated:** April 2025

---

## 1. 🔍 Purpose & Scope

TBF-101 defines a **universal coding system** for expressing **fee adjustments**, **subsidies**, and **barriers** in international trade. Its goal is to **normalize and contextualize** trade balance evaluations by:

- Capturing real-world adjustments (tariffs, subsidies, etc.) in a machine-readable, multi-context format.
- Enabling composable fee structures applicable to **multiple commodities** or **specific scenarios**.
- Enabling **blockchain**, **customs**, and **API-ready** implementations.

---

## 2. 🔧 Format Overview

### 📌 **Formal Syntax**

```txt
[GF][GT]-[T][CC].[SS].[DDDD]-[CF][HS]
```

### 📌 **Segments Defined**

| Segment | Description                                                          |
| ------- | -------------------------------------------------------------------- |
| `GF`    | **Geo From** (ISO 3166-1 alpha-2) origin country                     |
| `GT`    | **Geo To** (ISO 3166-1 alpha-2) destination country                  |
| `T`     | **Type of Adjustment** (e.g., T=Tariff, S=Subsidy, N=NTB)            |
| `CC`    | **Top-Level Category** (Tariff, Subsidy, etc.)                       |
| `SS`    | **Subcategory** (e.g., Anti-dumping, Tax credit)                     |
| `DDDD`  | **Detailed Condition/Policy Layer** (e.g., High demand, Wartime)     |
| `CF`    | **Context Function** (e.g., AV = Avg if Commodity more granular)     |
| `HS`    | **Commodity Context**, defined using latest **Schedule B (HS Code)** |

---

## 3. 🧱 Components & Semantics

### 🔠 **Type (T)**

Indicates both **class** and **direction** of value.

| Code | Meaning                  | Effect   |
| ---- | ------------------------ | -------- |
| T    | Tariff                   | Negative |
| S    | Subsidy                  | Positive |
| N    | NTB (Non-Tariff Barrier) | Negative |
| R    | Relief/Incentive         | Positive |

---

### 🔢 **Adjustment Categories (CC) and Subcategories (SS)**

| T | CC | SS | Description       |
| - | -- | -- | ----------------- |
| T | 01 | 01 | MFN Tariff        |
| T | 01 | 02 | Anti-Dumping      |
| S | 02 | 01 | Export Tax Credit |
| N | 03 | 01 | Quotas            |
| R | 04 | 01 | Stimulus Relief   |

---

### 🧬 **Detail Layer (DDDD)**

This field encodes **specific conditions**, policies, or temporal modifiers. It allows **granular context** to be applied or overridden, such as:

| DDDD | Description            |
| ---- | ---------------------- |
| 1001 | High Demand Exception  |
| 2001 | War-time Adjustment    |
| 3002 | Supply Chain Emergency |
| 9999 | Universal Application  |

---

### 🧠 **Context Function (CF)**

CF = **[Granularity Prefix][Function Type]**

| Prefix | Meaning                             |
| ------ | ----------------------------------- |
| A      | Adjustment context is more granular |
| C      | Commodity context is more granular  |
| B      | Both are granular                   |

| Function | Description |
| -------- | ----------- |
| A        | Minimum     |
| Z        | Maximum     |
| S        | Sum         |
| V        | Average     |
| M        | Multiply    |
| D        | Divide      |
| O        | Override    |

---

## 4. 📘 Example Encodings

### Example A: Basic Tariff on Steel

**U.S. applies 10% MFN tariff on all iron and steel products.**

```
USCN-T01.01.9999-CS72
```

- **US to CN**
- **Tariff > MFN > universal**
- **Commodity-specific: HS72 (Steel)**
- **Commodity is more granular, use Sum**

---

### Example B: Specific Subsidy Exception During High Demand

**China subsidizes solar panel exports unless made with steel.**

```txt
CNUA-S02.01.1001-AS85
```

- China to U.S.
- Subsidy → Tax credit → High Demand (1001)
- Commodity: HS85 (Electrical Equipment incl. Solar)
- Adjustment granularity overrides general steel tariff for energy

---

### Example C: Override Tariff on a Specific Steel Class

**U.S. adds a steel exemption for medical supply producers**

```txt
USCN-T01.01.3002-BO7216
```

- 7216 = Angles, shapes, and sections of iron/steel
- Applies an **override** to a wartime adjustment (Detail = 3002)
- BO = Either context can trigger override

---

## 5. 📦 Example Ledger Entry (Customs Blockchain)

```json
{
  "transaction_id": "TXN-87999313",
  "timestamp": "2025-04-05T17:25:43Z",
  "exporter": "CN",
  "importer": "US",
  "value_usd": 5_000_000,
  "commodity_hs": "7216",
  "adjustments": [
    {
      "code": "USCN-T01.01.3002-BO7216",
      "value": -0.00,
      "description": "Steel exemption override for medical sectors (wartime)"
    },
    {
      "code": "USCN-S02.01.1001-AS85",
      "value": 500_000,
      "description": "High-demand solar export subsidy from CN"
    }
  ],
  "FAB_adjusted_value": 5_500_000
}
```

---

## 6. 🔁 Application Scenarios

### 📘 *User Story: High-Demand Exception*

> “A U.S. importer brings in solar panels (HS85) under a high-demand exception (1001). While steel normally incurs a 10% tariff (T01.01), the high-demand policy allows an override under the subsidy function for clean tech. The FAB value rises accordingly.”

### 📘 *User Story: Layered Context*

> “An exporter from Mexico ships electronics (HS85) that fall under both a general subsidy and a wartime NTB. Because the commodity context is more specific, the CF of `CS` applies a `SUM`, adding both values into the FAB.”

---

## 7. 🔮 Next Steps

- ✅ Finalize the **spreadsheet version** with seed data (TBC + HS codes)
- ✅ Generate **prisma.schema** and TypeScript interfaces
- ✅ Build an **Express API** to evaluate FAB based on transactions
- ✅ Create **SDKS**


