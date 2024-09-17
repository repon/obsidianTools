#!/bin/bash
# ファイルが保存されているディレクトリへ移動
cd path/to/vault

# 日付に対応する曜日を追加してファイル名を変更
for file in *.md; do
    if [[ $file =~ ^([0-9]{4}-[0-9]{2}-[0-9]{2})\.md$ ]]; then
        date=${BASH_REMATCH[1]}
        day_of_week=$(date -jf "%Y-%m-%d" "$date" +"(%a)")
        mv "$file" "${date}${day_of_week}.md"
    fi
done