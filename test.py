import openai

# 設定API金鑰
openai.api_key = "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"

try:
    # 使用新的ChatCompletion接口進行測試
    response = openai.ChatCompletion.create(
        model="gpt-4-o-mini",  # 或者使用 "gpt-4" 如果你的帳戶有權限
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "你好嗎？"}
        ]
    )
    print("API回應內容：", response.choices[0].message['content'].strip())
    print("API測試成功！")
except Exception as e:
    print("API測試失敗，錯誤訊息：", e)
