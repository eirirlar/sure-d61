# Batch in-place edits require dry-run + backups

When writing a script that transforms many files with regex/pattern replacement, the default must be a non-destructive mode (write to `<name>.cleaned.<ext>` sibling files, or a separate output folder). Only overwrite originals after a dry-run has printed per-file word-count / line-count deltas and a human has confirmed none of them are surprising.

Any single file that shrinks below ~70% of its original size is a red flag until inspected — an over-broad regex can silently truncate content.

Convention exists because of the T73 investor-update incident where two files silently lost ~90% of content to a signature-start regex that matched markdown horizontal rules.
