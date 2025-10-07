# 🚀 部署指南

## 一、推送到 GitHub

### 步驟 1: 初始化 Git 倉庫

在專案目錄中打開終端機（PowerShell），執行以下命令：

```powershell
cd "c:\Users\周\Desktop\AIOT\HW1"
git init
git add .
git commit -m "Initial commit: Simple Linear Regression with CRISP-DM"
```

### 步驟 2: 在 GitHub 上創建新倉庫

1. 登入 [GitHub](https://github.com)
2. 點擊右上角的 `+` 號，選擇 `New repository`
3. 輸入倉庫名稱（例如：`linear-regression-crisp-dm`）
4. 選擇 `Public`（公開倉庫才能免費使用 Streamlit Cloud）
5. **不要**勾選 "Initialize this repository with a README"
6. 點擊 `Create repository`

### 步驟 3: 將本地倉庫推送到 GitHub

在 GitHub 創建倉庫後，複製顯示的 URL，然後執行：

```powershell
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

> 將 `YOUR_USERNAME` 和 `YOUR_REPO_NAME` 替換為您的 GitHub 用戶名和倉庫名稱。

---

## 二、部署到 Streamlit Cloud

### 步驟 1: 註冊 Streamlit Cloud

1. 前往 [Streamlit Cloud](https://streamlit.io/cloud)
2. 點擊 `Sign up` 或 `Get started`
3. 使用您的 GitHub 帳號登入

### 步驟 2: 部署應用程式

1. 登入後，點擊 `New app`
2. 選擇您的 GitHub 倉庫
3. 設定以下參數：
   - **Repository**: 選擇您剛才創建的倉庫
   - **Branch**: `main`
   - **Main file path**: `app.py`
4. 點擊 `Deploy!`

### 步驟 3: 等待部署完成

- 部署通常需要 2-5 分鐘
- 您會看到即時的部署日誌
- 完成後，您會獲得一個公開的 URL（例如：`https://your-app.streamlit.app`）

---

## 三、驗證部署

部署完成後，請測試以下功能：

- [ ] 應用程式可以正常載入
- [ ] 側邊欄的滑桿可以調整參數
- [ ] 圖表會根據參數變化即時更新
- [ ] 所有六個 CRISP-DM 標籤都能正常顯示
- [ ] 評估指標正確計算並顯示

---

## 四、更新應用程式

當您需要更新程式碼時：

```powershell
# 在本地進行修改後
git add .
git commit -m "描述您的修改"
git push origin main
```

Streamlit Cloud 會自動檢測到變更並重新部署。

---

## 五、常見問題

### Q1: 部署失敗，顯示 "requirements.txt not found"

**解決方案**：確保 `requirements.txt` 在倉庫的根目錄中。

### Q2: 應用程式運行但圖表不顯示

**解決方案**：檢查 Streamlit 版本是否正確安裝，嘗試在 `requirements.txt` 中固定版本號。

### Q3: 記憶體不足錯誤

**解決方案**：
- 減少預設的資料點數量
- 在程式中使用 `plt.close()` 關閉不需要的圖表
- 考慮使用 `@st.cache_data` 快取資料

### Q4: 應用程式載入很慢

**解決方案**：
- Streamlit Cloud 的免費方案在閒置後會休眠
- 第一次訪問時需要重新啟動，大約需要 30 秒
- 考慮升級到付費方案以保持應用程式持續運行

---

## 六、本地測試

在推送到 GitHub 之前，建議先在本地測試：

```powershell
# 安裝依賴
pip install -r requirements.txt

# 運行應用程式
streamlit run app.py
```

應用程式會在瀏覽器中自動開啟（通常是 http://localhost:8501）

---

## 七、進階設定

### 自訂域名

Streamlit Cloud 允許您設定自訂域名（需要付費方案）。

### 環境變數

如果需要設定環境變數，可以在 Streamlit Cloud 的應用程式設定中添加。

### 資源限制

免費方案的限制：
- 1 GB RAM
- 1 CPU
- 無限公開應用程式
- 社群支援

---

## 八、後續維護

### 監控應用程式

- 定期檢查應用程式是否正常運行
- 查看 Streamlit Cloud 的日誌以診斷問題
- 關注使用者回饋

### 更新套件

定期更新 `requirements.txt` 中的套件版本以修復安全漏洞和獲得新功能。

```powershell
pip list --outdated
pip install --upgrade streamlit numpy pandas matplotlib scikit-learn seaborn
pip freeze > requirements.txt
```

---

## 九、相關資源

- [Streamlit 文件](https://docs.streamlit.io/)
- [Streamlit Cloud 文件](https://docs.streamlit.io/streamlit-community-cloud)
- [GitHub 文件](https://docs.github.com/)
- [Git 基礎教學](https://git-scm.com/book/zh-tw/v2)

---

**祝您部署順利！🎉**

如有問題，請參考官方文件或在 GitHub Issues 中提問。
