# Quant Challenge
Practice project based on a public JPMC Forage virtual experience. 
This repository contains my implementations of the practice tasks from the Virtual Experience on Forage.  
It covers **two main projects**:  

1. **Natural Gas Storage Pricing Model**  
   - Analyzed historical and forward monthly natural gas prices.  
   - Implemented **interpolation** and **extrapolation** to estimate prices at arbitrary dates.  
   - Modeled **injection** and **withdrawal** scenarios to understand storage economics.  
   - Visualized trends and extended forecasts for 1 year beyond available data.  

2. **Credit Risk Modeling**  
   - Predicted borrower **Probability of Default (PD)** using machine learning (Random Forest, Logistic Regression).  
   - Calculated **Expected Loss** using the risk framework:  
     \[
     EL = PD \times (1 - \text{Recovery Rate}) \times \text{Exposure at Default}
     \]  
   - Applied models to portfolio provisioning.  
   - **Quantized FICO scores** into categorical risk bands using **K-means clustering (MSE minimization)** to make them suitable for models requiring categorical input.  

---

## 🛠️ Skills & Tools
- **Python**: Pandas, NumPy, scikit-learn, Matplotlib  
- **Machine Learning**: Classification, Clustering, Interpolation/Extrapolation  
- **Risk Analytics**: Probability of Default (PD), Expected Loss, Recovery Rate  
- **Time Series Analysis**: Price interpolation, extrapolation, storage modeling  
- **Version Control**: Git, GitHub  

---

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/samarth-web/Quantitative-Research-Challenge.git

For educational purposes only; not affiliated with or endorsed by J.P. Morgan.
