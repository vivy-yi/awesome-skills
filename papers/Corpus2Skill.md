# Corpus2Skill: Navigable Agent Skills for QA and RAG

> **Paper**: [arXiv 2604.14572](https://arxiv.org/abs/2604.14572)  
> **Published**: 2026-04-16  
> **Authors**: Yiqun Sun, Pengfei Wei, Lawrence B. Hsieh

---

## Core Problem

Retrieval-Augmented Generation (RAG) treats the LLM as a **passive consumer** of search results. The agent never sees how the corpus is organized or what it has not yet retrieved — limiting its ability to backtrack or combine scattered evidence.

## Corpus2Skill Solution

Distills a document corpus into a **hierarchical skill directory** offline, then lets the LLM agent **navigate it at serve time**.

### Compilation Pipeline (Offline)
1. Iteratively cluster documents
2. Generate LLM-written summaries at each level
3. Materialize as a **tree of navigable skill files**

### Serve Time (Online)
- Agent receives a **bird's-eye view** of the corpus
- Drills into topic branches via **progressively finer summaries**
- Retrieves full documents by ID
- Can **reason about where to look**, backtrack from unproductive paths, and **combine evidence across branches**

## Key Insight

> Instead of retrieving, **navigate**.

Traditional RAG: retrieval → passive consumption  
Corpus2Skill: hierarchical skill tree → active navigation

## Results

On **WixQA** (enterprise customer-support benchmark):
- Outperforms dense retrieval, RAPTOR, and agentic RAG baselines
- Across all quality metrics

## Relevance to Agent Skills

- Introduces **"Skill" as a navigable unit** of knowledge (skill files)
- Shows how to structure domain knowledge as **Agent-Navigable Skills** (not just human-readable docs)
- Could be applied to any domain: enterprise knowledge bases → navigable agent skill trees

## Tags

`navigable-skills` `rag` `knowledge-management` `corpus2skill` `enterprise`
