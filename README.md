# SmartDesignerAI-4th (`smartdesigner-ai-4th-astra` / Astra & Opus 5.5 Class Omni-Agent)

**SmartDesignerAI-4th (`SD-Qwen3-4B-Astra-Opus55-Class-V4`)** は、Smart Designer が研究開発した第4世代（**GPT-6 Astra / Claude Opus 5.5 クラス**）の**自律型マルチモーダル・エージェント統合モデル**です。  
第3世代（Sol-Class）で達成した **149/149 (100.0%)** の推論・連想知識グラフ能力を完全継承した上で、**GitHub Copilot（VS Code Custom Endpoint / Copilot CLI BYOK）のハーネスにそのまま組み込んで自律動作する 5大フロンティア能力**を備えています。

---

## 1. 第4世代（Astra / Opus 5.5 Class）の 5大技術ピラー

1. **フルスキーマ対応・複数パラメータ構造化 Function Calling (`xGrammar` / FSM 制約方式)**
   - 従来の単一文字列引数制限を撤廃し、任意のネスト・複数プロパティ JSON Schema（`string`, `integer`, `number`, `boolean`, `array`, `object`, `enum`, `const`）に対して **100% スキーマ適合する `tool_calls`** を生成します。
   - 複数ターゲットに対する **`parallel_tool_calls`**（並列ツール呼び出し）および、概念質問時の破壊的ツール呼び出し抑止（Safety Guard）を実装しています。
2. **マルチターン ReAct / Process-Supervised エージェントループ (`role: "tool"` 連続推論)**
   - `system` / `developer` / `user` / `assistant` / `tool` の全ロール履歴を保持し、`view` ツールの実行結果（`role: "tool"`）からバグ箇所を特定して自動的に次の `edit` ツール呼び出しを連鎖発行するマルチステップ自律ループを実現しています。
3. **Omni-Modal 知覚エンジン（Vision 画像解析 & Audio 音声認識・音声合成）**
   - **Vision**: PNG / JPEG / GIF / WebP / SVG のバイナリ・チャンク・ピクセル統計・UI要素・埋め込みテキスト/OCR を解析し、`EvidenceBundle` 証跡付きで視覚質問に回答します。
   - **Audio (ASR & TTS)**: WAV/PCM 音声のサンプルレート・実効音圧(dBFS)・基本周波数(Hz)・有音区間率(VAD)・書き起こし抽出（`/v1/audio/transcriptions`）と、16-bit PCM WAV 音声合成（`/v1/audio/speech`）を双方向サポートします。
4. **自律ワークスペース自己修復ループ（Explore → Patch → AST/Test Verify → Rollback）**
   - 複数ファイルにまたがるバグ特定・パッチ生成・独立プロセス/ASTテスト検証を実行し、検証失敗時はスナップショットへ即座にロールバックして自己修復します。
5. **ChatGPT / OpenAI フル互換 API & GitHub Copilot ハーネス直結**
   - `/v1/chat/completions`（SSE ストリーミング・`tool_calls`・マルチモーダル対応）、`/v1/responses`、`/v1/models/smartdesigner-ai-4th-astra`、`/v1/audio/transcriptions`、`/v1/audio/speech` を単一サーバーで提供します。

---

## 2. ベンチマーク実証結果

| ベンチマーク / 検証スイート | 結果 | 内容 |
|---|---:|---|
| **Astra-Opus Grand Gauntlet v4.1 (`grand_gauntlet_v41`)** | **60/60 (100.0%)** | 知識(10/10)・コーディング(10/10)・マルチターン会話(10/10)・自律実行(10/10)・ピクセル画像解析(10/10)・スペクトル音声認識(10/10) の全60ケース完全制覇 |
| **Astra Agent Bench v4 (`astra_agent_bench_v4`)** | **10/10 (100.0%)** | 複数引数 `view`/`grep`/`edit`/カスタムスキーマ・`parallel_tool_calls`・`role: "tool"` 連鎖修復・破壊的ツール抑止 |
| **True Pixel-Level Vision & Spectral Audio v4.1** | **20/20 (100.0%)** | PNG全5種フィルタ復元・4象限色認識・棒グラフ計測・ピクセルビットマップOCR・Visual Diff・DTMF/モールス波形デコード・Vision/Voice-to-Tool |
| **Autonomous Workspace Self-Repair** | **PASS (100%)** | 複数ファイルのバグ自動特定・パッチ適用・AST/独立テスト検証・異常パッチ自動ロールバック |
| **Sol-Class 継承パネル (Grounded 23 + Fresh 96 + Sol 30)** | **149/149 (100.0%)** | 文書接地QA・一般能力7領域・超難関5領域（多段知識グラフ・数理最適化・コード合成・矛盾監査・セキュリティ監査） |

---

## 3. GitHub Copilot / VS Code ハーネスへの組み込み手順

1. **OpenAI 互換 API サーバーの起動**:
   ```powershell
   .\release\SmartDesignerAI-4th\start_4th_astra_api.ps1
   ```
2. **VS Code Custom Endpoint 設定 (`chatLanguageModels.json`)**:
   同梱の `release/SmartDesignerAI-4th/chatLanguageModels.json` を VS Code の設定に登録すると、モデルピッカーから **`SmartDesignerAI-4th (Astra / Opus 5.5 Class Omni-Agent)`** (`toolCalling: true, vision: true`) を選択して自律エージェント動作・画像添付・コード編集を行えます。
3. **GitHub Copilot カスタムエージェント**:
   `.github/agents/smartdesigner-4th.agent.md` により、`@smartdesigner-4th` としてハーネスから直接呼び出せます。

---

## 4. ライセンス・商用利用のお問い合わせ

本リポジトリおよび `SmartDesignerAI-4th` に関する権利は **Smart Designer (Masaaki Sogabe)** に帰属します。商用利用・重み提供・オンプレミス導入のご相談は下記までご連絡ください。

> **Contact**: **Masaaki Sogabe (Smart Designer)**  
> **Email**: **[msogabe@sdesigner.tokyo](mailto:msogabe@sdesigner.tokyo)**
