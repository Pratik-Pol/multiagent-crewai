# AI Multi-Agent Content Generator

A Flask-based web application that generates structured content using a multi-agent AI workflow.
The project simulates how different AI stages can collaborate to research, write, and review content before generating a final output.

## Overview

This project was created to explore how AI workflows can be divided into smaller task-specific stages instead of relying on a single prompt.
The application processes user input through multiple AI stages:
- Research
- Writing
- Review
This helps produce cleaner and more structured content.

---

## Workflow

```text
User Input
   ↓
Research Agent
   ↓
Writing Agent
   ↓
Review Agent
   ↓
Final Output
