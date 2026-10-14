# Weekly Parenting Guide

A reusable AI skill for parents and caregivers of children aged 0–71 months in South Korea. It turns age, recent observations and everyday concerns into up to three practical actions for the coming week.

Public draft v1.0.0 · Korean by default · Claude and ChatGPT guidance

[Download Weekly Parenting Guide (.skill)](https://raw.githubusercontent.com/Jeongin-Choe-RN/weekly-childcare/main/dist/weekly-childcare.skill) · [View SKILL.md](SKILL.md) · [한국어](README.md)

## 1. What it does

It covers relationships, communication and play, movement, sleep and meals, oral care and toileting, childcare adjustment, discipline, safety, health-check reminders and caregiver workload. It does not turn every domain into weekly homework or score the child or parent.

The five steps are: understand the child → review observations → choose priorities → try everyday actions → record and continue. The first week skips the review step.

## 2. Claude

Download the `.skill` file above; it bundles the instructions and supporting materials. You do not need to extract it. Enable code execution and file creation, then open Customize → Skills → + → Create skill → Upload a skill. If the file picker accepts `.skill`, upload the file and enable it. Supported file types and menus may vary by account or version; if the file cannot be selected, check the official installation instructions below.

Example: "Use weekly-childcare. My child is 22 months old, attends childcare, and I have about 10 minutes on weekdays. I would like help responding when toys are thrown."

See [Claude's official instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude). Archive structure has been checked; installation and behavior in a particular Claude account still need to be confirmed.

## 3. ChatGPT

Where personal skills are supported, provide SKILL.md and its supporting folders and ask ChatGPT to create a personal skill. A Claude `.skill` archive is not a universal ChatGPT installer. For an ordinary chat, attach or paste [the starter instructions](docs/CHATGPT_START.md), which are in Korean, and ask for your preferred response language. This is a prompt-based route, not installation.

See [ChatGPT skills](https://learn.chatgpt.com/docs/skills-and-plugins).

## 4. Records, privacy and limitations

Use the blank [profile](templates/profile.md) and [weekly log](templates/weekly-log.md) privately. A short reply can include: a new observation / the hardest situation / available time next week. Bring the recent record to a new chat; cross-chat or cross-service memory is not guaranteed.

No real child's information is bundled as a default. Do not upload personal records, photographs or medical information to the public repository or its Issues. The age script has no network calls or external storage; the AI service's own data policies still apply.

This is parenting support, not a diagnostic test, treatment, K-DST replacement or a clinically validated program. Consult a clinician about lost skills or persistent developmental concerns. Follow individual clinical advice. Sources and their verification date are in [evidence.md](references/evidence.md); unavailable live verification must be disclosed.

Installing the skill does not create reminders. Scheduling requires a separate supported feature and a successful scheduling result. Download and apply updated releases when needed; a repository edit does not automatically update every installed copy.

## 5. Use and author

The skill instructions, documentation, blank templates and examples are shared under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Parents and caregivers may use, adapt and share copies for noncommercial purposes, with attribution, a license link and an indication of changes. Commercial use, including sale, requires separate permission from the author.

Original repository: <https://github.com/Jeongin-Choe-RN/weekly-childcare>. Permission to modify a downloaded copy does not grant write access to this repository.

Python scripts use [PolyForm Noncommercial 1.0.0](LICENSES/PolyForm-Noncommercial-1.0.0.txt). See [LICENSE.md](LICENSE.md) for file-level scope and copyright notices. The `.skill` file includes these notices and license texts. Third-party source materials retain their own rights and are not relicensed by this repository.

Author: Jeongin Choe (최정인). Developed with assistance from ChatGPT (OpenAI). This is not an official or endorsed product of any university, hospital, professional society or cited organization.
