---
theme: default
title: "Algorithms Lab — Week 1 – Coding Agents"
info: "Algorithms Lab"
class: text-center
drawings:
  persist: false
transition: slide-left
---

# Algorithms Lab

## Week 1 -- Coding Agents

Korea University Sejong Campus, Department of Computer Science & Software

---

# Lab Overview

- **Goal**: Install and use an AI-powered coding agent for real development tasks
- **Duration**: ~50 minutes
- **Submission**: None -- exploration lab
- These tools will be used **throughout the semester** for labs and assignments

<div style="display: flex; align-items: center; justify-content: center; gap: 8px; margin-top: 40px;">
  <div style="background: #dce6f7; border: 1px solid #b0c4de; border-radius: 8px; padding: 12px 16px; text-align: center; min-width: 120px;">
    <div style="font-weight: bold;">Task 1</div>
    <div style="font-size: 0.85em;">Install Agent</div>
  </div>
  <div style="font-size: 1.2em;">→</div>
  <div style="background: #dce6f7; border: 1px solid #b0c4de; border-radius: 8px; padding: 12px 16px; text-align: center; min-width: 120px;">
    <div style="font-weight: bold;">Task 2</div>
    <div style="font-size: 0.85em;">File Organization</div>
  </div>
  <div style="font-size: 1.2em;">→</div>
  <div style="background: #dce6f7; border: 1px solid #b0c4de; border-radius: 8px; padding: 12px 16px; text-align: center; min-width: 120px;">
    <div style="font-weight: bold;">Task 3</div>
    <div style="font-size: 0.85em;">Repo Documentation</div>
  </div>
  <div style="font-size: 1.2em;">→</div>
  <div style="background: #dce6f7; border: 1px solid #b0c4de; border-radius: 8px; padding: 12px 16px; text-align: center; min-width: 120px;">
    <div style="font-weight: bold;">Task 4</div>
    <div style="font-size: 0.85em;">RALPH Technique</div>
  </div>
  <div style="font-size: 1.2em;">→</div>
  <div style="background: #dce6f7; border: 1px solid #b0c4de; border-radius: 8px; padding: 12px 16px; text-align: center; min-width: 120px;">
    <div style="font-weight: bold;">Task 5</div>
    <div style="font-size: 0.85em;">Sorting Benchmark</div>
  </div>
</div>

---

# What Are Coding Agents?

AI-powered CLI tools that understand and generate code **in context**

<div style="display: flex; align-items: center; justify-content: center; gap: 12px; margin: 30px 0;">
  <div style="background: #e3f2fd; border: 2px solid #90caf9; border-radius: 8px; padding: 16px 20px; text-align: center;">
    <div style="font-weight: bold;">Read</div>
    <div style="font-size: 0.85em;">files & context</div>
  </div>
  <div style="font-size: 1.2em;">→</div>
  <div style="background: #fff8e1; border: 2px solid #ffe082; border-radius: 8px; padding: 16px 20px; text-align: center;">
    <div style="font-weight: bold;">Plan</div>
    <div style="font-size: 0.85em;">what to do</div>
  </div>
  <div style="font-size: 1.2em;">→</div>
  <div style="background: #e8f5e9; border: 2px solid #a5d6a7; border-radius: 8px; padding: 16px 20px; text-align: center;">
    <div style="font-weight: bold;">Act</div>
    <div style="font-size: 0.85em;">edit & run</div>
  </div>
  <div style="font-size: 1.2em;">→</div>
  <div style="background: #fce4ec; border: 2px solid #f48fb1; border-radius: 8px; padding: 16px 20px; text-align: center;">
    <div style="font-weight: bold;">Verify</div>
    <div style="font-size: 0.85em;">check results</div>
  </div>
</div>

<div style="text-align: center; font-style: italic; margin-bottom: 20px;">← iterate →</div>

- Can read your file system, run commands, and make edits autonomously
- Useful for: scaffolding, refactoring, documentation, debugging

> **Example**: *"Create a Python sorting benchmark with timing utilities"* Agent: reads directory → writes files → confirms tests pass

---

# Available Agents

