# Generate a PowerPoint presentation using your custom templates (Presenton API)

This tool generates a PowerPoint presentation using **your 4 custom templates**.  
The agent must prepare a JSON body exactly matching the Presenton API structure.

You MUST NOT output the JSON body directly.
You MUST call the MCP tool “generate_powerpoint” using the provided arguments.
Do not return the JSON itself. Pass it to the tool.

---

## 📌 Available Custom Templates (template_type)

1. **general** (일반)
   - 기본 소개 자료
   - 제목 + 본문 구조
   - 범용적인 PPT

2. **standard** (표준)
   - 공식 문서 스타일
   - 전문적인 레이아웃
   - 비즈니스 프레젠테이션

3. **modern** (모던)
   - 현대적 디자인
   - 시각적 강조
   - 창의적 프레젠테이션

4. **swift** (간결)
   - 간결한 구성
   - 핵심 내용 중심
   - 빠른 정보 전달

---

## 📌 Presenton API Parameter Mapping

You MUST use the template_type values **directly** in the Presenton `"template"` field:
- general
- standard
- modern
- swift

⚠ These are your custom templates stored inside Presenton.

---

## 📌 Required Output (JSON Only)

The agent MUST generate only a JSON body like this:

```json
{
  "content": "PPT 내용 또는 요약",
  "n_slides": 8,
  "language": "ko",
  "template": "general",   // ← template_type 기반
  "export_as": "pptx"
}
```

### 필수 규칙
- `"template"` 값은 **template_type 그대로 사용**  
- `"export_as"`는 항상 `"pptx"`  
- `"language"`는 `"ko"`  
- `"n_slides"`는 5~15 사이로 자동 조정  
- `"content"`에는 사용자의 요청 내용을 구조화하고 PPT의 내용을 구성할 수 있게 상세히 입력  
- Python 코드를 생성하지 않음  
- JSON 이외의 텍스트 절대 포함 금지  

---

## 🧠 Agent Instructions

- 유저의 요청을 분석해 content를 적절히 요약하여 작성
- template_type은 다음 중 하나를 사용: general, standard, modern, swift
- n_slides는 사용자 요청에 따라 5~15 사이로 조정
- content에는 PPT의 전체 내용과 구조를 상세히 작성  

---

## 🧩 Example

### 🔹 User input:
"AI 이용한 전북도 RAG 시스템 전체 설명 PPT 만들어줘 (일반 템플릿 사용)"

### 🔹 Tool call:

```
Tool: generate_powerpoint
Arguments:
{
  "content": "전북도 AI RAG 시스템의 개요, 구조, 처리 흐름, 활용 사례를 중심으로 설명합니다. 1) RAG 시스템 소개, 2) 전북도 적용 사례, 3) 시스템 아키텍처, 4) 주요 기능, 5) 처리 흐름, 6) 벡터DB 활용, 7) AI 모델 통합, 8) 향후 계획",
  "file_name": "jeonbuk_rag_system",
  "user_id": "user123",
  "template_type": "general"
}
```

---

IMPORTANT:
- You MUST call the MCP tool "generate_powerpoint" with the arguments
- DO NOT output JSON directly to the user
- The content parameter should contain detailed information for slide generation
- template_type must be one of: general, standard, modern, swift

---

This document defines the complete rules for generating PowerPoint presentations  
using **your own custom templates stored in Presenton**.
