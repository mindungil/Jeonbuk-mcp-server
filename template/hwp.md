Generate a HWP document using the HWPX Report Generator API

This tool generates a Hangul HWP document using your administrative templates.
The agent must prepare a JSON body exactly matching the HWPX Report Generator API structure.

You MUST NOT output the JSON body directly.
You MUST call the MCP tool “generate_hwp” using the provided arguments.
Do not return the JSON itself. Pass it to the tool.

📌 Available Template Options (template_type)

default

기본 도청 행정 문서 양식

표준 공문 / 일반 보고 양식에 적합

v2

최신 도청 서식 스타일

구조화된 레이아웃 / 시각적 개선

📌 HWPX Report Generator Parameter Mapping

You MUST use the template_type values directly in the request:

default

v2

⚠ These are stored server-side templates.

📌 Required JSON Structure (body for the API)
{
  "content": "문서 본문 전체 내용",
  "file_name": "파일명(확장자 제외)",
  "template_type": "default",
  "language": "ko"
}

필수 규칙

"language" must always be "ko"

"template_type" must be exactly "default" or "v2"

"content" must include the full body text for the document with section structure

No HTML / No Markdown inside content

🧠 Agent Instructions

User request → structured administrative document

Include title, purpose, main body, bullet points if needed

Follow standard 행정 문서 톤

Avoid code blocks, emojis, Markdown formatting inside content

Do NOT output JSON visibly

MUST call:

Tool: generate_hwp
Arguments: { ... }

🧩 Example
🔹 User Input:

“전북도청 AI 문서배부 시스템 기술보고서 만들어줘 (기본 템플릿)”

🔹 Tool Call:
Tool: generate_hwp
Arguments:
{
  "content": "1. 개요\n본 문서는 전북도청 AI 문서배부 시스템의 구축 현황을 기술한다...\n2. 시스템 구성\n- OCR 처리 흐름\n- RAG 기반 분류 방식...\n3. 향후 계획\n...",
  "file_name": "ai_document_dispatch",
  "template_type": "default",
  "language": "ko"
}


IMPORTANT:

You MUST call the MCP tool "generate_hwp" with the arguments

DO NOT output the JSON directly to the user

Template type must be one of: default, v2

Document text must be fully contained in "content" field

This document defines the complete rules
for generating government-grade HWP documents using your HWPX Report Generator.
