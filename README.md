# Interactive Linear Regression Visualizer with CRISP-DM

這是一個互動式線性回歸視覺化工具，完整實作 CRISP-DM (Cross-Industry Standard Process for Data Mining) 方法論，透過 Streamlit 提供直觀的網頁介面。

## 🌐 Demo Site

**線上展示**: [https://your-app.streamlit.app/](https://your-app.streamlit.app/)  
*(部署後請更新此連結)*

## 📋 專案簡介

本專案提供一個教學用的互動式線性回歸工具，使用者可以：
- 調整線性方程式的參數（斜率 a、截距 b）
- 控制資料的雜訊程度
- 改變資料點數量
- 即時觀察模型效能變化

## ✨ 專案特色

- 📊 **完整 CRISP-DM 流程**: 從商業理解到部署的六個階段
- 🎛️ **參數可調整**: 斜率、截距、雜訊、資料點數量、測試集比例
- 📈 **豐富視覺化**: 回歸線圖、預測比較圖、殘差分析圖
- 🔄 **即時更新**: 參數改變時立即重新訓練和顯示結果
- 📚 **教育導向**: 清楚解釋每個步驟和決策

## 🔄 CRISP-DM 方法論

本專案完整實現資料科學標準流程：

1. **Business Understanding** (商業理解)
   - 定義專案目標和成功標準
   - 理解線性回歸的應用場景

2. **Data Understanding** (資料理解)
   - 探索資料生成機制
   - 展示資料統計特性

3. **Data Preparation** (資料準備)
   - 訓練/測試集分割
   - 資料品質檢查

4. **Modeling** (建模)
   - 使用 Scikit-learn 線性回歸
   - 比較學習參數與真實參數

5. **Evaluation** (評估)
   - MSE (Mean Squared Error)
   - R² Score (決定係數)
   - 多角度視覺化分析

6. **Deployment** (部署)
   - Streamlit Cloud 部署
   - 提供公開訪問 URL

## 🚀 快速開始

### 線上使用

直接訪問部署的網站：[https://your-app.streamlit.app/](https://your-app.streamlit.app/)

### 本地執行

```bash
# 1. 克隆專案
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

# 2. 安裝依賴套件
pip install -r requirements.txt

# 3. 執行應用程式
streamlit run app.py
```

應用程式會在瀏覽器自動開啟（預設：http://localhost:8501）

## 🎯 功能說明

### 互動式參數控制

| 參數 | 範圍 | 說明 |
|------|------|------|
| 斜率 (a) | -10.0 ~ 10.0 | 控制直線的傾斜程度 |
| 截距 (b) | -10.0 ~ 10.0 | 控制直線與 y 軸的交點 |
| 雜訊程度 (σ) | 0.0 ~ 5.0 | 高斯雜訊的標準差 |
| 資料點數量 | 50 ~ 500 | 生成的樣本數量 |
| 測試集比例 | 10% ~ 40% | 用於評估的資料比例 |

### 視覺化輸出

1. **回歸線圖**: 顯示資料點、真實線（綠色虛線）、預測線（紅色實線）
2. **預測比較圖**: 預測值 vs 實際值，完美預測會在 45° 對角線上
3. **殘差圖**: 檢查誤差是否隨機分布，無系統性偏差

### 評估指標

- **MSE (Mean Squared Error)**: 平均平方誤差，越小越好
- **R² Score**: 決定係數，範圍 0~1，越接近 1 表示模型越好

## 技術棧

- **Python 3.8+**
- **Streamlit**: 網頁應用框架
- **NumPy**: 數值計算
- **Pandas**: 資料處理
- **Scikit-learn**: 機器學習模型
- **Matplotlib & Seaborn**: 資料視覺化

## 📁 專案結構

```
HW1/
├── app.py                    # 主要 Streamlit 應用程式
├── requirements.txt          # Python 依賴套件
├── .gitignore               # Git 忽略檔案
├── README.md                # 專案說明（本檔案）
├── 0_devLog.md             # 開發日誌
├── Development.md           # 詳細開發記錄
├── DEPLOYMENT.md           # 部署指南
├── prompt.md               # 原始需求
└── log.md                  # 簡易記錄
```

## 📦 部署到 Streamlit Cloud

### 快速部署步驟

1. **推送到 GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```

2. **Streamlit Cloud 設定**
   - 前往 [Streamlit Cloud](https://streamlit.io/cloud)
   - 使用 GitHub 帳號登入
   - 點擊 "New app"
   - 選擇您的倉庫
   - 主檔案路徑：`app.py`
   - 點擊 "Deploy"

3. **等待部署完成**（通常 2-5 分鐘）

詳細部署說明請參考 [DEPLOYMENT.md](DEPLOYMENT.md)

## 📚 開發文件

- **[0_devLog.md](0_devLog.md)**: 開發日誌，記錄每個開發步驟
- **[Development.md](Development.md)**: 詳細的 CRISP-DM 實作過程和技術決策
- **[DEPLOYMENT.md](DEPLOYMENT.md)**: 完整的部署指南和常見問題

## 🎓 學習重點

透過本專案，您可以學習到：

- ✅ CRISP-DM 方法論的實際應用
- ✅ 線性回歸的工作原理和效能評估
- ✅ Streamlit 互動式網頁應用開發
- ✅ Python 資料科學工具鏈（NumPy, Pandas, Scikit-learn, Matplotlib）
- ✅ 從開發到部署的完整流程

## 📄 授權

MIT License

## 👤 作者

**AIoT HW1 Project**

如有問題或建議，歡迎開 Issue 或 Pull Request！

---

**⭐ 如果這個專案對您有幫助，請給個星星支持！**
