# GitHub 推送指令

請按照以下步驟將專案推送到 GitHub：

## 步驟 1: 在 GitHub 上創建新倉庫

1. 登入 [GitHub](https://github.com)
2. 點擊右上角的 `+` 號
3. 選擇 `New repository`
4. 輸入倉庫名稱（建議：`linear-regression-crisp-dm`）
5. 選擇 `Public`（公開才能用 Streamlit Cloud 免費部署）
6. **不要**勾選任何初始化選項
7. 點擊 `Create repository`

## 步驟 2: 在本地執行以下命令

打開 PowerShell，切換到專案目錄後執行：

```powershell
# 初始化 Git 倉庫
git init

# 添加所有檔案
git add .

# 提交
git commit -m "Initial commit: Linear Regression with CRISP-DM"

# 添加遠端倉庫（請替換成您的 GitHub 用戶名和倉庫名稱）
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# 推送到 GitHub
git branch -M main
git push -u origin main
```

## 步驟 3: 部署到 Streamlit Cloud

1. 前往 [Streamlit Cloud](https://streamlit.io/cloud)
2. 點擊 `Sign up` 或 `Sign in` (使用 GitHub 帳號)
3. 點擊 `New app`
4. 設定以下參數：
   - Repository: `YOUR_USERNAME/YOUR_REPO_NAME`
   - Branch: `main`
   - Main file path: `app.py`
5. 點擊 `Deploy!`
6. 等待 2-5 分鐘完成部署
7. 複製部署後的 URL 並更新 README.md

## 步驟 4: 更新 README.md 中的連結

將 README.md 中的 `https://your-app.streamlit.app/` 替換為實際的部署 URL。

然後執行：

```powershell
git add README.md
git commit -m "Update demo site URL"
git push
```

---

## 常用 Git 命令

```powershell
# 查看狀態
git status

# 查看變更
git diff

# 添加檔案
git add <filename>
git add .  # 添加所有變更

# 提交
git commit -m "Your commit message"

# 推送
git push

# 拉取
git pull

# 查看歷史
git log --oneline
```

---

## 疑難排解

### Q: 如果已經有 .git 資料夾怎麼辦？

```powershell
# 刪除現有的 Git 倉庫
Remove-Item -Recurse -Force .git

# 重新初始化
git init
```

### Q: 推送時要求輸入帳號密碼？

GitHub 現在使用 Personal Access Token (PAT)，請：

1. 前往 GitHub Settings > Developer settings > Personal access tokens
2. 生成新的 token
3. 使用 token 作為密碼

或者使用 SSH：

```powershell
# 使用 SSH URL
git remote set-url origin git@github.com:YOUR_USERNAME/YOUR_REPO_NAME.git
```

### Q: 檔案太大無法推送？

確保 `.gitignore` 正確設定，排除了：
- `venv/` 或 `env/`
- `__pycache__/`
- `*.pyc`

---

祝您部署順利！🚀
