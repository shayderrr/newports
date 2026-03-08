function onCreate()
    makeAnimatedLuaSprite('speaker', 'studio_speaker', -620, 200)
	luaSpriteAddAnimationByPrefix('speaker', 'idle', 'speaker', 24, true)
    setScrollFactor('speaker', 0.9, 0.9);
	
	makeAnimatedLuaSprite('speaker2', 'studio_speaker', 920, 200)
	luaSpriteAddAnimationByPrefix('speaker2', 'idle', 'speaker', 24, true)
    setScrollFactor('speaker2', 0.9, 0.9);
    setProperty('speaker2.flipX', true); --mirror sprite horizontally

	makeLuaSprite('studioback2','studio_evenfurtherback',-550,-200)
	setScrollFactor('studioback2', 0.5, 0.5);
	scaleObject('studioback2', 1.1, 1.1);
	
	makeLuaSprite('fx','studio_fx',-550,-200)
	setScrollFactor('fx', 0.5, 0.5);
	scaleObject('fx', 1.1, 1.1);
	
	makeLuaSprite('studioback','studio_back',-1300,-450)
	setScrollFactor('studioback', 0.9, 0.9);

    addLuaSprite('studioback2', false);
	addLuaSprite('fx', false);
    addLuaSprite('studioback', false);
	addLuaSprite('speaker', false);
	addLuaSprite('speaker2', false);
end

