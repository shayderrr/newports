local pencilsup = true
local pencilsmovement = true

function onUpdate()
if pencilsup == true and pencilsmovement == true and getProperty('startdrawing') == false then
pencilsmovement = false
doTweenY('floatup', 'dad', 450, 2, quadInOut)
end

if pencilsup == false and pencilsmovement == true and getProperty('startdrawing') == false then
pencilsmovement = false
doTweenY('downfloat', 'dad', 150, 2, quadInOut)
end


if dadName == 'colors' and getProperty('startdrawing') == false then
            triggerEvent('Camera Follow Pos','','')
end


end

function onTweenCompleted(tag)
if tag == 'floatup' then
pencilsup = false
pencilsmovement = true
end

if tag == 'downfloat' then
pencilsup = true
pencilsmovement = true
end
end