# Heart_Failure_Model

live demo : https://heartfailuremodel-maruti.streamlit.app/


## 🧠 Heart Disease Prediction App – System Diagram

```mermaid
flowchart TD
    A[🧍 User Inputs Health Data\n(Age, BP, Cholesterol, etc.)] --> B[📊 Streamlit UI Form]
    B --> C[⚙️ Feature Encoding\n(Label & One-Hot Encoding)]
    C --> D[🤖 KNN Model\nHeart_Failure_Prediction.pkl]
    D --> E{🩺 Prediction:\nHeart Disease?}
    E -->|Yes| F[🔴 High Risk\nShow Warning]
    E -->|No| G[🟢 Low Risk\nShow Success Message]
    F --> H[📤 Suggest Consulting Doctor]
    G --> H
