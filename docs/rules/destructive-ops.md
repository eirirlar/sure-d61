# `rm` and other destructive operations require explicit permission

For files not generated in the current conversation. Before every `rm`, `mv --force`, `> file` (overwrite) or equivalent: check whether the file is something generated in this session. If not — stop and ask.

## Signals the file belongs to the user (and must not be touched)

- File size or mtime that differs from your own output.
- Filename that does not match your pipeline.
- Files that "seem odd to have" in the folder.

Deleting is worse than letting it be — ask instead.