<div style="display: flex; justify-content: center; gap: 80px; margin: 40px 0 20px;">
  <div style="text-align: center;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/8/8f/Google-gemini-icon.svg" alt="Gemini" width="56" style="margin-bottom: 8px;" />
    <div style="font-weight: bold; font-size: 1.1em;">Gemini CLI</div>
    <div style="color: #2e7d32; font-size: 0.9em;">Free (1000 calls/day)</div>
    <div style="font-size: 0.85em; color: #666;">Google's agent</div>
    <div style="font-size: 0.85em; color: #666;">Good default choice</div>
  </div>
  <div style="text-align: center;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/b/b0/Claude_AI_symbol.svg" alt="Claude" width="56" style="margin-bottom: 8px;" />
    <div style="font-weight: bold; font-size: 1.1em;">Claude Code</div>
    <div style="color: #e65100; font-size: 0.9em;">Paid</div>
    <div style="font-size: 0.85em; color: #666;">Anthropic's agent</div>
    <div style="font-size: 0.85em; color: #666;">Strong multi-file reasoning</div>
  </div>
  <div style="text-align: center;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/6/66/OpenAI_logo_2025_%28symbol%29.svg" alt="OpenAI" width="56" style="margin-bottom: 8px;" />
    <div style="font-weight: bold; font-size: 1.1em;">Codex CLI</div>
    <div style="color: #e65100; font-size: 0.9em;">Paid</div>
    <div style="font-size: 0.85em; color: #666;">OpenAI's agent</div>
    <div style="font-size: 0.85em; color: #666;">Open-source CLI</div>
  </div>
</div>

Also available: **OpenCode** (open-source harness -- use any model including open-source LLMs)

> *Recommendation*: Install **Gemini CLI** if you have no preference -- it's free and easy to set up.

---

# Task 1 -- Install a Coding Agent

Install at least one coding agent by following its official documentation.

**Installation commands:**

```bash
npm install -g @google/gemini-cli          # Gemini CLI (free)
npm install -g @anthropic-ai/claude-code    # Claude Code (paid)
```

**Verify installation:**

```bash
gemini --version    # or: claude --version
```

**What to check:**

- The CLI launches without errors
- You can authenticate (Google account for Gemini, Anthropic account for Claude)
- Try a simple prompt: `"What is 2 + 2?"` to confirm it responds

---

# Task 2 -- Organize Files

Use the agent to **organize files** in a messy directory.

**Example prompt:**

```
"Organize the files in ~/Downloads by file type into subfolders
 (images, documents, code, etc.). Show me the plan before executing."
```

**What to observe:**

- Does the agent **ask for confirmation** before moving files?
- Does it create a sensible folder structure?
- Does it handle edge cases (e.g., files with no extension)?

**Discussion:**

- What would happen if you didn't say *"show me the plan first"*?
- How do you give the agent more specific instructions if the result isn't right?

---

# Task 3 -- Document a GitHub Repo

Use the agent to **generate a README.md** for an existing codebase.

**Pick a target repository:**

- Your own project, or a public repo such as:
  - `https://github.com/code-yeongyu/oh-my-opencode`

**Example prompt:**

```
"Read this codebase and generate a comprehensive README.md
 with architecture overview, setup instructions, and usage examples."
```

**Evaluate the output:**

- Does the README **accurately** describe the project?
- Are the setup instructions correct and complete?
- Is anything missing (license, contributing guide, screenshots)?

> Save this README -- you'll improve it in the next task.

---

# Task 4 -- RALPH Technique

<div style="display: flex; align-items: center; gap: 24px;">
<div style="flex: 1;">

### What is RALPH Mode?

An **autonomous verification loop** where coding agents run continuously, self-validating outputs without human intervention.

<br>

**R**equest → **A**nalyze → **L**ist issues → **P**rompt again → **H**armonize

<br>

> The developer's role is shifting from **implementer** to **architect** — you design specs and validation systems, the agent codes.

</div>
<div style="flex-shrink: 0;">
  <img src="./images/openclaw-lobster.png" alt="OpenClaw Lobster" width="280" />
</div>
</div>

---

# RALPH Mode -- Real-World Impact

At Korea's first **Ralphton** hackathon, 13 elite teams let AI agents code **autonomously overnight** and reviewed results the next morning.

<div style="display: flex; justify-content: center; gap: 16px; margin: 24px 0;">
  <div style="background: #e8f5e9; border: 2px solid #a5d6a7; border-radius: 8px; padding: 16px 20px; text-align: center; min-width: 160px;">
    <div style="font-size: 1.8em; font-weight: bold;">100,000</div>
    <div style="font-size: 0.85em;">lines of code (winner)</div>
  </div>
  <div style="background: #fff8e1; border: 2px solid #ffe082; border-radius: 8px; padding: 16px 20px; text-align: center; min-width: 160px;">
    <div style="font-size: 1.8em; font-weight: bold;">70%</div>
    <div style="font-size: 0.85em;">was test code</div>
  </div>
  <div style="background: #e3f2fd; border: 2px solid #90caf9; border-radius: 8px; padding: 16px 20px; text-align: center; min-width: 160px;">
    <div style="font-size: 1.8em; font-weight: bold;">133</div>
    <div style="font-size: 0.85em;">Socratic reasoning iterations</div>
  </div>
