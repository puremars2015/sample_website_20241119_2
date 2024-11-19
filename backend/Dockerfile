# 使用 Python 基礎映像
FROM python:3.12-slim

# 設定工作目錄
WORKDIR /app

# 複製後端代碼和依賴檔案
COPY . .

# 安裝 Python 依賴
RUN pip install --no-cache-dir -r requirements.txt

# 啟動 Flask API
CMD ["python", "app.py"]
