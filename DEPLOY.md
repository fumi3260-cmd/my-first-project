# GitHub Pages デプロイ手順

## ファイル構成

```
portfolio-haishin/
├── index.html      ← メインページ（必須・このファイル名固定）
├── style.css       ← スタイルシート
├── script.js       ← JavaScript
├── IMG_5046.JPG    ← 実績画像
├── IMG_2662.jpeg   ← 実績画像
├── IMG_5043.JPG    ← 実績画像
└── DEPLOY.md       ← この手順書
```

---

## Step 1: GitHubリポジトリを作成

1. https://github.com を開いてログイン
2. 右上の「+」→「New repository」
3. 設定：
   - Repository name: `portfolio` （または好きな名前）
   - **Public** を選択（Pagesは無料プランではPublicのみ）
   - README は追加しない
4. 「Create repository」をクリック

---

## Step 2: ファイルをGitHubにアップロード

### 方法A: ブラウザ（git不要・簡単）

1. 作成したリポジトリのページを開く
2. 「uploading an existing file」のリンクをクリック
3. `index.html` `style.css` `script.js` と画像ファイル3枚を**まとめてドラッグ＆ドロップ**
4. 「Commit changes」ボタンをクリック

### 方法B: git コマンド（ターミナルが使える場合）

```bash
cd /Users/fumi/Desktop/portfolio-haishin

git init
git add index.html style.css script.js IMG_5046.JPG IMG_2662.jpeg IMG_5043.JPG
git commit -m "first commit"

git branch -M main
git remote add origin https://github.com/あなたのユーザー名/portfolio.git
git push -u origin main
```

---

## Step 3: GitHub Pages を有効化

1. リポジトリ上部の「Settings」タブをクリック
2. 左メニューの「Pages」をクリック
3. **Source** → 「Deploy from a branch」を選択
4. **Branch** → `main` / `/(root)` を選択
5. 「Save」をクリック

数分後、以下のURLでサイトが公開されます：

```
https://あなたのユーザー名.github.io/portfolio/
```

---

## Step 4: 公開確認チェックリスト

- [ ] URLにアクセスして表示される
- [ ] スマートフォンで確認（レスポンシブ）
- [ ] ナビのリンクが全セクションに飛ぶ
- [ ] お問い合わせフォームのバリデーションが動作する
- [ ] 画像が表示されている

---

## 更新方法

ファイルを修正したら、GitHubのリポジトリで対象ファイルを開き  
「鉛筆アイコン（Edit）」→ 内容を修正 →「Commit changes」で即反映されます。

git を使う場合：
```bash
git add .
git commit -m "update"
git push
```

---

## よくある問題

| 症状 | 原因 | 解決策 |
|------|------|--------|
| ページが真っ白 | `index.html` のファイル名が違う | ファイル名を `index.html` に統一 |
| 画像が表示されない | ファイル名の大文字小文字が違う | HTMLの `src` と実際のファイル名を一致させる |
| URLが404 | Pages設定が未完 | Settings → Pages → Branch を再確認 |
| 反映されない | キャッシュ | ブラウザで強制リロード（Cmd+Shift+R） |
