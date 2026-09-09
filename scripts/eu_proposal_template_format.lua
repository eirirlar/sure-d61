--[[
  Pandoc Lua filter: reformat EU proposal-template documents (EIC Transition,
  Horizon Europe application forms) that Pandoc has converted from .docx.

  The Word templates put every guidance note, every answer and every work
  package description inside a table. Pandoc renders those either as huge ASCII
  grid tables or, for GFM output, as raw HTML. Both are unreadable as Markdown.

  This filter:
    * 1-column tables       -> header row becomes a blockquote, body becomes text
    * label/value tables    -> "**Label:** value" lines, or a bold label followed
                               by the block content when the value is long
    * simple data tables    -> left alone, so they stay real Markdown tables
    * numbered bold headings -> real Markdown headings (bold markup removed)
    * all-guidance bullet lists -> blockquotes
    * [text]{.mark}         -> plain text
    * [text]{.underline}    -> italics

  Usage:
    pandoc IN.md -f markdown -t gfm --wrap=none \
      --lua-filter=scripts/eu_proposal_template_format.lua -o OUT.md
--]]

local stringify = pandoc.utils.stringify

-- true if the inline list is a single Span carrying the given class
local function lone_span_with_class(inlines, class)
  if #inlines ~= 1 then return nil end
  local el = inlines[1]
  if el.t ~= "Span" then return nil end
  for _, c in ipairs(el.classes) do
    if c == class then return el end
  end
  return nil
end

-- a cell Pandoc can put in a pipe table: at most one paragraph, no lists
local function cell_is_simple(cell)
  local bs = cell.contents
  if #bs == 0 then return true end
  if #bs > 1 then return false end
  local t = bs[1].t
  return t == "Plain" or t == "Para"
end

local function cell_is_empty(cell)
  return stringify(cell.contents):match("^%s*$") ~= nil
end

-- drop an outer Strong/Emph wrapper so labels are not bolded twice
local function unwrap_label(inlines)
  while #inlines == 1 and (inlines[1].t == "Strong" or inlines[1].t == "Emph") do
    inlines = inlines[1].content
  end
  return inlines
end

-- the inlines of a one-paragraph cell, or nil
local function cell_inlines(cell)
  local bs = cell.contents
  if #bs ~= 1 then return nil end
  if bs[1].t ~= "Plain" and bs[1].t ~= "Para" then return nil end
  return bs[1].content
end

local function all_rows(tbl)
  local rows = pandoc.List()
  for _, r in ipairs(tbl.head.rows) do rows:insert({ row = r, head = true }) end
  for _, body in ipairs(tbl.bodies) do
    for _, r in ipairs(body.body) do rows:insert({ row = r, head = false }) end
  end
  for _, r in ipairs(tbl.foot.rows) do rows:insert({ row = r, head = false }) end
  return rows
end

-- one column: guidance box on top, answer underneath
local function flatten_single_column(rows)
  local out = pandoc.List()
  for _, entry in ipairs(rows) do
    local blocks = pandoc.List()
    for _, cell in ipairs(entry.row.cells) do
      for _, b in ipairs(cell.contents) do blocks:insert(b) end
    end
    if #blocks > 0 then
      if entry.head then
        out:insert(pandoc.BlockQuote(blocks))
      else
        for _, b in ipairs(blocks) do out:insert(b) end
      end
    end
  end
  return out
end

