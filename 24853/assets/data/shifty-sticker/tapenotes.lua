function onCreate()
	for i = 0, getProperty('unspawnNotes.length')-1 do
		if getPropertyFromGroup('unspawnNotes', i, 'noteType') == 'Tape Note' then
			setPropertyFromGroup('unspawnNotes', i, 'texture', 'testNOTES'); 
			if getPropertyFromGroup('unspawnNotes', i, 'mustPress') == true then
				setPropertyFromGroup('unspawnNotes', i, 'ignoreNote', true); 
			end
		end

	end


	

	makeAnimatedLuaSprite('tleft', 'tape', 0, 0)
	addAnimationByPrefix('tleft', 'peel', 'tape', 24, false)
	setProperty('tleft.alpha', 0)
	scaleObject('tleft', 0.6, 0.6)
	setObjectCamera('tleft', 'other')
	addLuaSprite('tleft')


	makeAnimatedLuaSprite('tdown', 'tape', 0, 0)
	addAnimationByPrefix('tdown', 'peel', 'tape', 24, false)
	setProperty('tdown.alpha', 0)
	addLuaSprite('tdown')
	scaleObject('tdown', 0.6, 0.6)
	setObjectCamera('tdown', 'other')


	makeAnimatedLuaSprite('tup', 'tape', 0, 0)
	addAnimationByPrefix('tup', 'peel', 'tape', 24, false)
	setProperty('tup.alpha', 0)
	addLuaSprite('tup')
	scaleObject('tup', 0.6, 0.6)
	setObjectCamera('tup', 'other')


	makeAnimatedLuaSprite('tright', 'tape', 0, 0)
	addAnimationByPrefix('tright', 'peel', 'tape', 24, false)
	setProperty('tright.alpha', 0)
	addLuaSprite('tright')
	scaleObject('tright', 0.6, 0.6)
	setObjectCamera('tright', 'other')

setProperty('tright.x', 1030)
setProperty('tup.x', 920)
setProperty('tdown.x', 810)
setProperty('tleft.x', 700)

if downscroll == false then

setProperty('tright.y', 35)
setProperty('tup.y', 35)
setProperty('tdown.y', 35)
setProperty('tleft.y', 35)

end


if downscroll == true then

setProperty('tright.y', 545)
setProperty('tup.y', 545)
setProperty('tdown.y', 545)
setProperty('tleft.y', 545)

end

	makeAnimatedLuaSprite('bubble', 'chapters/chapter4/seatower/speechbubble', -20, 220)
	addAnimationByPrefix('bubble', 'go', 'speechbubble idle', 12, false)
	setProperty('bubble.alpha', 0)
	scaleObject('bubble', 0.5, 0.5)
	setObjectCamera('bubble', 'hud')
	addLuaSprite('bubble')

	makeAnimatedLuaSprite('pieces', 'chapters/chapter4/seatower/piece', 0, 0)
	addAnimationByPrefix('pieces', 'go', 'piece idle', 12, false)
	setProperty('pieces.alpha', 0)
	scaleObject('pieces', 0.6, 0.6)
	setObjectCamera('pieces', 'hud')
	addLuaSprite('pieces')
end

function onCreatePost()
if isStoryMode then
makeLuaSprite('directions', 'chapters/chapter4/seatower/directions', -75, 175)
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

function goodNoteHit(id, noteData, noteType, isSustainNote)
	if noteType == 'Tape Note' then

		if noteData == 0 then
			setProperty('tapeleft', true)
			doTweenAlpha('tweenlefttape', 'tleft', 0.8, 0.1)
			objectPlayAnimation('tleft', 'peel')
		end

		if noteData == 1 then
			setProperty('tapedown', true)
			doTweenAlpha('tweendowntape', 'tdown', 0.8, 0.1)
			objectPlayAnimation('tdown', 'peel')
		end

		if noteData == 2 then
			setProperty('tapeup', true)
			doTweenAlpha('tweenuptape', 'tup', 0.8, 0.1)
			objectPlayAnimation('tup', 'peel')
		end

		if noteData == 3 then
			setProperty('taperight', true)
			doTweenAlpha('tweenrighttape', 'tright', 0.8, 0.1)
			objectPlayAnimation('tright', 'peel')
		end


		runTimer('ff', 3)

	end
end

function noteMiss(id, noteData, noteType, isSustainNote)
	if noteType == 'Tape Note' then
		
	end
end

function onUpdate()

if curStep == 615 then
	setProperty('pieces.alpha', 1)
	objectPlayAnimation('pieces', 'go')
end

if curStep == 625 then	
	setProperty('pieces.alpha', 0)
	setProperty('bubble.alpha', 1)
	objectPlayAnimation('bubble', 'go')

end

if curStep == 650 then
doTweenAlpha('bubblegone', 'bubble', 0, 0.3)
end

end

function onTimerCompleted(tag)
	if tag == 'ff' then		

		if getProperty('tapeleft') == true then
		setProperty('tapeleft', false)
		doTweenAlpha('goodbyetapeleft', 'tleft', 0, 0.3)
		end

		if getProperty('tapedown') == true then
		setProperty('tapedown', false)
		doTweenAlpha('goodbyetapedown', 'tdown', 0, 0.3)
		end

		if getProperty('tapeup') == true then
		setProperty('tapeup', false)
		doTweenAlpha('goodbyetapeup', 'tup', 0, 0.3)
		end

		if getProperty('taperight') == true then
		setProperty('taperight', false)
		doTweenAlpha('goodbyetaperight', 'tright', 0, 0.3)
		end		
	end

	if tag == 'yeawaitfordirections' then
	doTweenAlpha('directionsalpha', 'directions', 0, 1, quadInOut)	

	end
end

function onTweenCompleted(tag)

if tag == 'directionsalpha' then
runTimer('yeawaitfordirections', 6)
end

end