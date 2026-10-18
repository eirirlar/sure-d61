# Git and gh are never allowed without explicit permission in the current conversation

Never run `git`, `gh` or other commands that invoke git. This includes:

- Scripts that call git internally.
- Compound Bash commands where git appears anywhere — `pwd && git ...` is just as forbidden as plain `git ...`.
- Read-only commands: `git status`, `git diff`, `git log`, `git branch`, `git show`, `git ls-files`, `git rev-parse`, `git worktree list`, `gh pr list`, `gh issue view`, etc.

Before every Bash command, explicitly check whether `git` or `gh` appears anywhere — if yes, stop and ask, even when you need info quickly.

If you need info that could have come from git: use Read / Glob / Grep, or ask the user to paste the output.
