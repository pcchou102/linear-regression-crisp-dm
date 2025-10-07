# Development Log (開發日誌)

## 專案概述
**專案名稱**: Simple Linear Regression with CRISP-DM  
**開發日期**: 2025-10-07 ~ 2025-10-08  
**目標**: 建立一個互動式線性回歸視覺化工具，完整實作 CRISP-DM 方法論

---

## 開發步驟

### 1.0 專案初始化
- **時間**: 2025-10-07
- **動作**:
  - 建立專案資料夾結構
  - 建立 `prompt.md` 記錄需求
  - 建立 `log.md` 作為快速記錄

### 2.0 需求分析
- **動作**:
  - 分析 prompt.md 中的需求
  - 確認需要實作 CRISP-DM 六個步驟
  - 確認需要 Streamlit 互動介面
  - 確認參數可調整：a (斜率), b (截距), noise, n_points

### 3.0 建立專案基礎檔案
- **動作**:
  - 建立 `requirements.txt` - 列出所有必要套件
  - 建立 `.gitignore` - 排除不必要的檔案
  - 建立 `README.md` - 專案說明文件

**requirements.txt 內容**:
```
streamlit==1.31.0
numpy==1.24.3
pandas==2.0.3
matplotlib==3.7.2
scikit-learn==1.3.0
seaborn==0.12.2
```

### 4.0 撰寫開發文件
- **動作**:
  - 建立 `Development.md` - 詳細的 CRISP-DM 實作記錄
  - 記錄每個步驟的決策理由
  - 記錄技術選擇和架構設計

### 5.0 實作核心功能
- **動作**:
  - 建立 `app.py` - 主要 Streamlit 應用程式
  - 實作資料生成函數: `generate_data()`
  - 實作模型訓練函數: `train_model()`
  - 實作模型評估函數: `evaluate_model()`

**核心函數架構**:
```python
def generate_data(a, b, noise, n_points, random_state=42)
def train_model(X_train, y_train)
def evaluate_model(model, X_test, y_test)
```

### 6.0 實作視覺化功能
- **動作**:
  - 實作回歸線繪圖: `plot_regression()`
  - 實作預測值比較圖: `plot_predictions_vs_actual()`
  - 實作殘差圖: `plot_residuals()`

**視覺化特色**:
- 三種圖表呈現不同分析角度
- 清楚標示真實線與預測線
- 使用顏色區分不同元素

### 7.0 建立 Streamlit 介面
- **動作**:
  - 設定頁面配置和標題
  - 建立側邊欄參數控制區
  - 使用 Tabs 組織 CRISP-DM 六個步驟
  - 整合資料生成、訓練、評估和視覺化

**介面元件**:
- 側邊欄滑桿: 控制 a, b, noise, n_points, test_size
- 6 個 Tabs: 對應 CRISP-DM 六個階段
- 即時更新: 參數改變時自動重新計算

### 8.0 完整實作 CRISP-DM 步驟

#### Tab 1: Business Understanding
- 說明專案目標
- 定義成功標準
- 解釋為何選擇線性回歸

#### Tab 2: Data Understanding
- 顯示資料生成公式
- 展示資料統計摘要
- 提供樣本資料預覽

#### Tab 3: Data Preparation
- 執行訓練/測試集分割
- 說明資料特性
- 顯示分割結果統計

#### Tab 4: Modeling
- 訓練線性回歸模型
- 顯示學習到的參數
- 比較真實參數與學習參數

#### Tab 5: Evaluation
- 計算 MSE 和 R² 指標
- 提供效能解釋
- 展示三種視覺化圖表

#### Tab 6: Deployment
- 說明部署策略
- 提供使用指南
- 列出學習重點

### 9.0 建立部署文件
- **動作**:
  - 建立 `DEPLOYMENT.md` - 詳細部署指南
  - 涵蓋 GitHub 推送步驟
  - 涵蓋 Streamlit Cloud 部署步驟
  - 提供常見問題解答

### 10.0 本地測試
- **動作**:
  - 測試所有參數調整功能
  - 驗證圖表正確顯示
  - 檢查評估指標計算正確性
  - 確認所有 Tabs 正常運作

**測試情境**:
- Noise = 0: 應該得到 R² ≈ 1.0
- Noise 增加: R² 應該降低，MSE 應該增加
- 不同斜率和截距: 模型應該正確學習
- 不同資料點數: 更多資料點應該得到更穩定的估計

### 11.0 程式碼優化
- **動作**:
  - 添加完整的 docstrings
  - 優化圖表大小和樣式
  - 確保 `plt.close()` 避免記憶體洩漏
  - 使用 Seaborn 美化視覺效果

### 12.0 文件完善
- **動作**:
  - 完善 README.md
  - 更新 Development.md
  - 確保所有文件內容一致
  - 添加使用範例和截圖說明

---

## 技術細節

### 環境設定
```bash
# 建立虛擬環境（建議）
python -m venv venv
venv\Scripts\activate

# 安裝依賴
pip install -r requirements.txt

# 執行應用程式
streamlit run app.py
```

