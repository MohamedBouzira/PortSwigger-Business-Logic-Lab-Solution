# PortSwigger-Business-Logic-Lab-Solution
python tool to solve "Infinity Money logic flaw" Lab in PortSwigger academy without BurpSuite Pro , semi automated 

**Lab:** Infinite money logic flaw 
**Difficulty:** Practitioner  

## 💡 Idea
The lab has Domain specific flaw   
you can buy a gift card with promo code and redeem the card to get the full money back 

## ✅ Solution
This Python tool automates this process:
- Logs in.
- buy the gift card with the promo code
- resell it with the full price
- Works much faster than Burp Community.


## 🛠 Tools
- `businessLogicLab.py` — Basic single-threaded version.
- `businessLogicLab_enhanced.py` — Faster, threaded, but it can cause problems when so many threads

## 🚀 Usage
1. **Clone the repo**  
   ```bash
   git clone <repo.git>

2. **change Url and run the script**  
