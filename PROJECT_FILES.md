# 專案檔案總覽

本文件說明專案中每個檔案的用途和內容。

## 📂 專案結構

```
HW1/
├── .streamlit/              # Streamlit 配置資料夾
│   └── config.toml         # Streamlit 外觀和行為設定
├── .gitignore              # Git 忽略檔案清單
├── app.py                  # 主要應用程式（核心檔案）⭐
├── requirements.txt        # Python 依賴套件清單
├── README.md              # 專案說明文件（首頁）⭐
├── 0_devLog.md            # 開發日誌
├── Development.md         # 詳細開發記錄（CRISP-DM）
├── DEPLOYMENT.md         # 部署指南
├── GitHub_Push_Guide.md  # GitHub 推送教學
├── PROJECT_FILES.md      # 專案檔案總覽（本檔案）
├── run_app.bat           # Windows 快速啟動腳本
├── prompt.md             # 原始需求文件
└── log.md                # 簡易記錄
```

---

## 📄 檔案說明

### 🔴 核心檔案（必要）

#### `app.py`
- **用途**: Streamlit 主應用程式
- **內容**: 
  - 資料生成函數
  - 線性回歸模型訓練
  - 模型評估函數
  - 視覺化函數（3 種圖表）
  - Streamlit UI（6 個 CRISP-DM 標籤頁）
- **行數**: ~500 行
- **語言**: Python

#### `requirements.txt`
- **用途**: 列出專案所需的 Python 套件
- **內容**:
  ```
  streamlit==1.31.0
  numpy==1.24.3
  pandas==2.0.3
  matplotlib==3.7.2
  scikit-learn==1.3.0
  seaborn==0.12.2
  ```
- **用途**: 部署時自動安裝依賴

#### `README.md`
- **用途**: 專案首頁說明文件
- **內容**:
  - 專案簡介
  - Demo 網站連結
  - 功能特色
  - 快速開始指南
  - 使用說明
  - 部署步驟
- **對象**: GitHub 訪客、使用者

---

### 🟡 配置檔案

#### `.gitignore`
- **用途**: 告訴 Git 哪些檔案不要追蹤
- **內容**: 排除 Python 快取、虛擬環境、IDE 設定等
- **重要性**: 避免上傳不必要的檔案到 GitHub

#### `.streamlit/config.toml`
- **用途**: Streamlit 應用程式配置
- **內容**:
  - 主題顏色設定
  - 伺服器配置
  - 瀏覽器行為
- **效果**: 統一應用程式外觀

---

### 🟢 文件檔案

#### `0_devLog.md`
- **用途**: 開發日誌
- **內容**:
  - 時間軸格式的開發步驟
  - 每個步驟的動作和結果
  - 技術決策記錄
  - 遇到的問題和解決方案
- **對象**: 開發者、審查者

#### `Development.md`
- **用途**: 詳細的開發過程記錄
- **內容**:
  - CRISP-DM 六個步驟的詳細實作
  - 每個步驟的決策理由
  - 技術選擇說明
  - 程式架構設計
- **長度**: 約 400+ 行
- **對象**: 想深入了解專案的人

#### `DEPLOYMENT.md`
- **用途**: 部署指南
- **內容**:
  - GitHub 推送步驟
  - Streamlit Cloud 部署教學
  - 常見問題解答
  - 疑難排解
- **對象**: 想要部署此專案的人

#### `GitHub_Push_Guide.md`
- **用途**: GitHub 操作快速參考
- **內容**:
  - 創建 GitHub 倉庫步驟
  - Git 命令清單
  - 常用操作說明
- **對象**: Git 初學者

#### `PROJECT_FILES.md`
- **用途**: 專案檔案總覽（本檔案）
- **內容**: 解釋每個檔案的用途和內容

---

### 🔵 工具檔案

#### `run_app.bat`
- **用途**: Windows 快速啟動腳本
- **功能**:
  - 檢查 Streamlit 是否已安裝
  - 如未安裝，自動安裝依賴
  - 啟動 Streamlit 應用
- **使用方式**: 雙擊執行

---

### ⚪ 原始檔案

#### `prompt.md`
- **用途**: 原始專案需求
- **內容**:
  - 專案目標
  - 必須實作的功能
  - 技術要求
- **來源**: 作業需求

#### `log.md`
- **用途**: 簡易快速記錄
- **內容**: 可能是開發過程的簡短筆記

---

## 🎯 檔案重要性分級

### ⭐⭐⭐ 必要檔案（沒有它們無法運行）
- `app.py` - 主程式
- `requirements.txt` - 依賴清單

### ⭐⭐ 重要檔案（強烈建議保留）
- `README.md` - 專案說明
- `.gitignore` - Git 配置
- `.streamlit/config.toml` - Streamlit 配置

### ⭐ 輔助檔案（幫助理解和使用）
- `0_devLog.md` - 開發記錄
- `Development.md` - 詳細文件
- `DEPLOYMENT.md` - 部署指南
- `GitHub_Push_Guide.md` - Git 教學

### 其他檔案
- `PROJECT_FILES.md` - 檔案說明（本檔案）
- `run_app.bat` - 便利工具
- `prompt.md` - 原始需求
- `log.md` - 筆記

---

## 📊 檔案統計

| 類型 | 數量 | 說明 |
|------|------|------|
| Python 程式 | 1 | app.py |
| Markdown 文件 | 8 | 各種說明文件 |
| 配置檔案 | 3 | .gitignore, config.toml, requirements.txt |
| 批次檔 | 1 | run_app.bat |
| **總計** | **13** | - |

---

## 🔄 檔案使用流程

### 開發階段
1. 閱讀 `prompt.md` 了解需求
2. 參考 `Development.md` 進行開發
3. 編寫 `app.py` 實作功能
4. 記錄到 `0_devLog.md`
5. 更新 `README.md`

### 測試階段
1. 執行 `run_app.bat` 啟動應用
2. 或手動執行 `streamlit run app.py`
3. 在瀏覽器測試功能

### 部署階段
1. 參考 `GitHub_Push_Guide.md` 推送到 GitHub
2. 參考 `DEPLOYMENT.md` 部署到 Streamlit Cloud
3. 更新 `README.md` 中的 Demo 連結

### 使用階段
1. 使用者閱讀 `README.md` 了解專案
2. 訪問線上 Demo 或本地執行
3. 開發者可參考 `Development.md` 了解實作細節

---

## 💡 使用建議

### 對於使用者
- 先閱讀 `README.md`
- 訪問線上 Demo 或下載專案本地執行
- 有問題查看 `DEPLOYMENT.md`

### 對於開發者
- 閱讀 `Development.md` 了解設計決策
- 查看 `0_devLog.md` 了解開發過程
- 修改 `app.py` 進行客製化

### 對於學習者
- 按順序閱讀：`README.md` → `Development.md` → `app.py`
- 了解 CRISP-DM 方法論的實際應用
- 學習 Streamlit 開發技巧

---

## 📝 維護建議

### 定期更新
- `README.md` - 保持資訊最新
- `requirements.txt` - 更新套件版本（注意相容性）
- `0_devLog.md` - 記錄重大變更

### 版本控制
- 使用 Git 追蹤所有變更
- 重要更新建立 Git tag
- 寫清楚的 commit message

### 文件同步
- 程式碼變更時同步更新文件
- 確保範例程式碼可執行
- 截圖和說明保持一致

---

**最後更新**: 2025-10-08  
**專案版本**: 1.0  
**狀態**: ✅ 準備部署
