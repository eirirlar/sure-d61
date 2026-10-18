# Agent tool always creates worktrees — plan for cleanup

The `Agent` tool in Claude Code (this harness version) creates a worktree per spawn regardless, even without `isolation: "worktree"` set explicitly. This also applies to agents that only read files.

For tasks that invoke the `Agent` tool, always check at the end that `.claude/worktrees/agent-*` folders have been cleaned up. Document in the task solution note that cleanup was done.

## Cleanup sequence

After the session ends and the pid is dead, worktrees can be cleaned with:

```
git worktree repair
git worktree unlock
git worktree remove --force
git branch -D
git worktree prune
```

For Cygwin/Windows mismatch: run cleanup in Git Bash, not Cygwin.
