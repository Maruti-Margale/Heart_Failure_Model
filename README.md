# Heart_Failure_Model

live demo : https://heartfailuremodel-maruti.streamlit.app/

## 🧠 Heart Disease Prediction App – System Diagram

```mermaid
flowchart TD
    A[🧍 User Inputs Health Data<br/>(Age, BP, Cholesterol, etc.)] --> B[📊 Streamlit UI Form]
    B --> C[⚙️ Feature Encoding<br/>(Label & One-Hot Encoding)]
    C --> D[🤖 KNN Model<br/>Heart_Failure_Prediction.pkl]
    D --> E{🩺 Prediction:<br/>Heart Disease?}
    E -->|Yes| F[🔴 High Risk<br/>Show Warning]
    E -->|No| G[🟢 Low Risk<br/>Show Success Message]
    F --> H[📤 Suggest Consulting Doctor]
    G --> H

