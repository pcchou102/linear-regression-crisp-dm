# 快速 GitHub 推送指南

## ⚠️ 您的系統尚未安裝 Git

請選擇以下其中一種方式：

---

## 🚀 方法 1: 安裝 Git（推薦）

### 步驟 1: 下載並安裝 Git
1. 前往 https://git-scm.com/download/win
2. 下載「64-bit Git for Windows Setup」
3. 執行安裝程式（全部使用預設設定即可）

### 步驟 2: 重新開啟 PowerShell，執行以下命令

```powershell
# 進入專案目錄
cd "c:\Users\周\Desktop\AIOT\HW1"

# 設定 Git 使用者資訊（第一次使用時需要）
git config --global user.name "您的名字"
git config --global user.email "your.email@example.com"

# 初始化倉庫
git init

# 添加所有檔案
git add .

# 提交
git commit -m "Initial commit: Simple Linear Regression with CRISP-DM"

# 連接到 GitHub（使用您提供的倉庫）
git remote add origin https://github.com/pcchou102/linear-regression-crisp-dm.git

# 設定主分支
git branch -M main

# 推送到 GitHub
git push -u origin main
```

### 步驟 3: 輸入 GitHub 認證
- **使用者名稱**: pcchou102
- **密碼**: 使用 Personal Access Token（不是密碼）

#### 如何獲取 Personal Access Token:
1. 登入 GitHub
2. 右上角頭像 → Settings
3. 左側最下方 → Developer settings
4. Personal access tokens → Tokens (classic)
5. Generate new token (classic)
6. 勾選 `repo` 範圍
7. 生成並**複製 Token**（只會顯示一次！）

---

## 💻 方法 2: 使用 GitHub Desktop（最簡單）

### 步驟 1: 安裝 GitHub Desktop
- 下載: https://desktop.github.com/
- 安裝並使用 GitHub 帳號登入

### 步驟 2: 發布專案
1. File → Add Local Repository
2. 選擇路徑: `c:\Users\周\Desktop\AIOT\HW1`
3. 點擊「Create a repository」（如果提示）
4. 點擊「Publish repository」
5. 設定:
   - Name: `linear-regression-crisp-dm`
   - 取消勾選「Keep this code private」
6. 點擊「Publish Repository」

✅ 完成！

---

## 📤 方法 3: 網頁直接上傳

### 步驟 1: 前往 GitHub
https://github.com/new

### 步驟 2: 創建倉庫
- Repository name: `linear-regression-crisp-dm`
- Public
- **不要**勾選 Initialize
- Create repository

### 步驟 3: 上傳檔案
1. 點擊「uploading an existing file」
2. 拖曳以下檔案:
   - ✅ app.py
   - ✅ requirements.txt
   - ✅ README.md
   - ✅ Development.md
   - ✅ DEPLOYMENT.md
   - ✅ .gitignore
3. Commit message: `Initial commit`
4. 點擊「Commit changes」

---

## 🌐 部署到 Streamlit Cloud

推送完成後：

1. 前往 https://streamlit.io/cloud
2. 使用 GitHub 登入
3. 點擊「New app」
4. 選擇:
   - Repository: `pcchou102/linear-regression-crisp-dm`
   - Branch: `main`
   - Main file: `app.py`
5. 點擊「Deploy!」
6. 等待 2-5 分鐘

✅ 完成後您會獲得一個 URL，例如:
`https://linear-regression-crisp-dm.streamlit.app/`

---

## 📝 部署後更新 README

將獲得的 Streamlit URL 更新到 README.md 的 Live Demo 區塊。

---

## ❓ 需要協助？

如果您選擇了方法 1 並成功安裝 Git，請告訴我，我可以幫您執行推送命令！

如果遇到任何錯誤訊息，也請直接貼給我。