### 關鍵技術決策

1. **選擇 Streamlit 而非 Flask**
   - 理由: 更快速的開發、內建互動元件、自動重新整理
   - 適合: 資料科學專案的快速原型和展示

2. **使用合成資料而非真實資料**
   - 理由: 完全可控、易於理解因果關係
   - 適合: 教學和概念驗證

3. **採用 Sklearn 的 LinearRegression**
   - 理由: 穩定可靠、無需調參、標準實作
   - 適合: 簡單線性回歸問題

4. **Tabs 組織 CRISP-DM 步驟**
   - 理由: 清楚的結構、易於導航
   - 適合: 步驟化的流程展示

### 專案結構
```
HW1/
├── app.py                    # 主要 Streamlit 應用
├── requirements.txt          # Python 依賴套件
├── .gitignore               # Git 忽略檔案
├── README.md                # 專案說明
├── Development.md           # 詳細開發記錄（英文）
├── 0_devLog.md             # 開發日誌（本檔案）
├── DEPLOYMENT.md           # 部署指南
├── prompt.md               # 原始需求
└── log.md                  # 簡易記錄
```

---

## 遇到的挑戰與解決方案

### 挑戰 1: 參數更新時的效能
**問題**: 每次調整參數都會重新執行整個腳本  
**解決**: 
- 接受 Streamlit 的設計理念（reactive programming）
- 線性回歸計算很快，不需要快取
- 若需要可使用 `@st.cache_data` 裝飾器

### 挑戰 2: 圖表記憶體管理
**問題**: Matplotlib 圖表可能造成記憶體洩漏  
**解決**: 
- 每次繪圖後呼叫 `plt.close()`
- 使用 `st.pyplot(fig)` 正確顯示圖表

### 挑戰 3: 中文支援
**問題**: Matplotlib 預設不支援中文  
**解決**: 
- 使用英文標籤和說明
- 或安裝中文字型並設定 `plt.rcParams['font.sans-serif']`

---

## 測試結果

### 功能測試
- ✅ 參數調整功能正常
- ✅ 資料生成正確
- ✅ 模型訓練成功
- ✅ 評估指標正確
- ✅ 視覺化清晰美觀
- ✅ CRISP-DM 步驟完整

### 邊界測試
- ✅ Noise = 0: R² = 1.0 (完美擬合)
- ✅ Noise = 5.0: R² 顯著降低
- ✅ 50 個資料點: 結果合理但較不穩定
- ✅ 500 個資料點: 結果穩定可靠
- ✅ 極端斜率/截距: 模型正確學習

---

## 部署準備

### GitHub 推送
```bash
git init
git add .
git commit -m "Initial commit: Linear Regression with CRISP-DM"
git remote add origin <your-repo-url>
git push -u origin main
```

### Streamlit Cloud 部署
1. 登入 [Streamlit Cloud](https://streamlit.io/cloud)
2. 連接 GitHub 帳號
3. 選擇倉庫和 branch
4. 設定主檔案: `app.py`
5. 點擊 Deploy

### 部署檢查清單
- ✅ requirements.txt 正確
- ✅ .gitignore 排除虛擬環境
- ✅ README.md 包含部署連結
- ✅ app.py 可獨立執行
- ✅ 無硬編碼路徑

---

## 後續改進方向

### 短期
- [ ] 添加資料匯出功能
- [ ] 支援多項式回歸
- [ ] 添加更多評估指標（MAE, RMSE）
- [ ] 互動式圖表（Plotly）

### 中期
- [ ] 支援上傳 CSV 檔案
- [ ] 比較多種回歸演算法
- [ ] 添加交叉驗證
- [ ] 支援多變數回歸

### 長期
- [ ] 完整的機器學習教學平台
- [ ] 支援更多演算法
- [ ] 多國語言介面
- [ ] 使用者帳號系統

---

## 專案成果

### 完成項目
1. ✅ 完整的 CRISP-DM 實作
2. ✅ 互動式 Streamlit 應用
3. ✅ 可調整的參數控制
4. ✅ 完整的視覺化分析
5. ✅ 詳細的文件記錄
6. ✅ 準備好 GitHub 和 Streamlit Cloud 部署

### 學習成果
- 深入理解 CRISP-DM 方法論
- 掌握 Streamlit 開發技巧
- 實作線性回歸的完整流程
- 學習資料視覺化最佳實踐
- 體驗從開發到部署的完整週期

---

## 總結

本專案成功實現了一個功能完整、介面友善的線性回歸教學工具。透過 CRISP-DM 方法論的指引，我們系統化地完成了從需求分析到部署的每個步驟。專案不僅達成了原始需求，還提供了豐富的互動功能和清晰的視覺化，適合作為學習和展示用途。

**專案時間**: 2025-10-07 ~ 2025-10-08  
**開發語言**: Python 3.8+  
**主要框架**: Streamlit, Scikit-learn  
**部署平台**: Streamlit Cloud  
**專案狀態**: ✅ 完成並準備部署
