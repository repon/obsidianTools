import os
import re
from datetime import datetime
import locale

# ロケールを日本語に設定
locale.setlocale(locale.LC_TIME, "ja_JP.UTF-8")

# ObsidianのVaultのディレクトリを指定
vault_path = "path/to/vault"


# 日付から曜日を取得する関数（日本語対応）
def add_weekday_to_date(date_str):
    try:
        # YYYY-MM-DD形式の日付をdatetimeオブジェクトに変換
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        # 曜日を(ddd)形式で日本語で取得
        weekday = date_obj.strftime("(%a)")
        # 日付と曜日を結合して返す
        return f"{date_str}{weekday}"
    except ValueError:
        # 日付フォーマットが不正な場合はそのまま返す
        return date_str


# ノート内のリンクを変更する関数
def update_links_in_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # [[YYYY-MM-DD]] のリンク形式を正規表現で探す
    updated_content = re.sub(
        r"\[\[(\d{4}-\d{2}-\d{2})\]\]",
        lambda m: f"[[{add_weekday_to_date(m.group(1))}]]",
        content,
    )

    # ファイルの内容が変更された場合に上書き保存
    if updated_content != content:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(updated_content)
        print(f"Updated links in: {file_path}")


# Vault内のすべてのMarkdownファイルを処理
def update_links_in_vault(vault_path):
    for root, dirs, files in os.walk(vault_path):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                update_links_in_file(file_path)


# メイン処理
if __name__ == "__main__":
    update_links_in_vault(vault_path)
