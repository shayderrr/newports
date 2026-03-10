function onCreate()
setProperty('boyfriend.alpha', 0);
setProperty('gf.alpha', 0);
setProperty('dad.alpha', 0);
makeLuaSprite('blackbg', 'chapters/chapter2/images/background/std/blackbg', -400, -500)
scaleObject('blackbg', 1.5, 1.5)
addLuaSprite('blackbg', false)
makeLuaSprite('spotlight', 'chapters/chapter2/images/background/std/light', 0, -500)
setProperty('spotlight.alpha', 0);
addLuaSprite('spotlight', true)
end

function onCreatePost()
if isStoryMode then
makeLuaSprite('directions', 'chapters/chapter2/images/background/std/directions', 0, 50)
setObjectCamera('directions', 'hud')
addLuaSprite('directions', true)
setProperty('directions.alpha', 0);
end
end

function onSongStart()
if isStoryMode then
doTweenAlpha('directionsalpha', 'directions', 1, 4, expoOut)
end
end

function onTweenCompleted(tag)
if tag == 'directionsalpha' then
runTimer('ff', 10)
end
end

function onUpdatePost()

if curStep == 45 then
doTweenAlpha('dadlighttween', 'dad', 0.7, 2)
doTweenAlpha('lightlighttween', 'spotlight', 0.3, 2)
end

if curStep == 65 then
doTweenAlpha('boyfriendlighttween', 'boyfriend', 0.7, 2)
end

if curStep ==  362 then
doTweenAlpha('gflighttween', 'gf', 1, 2)
doTweenAlpha('boyfriendlighttween', 'boyfriend', 1, 2)
doTweenAlpha('dadlighttween', 'dad', 1, 2)
doTweenAlpha('blacklighttween', 'blackbg', 0, 2)
doTweenAlpha('lightlighttween', 'spotlight', 0, 2)
end

end

function onTimerCompleted(tag)
if tag == 'ff' then
doTweenAlpha('directionsalpha', 'directions', 0, 1, quadInOut)
end
end