-- two or more columns: render each row as a labelled block
local function flatten_label_value(rows)
  local out = pandoc.List()
  for _, entry in ipairs(rows) do
    local cells = pandoc.List()
    for _, c in ipairs(entry.row.cells) do
      if not cell_is_empty(c) then cells:insert(c) end
    end

    if #cells == 1 then
      -- a merged or single-content row: emit it as ordinary body text
      for _, b in ipairs(cells[1].contents) do out:insert(b) end
    elseif #cells >= 2 then
      local label = cell_inlines(cells[1])
      if label then label = unwrap_label(label) end
      local value = cell_inlines(cells[2])
      if label and value and #cells == 2 then
        local line = pandoc.List()
        line:insert(pandoc.Strong(label))
        line:insert(pandoc.Str(":"))
        line:insert(pandoc.Space())
        for _, i in ipairs(value) do line:insert(i) end
        out:insert(pandoc.Para(line))
      else
        if label then
          out:insert(pandoc.Para({ pandoc.Strong(label) }))
        else
          for _, b in ipairs(cells[1].contents) do out:insert(b) end
        end
        for i = 2, #cells do
          for _, b in ipairs(cells[i].contents) do out:insert(b) end
        end
      end
    end
  end
  return out
end

-- 0. Word underlining has no Markdown equivalent. Render it as bold: bold
-- nests correctly inside the italics the templates use for guidance text,
-- whereas italics inside italics produces broken markup.
function Underline(el)
  return pandoc.Strong(el.content)
end

-- 0b. Bold inside bold cannot be written in Markdown; collapse it
function Strong(el)
  if #el.content == 1 and el.content[1].t == "Strong" then
    return el.content[1]
  end
  return nil
end

-- 1. Spans: drop .mark, italicise .underline, unwrap the rest
function Span(el)
  for _, c in ipairs(el.classes) do
    if c == "underline" then return pandoc.Strong(el.content) end
  end
  return el.content
end

-- 2. Tables that are really layout boxes become headings, quotes and text
function Table(tbl)
  local rows = all_rows(tbl)
  if #rows == 0 then return nil end

  if #tbl.colspecs <= 1 then
    return flatten_single_column(rows)
  end

  -- keep genuine data tables: every cell fits in a pipe-table cell
  local simple = true
  for _, entry in ipairs(rows) do
    for _, cell in ipairs(entry.row.cells) do
      if not cell_is_simple(cell) then simple = false break end
    end
    if not simple then break end
  end
  if simple then return nil end

  return flatten_label_value(rows)
end

-- 3. Numbered bold template headings become real headings
function OrderedList(el)
  if #el.content ~= 1 then return nil end
  local item = el.content[1]
  local first = item[1]
  if first == nil then return nil end
  if first.t ~= "Para" and first.t ~= "Plain" then return nil end
  if #first.content == 0 or first.content[1].t ~= "Strong" then return nil end
  if #stringify(first.content) > 120 then return nil end

  local out = pandoc.List()
  out:insert(pandoc.Header(2, first.content))
  for i = 2, #item do out:insert(item[i]) end
  return out
end

-- 4. Bullet lists that are only guidance text become a blockquote
function BulletList(el)
  local guidance = pandoc.List()
  for _, item in ipairs(el.content) do
    if #item ~= 1 then return nil end
    local b = item[1]
    if b == nil then return nil end
    if b.t ~= "Para" and b.t ~= "Plain" then return nil end
    local span = lone_span_with_class(b.content, "mark")
    if not span then return nil end
    guidance:insert(pandoc.Para(span.content))
  end
  if #guidance == 0 then return nil end
  return pandoc.BlockQuote(guidance)
end

-- 5. A paragraph that is only a task title becomes a level-3 heading
function TaskHeading(el)
  local text = stringify(el.content)
  if not text:match("^Task%s+%d+%.%d+") then return nil end
  if #text > 200 then return nil end
  text = text:gsub("%s*:%s*$", "")
  return pandoc.Header(3, text)
end

-- 6. Headings carry no bold or italic markup of their own
function Header(el)
  return pandoc.Header(el.level, pandoc.utils.blocks_to_inlines(
    { pandoc.Plain(stringify(el.content)) }), el.attr)
end

-- Span runs last so the block rules can still see the class information
return {
  { BulletList = BulletList },
  { Table = Table, OrderedList = OrderedList },
  { Header = Header },
  { Span = Span, Underline = Underline },
  { Strong = Strong },
  { Para = TaskHeading },
}
