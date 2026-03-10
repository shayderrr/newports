function onCreate()
if isStoryMode then
makeLuaSprite('directions', 'chapters/chapter2/images/background/riverway/directions', 3200, 460)
setObjectCamera('directions', 'hud')
addLuaSprite('directions', true)
end
end

function onStartCountdown()
doTweenX('movedirections', 'directions', 200, 1, quadInOut)
end

function onSongStart()
setProperty('spaceriver', true)
if isStoryMode then
doTweenX('directionsmoveaway', 'directions', -1500, 1, quadInOut)
end
end

function onTweenCompleted(tag)
if tag == 'directionsmoveaway' then
removeLuaSprite('directions', true)
end
end

function onUpdate()
if getProperty('dad.animation.curAnim.name') == 'singLEFT' and getProperty('shouldsendanother') == true then
	setProperty('riverobject', true)
end
end