</div>

### The Engineering Evolution

```
Prompt Engineering  →  Context Engineering  →  Harness Engineering
   (what to say)        (what to provide)       (how to verify)
```

> *Source: [Korean First Ralphton Review — Brian Jang](https://briandwjang.substack.com/p/8d3)*

---

# Task 4 -- RALPH in Practice

Create a **verifiable evaluation rubric** and use it to iteratively improve output quality.

**Example workflow using the README from Task 3:**

```
You:    "Generate a rubric for evaluating a high-quality open-source README."
Agent:  Returns 8 criteria (description, install, usage, architecture, ... )

You:    "Now evaluate the README you wrote against this rubric. Score each criterion."
Agent:  Scores 6/8 — missing: architecture diagram, contributing guide.

You:    "Fix all failing criteria. Add an architecture diagram and contributing guide."
Agent:  Updates the README with both additions.

You:    "Re-evaluate. Are all criteria met now?"
Agent:  8/8 — all criteria satisfied.
```

**Key phrases to try:**

- *"Keep going until the criteria are met"*
- *"Evaluate against the rubric and fix all issues"*

**Why this matters:**

- Agents produce *good-enough* output on first try, but **not perfect**
- The RALPH loop teaches you to **systematically improve** agent output
- This skill transfers to any AI tool, not just coding agents

---

# Task 5 -- Build a Sorting Benchmark

Use the agent to **build a multi-file sorting benchmark** -- a preview of the semester project.

**Example prompt:**

```
"Create a Python sorting benchmark that compares bubble sort, merge sort,
 and Python's built-in sort. Include timing utilities and a results table.
 Organize the code into separate modules."
```

**Expected output files:**

<div style="display: flex; align-items: center; justify-content: center; gap: 8px; margin-top: 30px;">
  <div style="background: #e3f2fd; border: 1px solid #90caf9; border-radius: 8px; padding: 12px 16px; text-align: center;">
    <div style="font-weight: bold;">sorting.py</div>
    <div style="font-size: 0.85em;">sort algorithms</div>
  </div>
  <div style="font-size: 1.2em;">→</div>
  <div style="background: #fff8e1; border: 1px solid #ffe082; border-radius: 8px; padding: 12px 16px; text-align: center;">
    <div style="font-weight: bold;">timer.py</div>
    <div style="font-size: 0.85em;">timing utility</div>
  </div>
  <div style="font-size: 1.2em;">→</div>
  <div style="background: #e8f5e9; border: 1px solid #a5d6a7; border-radius: 8px; padding: 12px 16px; text-align: center;">
    <div style="font-weight: bold;">benchmark.py</div>
    <div style="font-size: 0.85em;">main runner</div>
  </div>
  <div style="font-size: 1.2em;">→</div>
  <div style="background: #fce4ec; border: 1px solid #f48fb1; border-radius: 8px; padding: 12px 16px; text-align: center;">
    <div style="font-weight: bold;">README.md</div>
    <div style="font-size: 0.85em;">documentation</div>
  </div>
</div>

---

# Task 5 -- What to Observe

You do **not** need a perfect benchmark -- the **process** matters.

**Watch how the agent:**

- Breaks a complex problem into multiple files
- Explains each component's role
- Handles errors when you give feedback
- Iterates on build failures (if any)

**Try follow-up prompts:**

- *"Add a bar chart visualization of the results"*
- *"Explain the time complexity of each sorting algorithm"*
- *"The benchmark crashes with large N -- fix it"*

---

# Assignments & Team Project

### Weekly Assignments (Weeks 02--06)

- **Weeks 2--6**, you will receive weekly assignments
- Each assignment: build a **web application** that applies the algorithm learned that week
- Goal: experience how algorithms improve real software performance

### Team Project (Final Exam, Weeks 09--13)

- Teams of 3--4 will build a **web application** that incorporates **all algorithms** covered in the course
- Deliverables: **working web app** + **report** + **presentation**
- The agent will be your primary development tool throughout

<br>

> Make the most of coding agents -- they will be essential for both assignments and the final project.

---

# Summary & Next Steps

**What we practiced today:**

| Task | Skill Learned |
|------|---------------|
| 1. Install agent | Tool setup, authentication, basic prompting |
| 2. File organization | Delegating real tasks, reviewing agent decisions |
| 3. Repo documentation | Evaluating AI-generated technical writing |
| 4. RALPH technique | Systematic iterative refinement with rubrics |
| 5. Sorting benchmark | Tackling complex multi-file algorithm projects |

**Coming up -- Week 2 Lab**: Complexity Analysis Practice (O(n²) vs O(n) comparison)

> Coding agents are tools -- understanding what they produce is still **your** responsibility.
