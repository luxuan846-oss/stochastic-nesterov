function Table(t)
  local widths
  if #t.colspecs == 3 then
    local h=pandoc.utils.stringify(t.head)
    if h:match('年份') then widths={0.12,0.36,0.52}
    else widths={0.24,0.28,0.48} end
  elseif #t.colspecs == 4 then widths={0.22,0.21,0.35,0.22}
  elseif #t.colspecs == 5 then widths={0.19,0.25,0.18,0.24,0.14}
  end
  if widths then
    for i=1,#t.colspecs do t.colspecs[i][2]=widths[i] end
  end
  return t
end
