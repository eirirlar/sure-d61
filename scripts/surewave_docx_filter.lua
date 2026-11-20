-- Pandoc Lua filter used by scripts/md_to_surewave_docx.py.
--
-- Both behaviours are opt-in through document metadata, which the wrapper
-- passes with -M from the deliverable's .meta.yaml:
--
--   number_figures: true          prefix every figure caption with "Figure N: "
--                                 (pandoc's docx writer does not number captions)
--   strip_horizontal_rules: true  drop markdown `---` rules from the docx body
--                                 (they stay in the LaTeX/PDF build)

local number_figures = false
local strip_rules = false
local n = 0

local function truthy(v)
  if v == nil then return false end
  if type(v) == "boolean" then return v end
  return pandoc.utils.stringify(v) == "true"
end

local function Meta(m)
  number_figures = truthy(m.number_figures)
  strip_rules = truthy(m.strip_horizontal_rules)
end

local function Figure(f)
  if not number_figures then return nil end
  n = n + 1
  local blk = f.caption.long[1]
  if blk and blk.content then
    blk.content:insert(1, pandoc.Space())
    blk.content:insert(1, pandoc.Str("Figure " .. n .. ":"))
  end
  return f
end

local function HorizontalRule()
  if strip_rules then return {} end
  return nil
end

return {
  { Meta = Meta },
  { Figure = Figure, HorizontalRule = HorizontalRule },
}
