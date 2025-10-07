# 🚀 快速開始指南

**歡迎！** 這是您的線性回歸專案，已經完全準備好部署了！

---

## ⚡ 3 步驟部署到網路

### 步驟 1: 推送到 GitHub（5 分鐘）

在 PowerShell 中執行：

```powershell
# 切換到專案目錄
cd "c:\Users\周\Desktop\AIOT\HW1"

# 初始化 Git
git init

# 添加所有檔案
git add .

# 提交
git commit -m "Initial commit: Linear Regression with CRISP-DM"

# 連接到 GitHub（請先在 GitHub 建立新倉庫）
# 將下面的 YOUR_USERNAME 和 YOUR_REPO_NAME 改成您的
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# 推送
git branch -M main
git push -u origin main
```

**注意**: 在執行 `git remote add` 之前，請先：
1. 前往 https://github.com
2. 點擊右上角 `+` → `New repository`
3. 輸入倉庫名稱（建議：`linear-regression-crisp-dm`）
4. 選擇 `Public`（公開）
5. **不要**勾選任何初始化選項
6. 點擊 `Create repository`
7. 複製倉庫 URL

### 步驟 2: 部署到 Streamlit Cloud（3 分鐘）

1. 前往 https://streamlit.io/cloud
2. 使用 GitHub 帳號登入
3. 點擊 `New app`
4. 選擇：
   - Repository: 您剛才建立的倉庫
   - Branch: `main`
   - Main file path: `app.py`
5. 點擊 `Deploy!`
6. 等待 2-5 分鐘

### 步驟 3: 更新 README（1 分鐘）

1. 複製 Streamlit Cloud 給您的 URL（例如：`https://your-app.streamlit.app/`）
2. 打開 `README.md`
3. 將所有 `https://your-app.streamlit.app/` 替換成您的實際 URL
4. 推送更新：
   ```powershell
   git add README.md
   git commit -m "Update demo site URL"
   git push
   ```

---

## 🏠 本地測試（可選）

在推送到 GitHub 之前，您可以先在本地測試：

### 方法 1: 使用批次檔（最簡單）
雙擊 `run_app.bat` 檔案

### 方法 2: 使用命令列
```powershell
# 安裝依賴（第一次執行）
pip install -r requirements.txt

# 執行應用
streamlit run app.py
```

應用會在瀏覽器自動開啟 http://localhost:8501

---

## 📋 需要幫助？

### 詳細指南
- **Git 操作**: 查看 `GitHub_Push_Guide.md`
- **部署步驟**: 查看 `DEPLOYMENT.md`
- **檢查清單**: 查看 `CHECKLIST.md`

### 常見問題

**Q: Git 推送時要求帳號密碼？**
- GitHub 現在使用 Personal Access Token
- 前往 Settings → Developer settings → Personal access tokens
- 生成新 token 並用它作為密碼

**Q: Streamlit Cloud 部署失敗？**
- 檢查 `requirements.txt` 是否在根目錄
- 確認倉庫是 Public
- 查看部署日誌找出錯誤

**Q: 應用無法正常運行？**
- 先在本地測試：`streamlit run app.py`
- 檢查所有套件是否已安裝
- 查看終端的錯誤訊息

---

## 🎯 下一步

部署完成後：

1. ✅ 測試所有功能
2. ✅ 分享您的 Demo URL
3. ✅ 在 GitHub 添加專案描述
4. ✅ 考慮添加截圖到 README

---

## 📚 專案檔案說明

| 檔案 | 用途 |
|------|------|
| `app.py` | 主程式 ⭐ |
| `requirements.txt` | 依賴套件 ⭐ |
| `README.md` | 專案說明 |
| `0_devLog.md` | 開發日誌 |
| `run_app.bat` | 快速啟動 |
| 其他 `.md` | 各種文件 |

---

## ✨ 專案特色

- 📊 完整的 CRISP-DM 方法論
- 🎛️ 可調整參數（斜率、截距、雜訊等）
- 📈 即時視覺化
- 🌐 一鍵部署到網路

---

**準備好了嗎？開始部署吧！** 🚀

有問題隨時查看詳細文件或在 GitHub 開 Issue。

**祝您部署順利！** 🎉
