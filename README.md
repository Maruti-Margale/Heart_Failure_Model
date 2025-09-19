# Heart_Failure_Model

live demo : https://heartfailuremodel-maruti.streamlit.app/


## 🧠 Heart Disease Prediction App – System Diagram

```mermaid
flowchart TD
    A["User Inputs Health Data
(Age, BP, Cholesterol, etc.)"] --> B["Streamlit UI Form"]
    B --> C["Feature Encoding
(Label & One-Hot Encoding)"]
    C --> D["KNN Model
(Heart_Failure_Prediction.pkl)"]
    D --> E{"Prediction:
Heart Disease?"}
    E -->|Yes| F["High Risk
Show Warning"]
    E -->|No| G["Low Risk
Show Success Message"]
    F --> H["Suggest Consulting Doctor"]
    G --> H
