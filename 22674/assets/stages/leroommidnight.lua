function onCreate()
	-- background shit
	makeLuaSprite('lamp', 'leroom/lamp', -500, -200);
	setScrollFactor('lamp', 0.9, 0.9);

	makeLuaSprite('room', 'leroom/roommidnight', -500, -200);
	setScrollFactor('room', 0.9, 0.9);

	addLuaSprite('room', false);
	addLuaSprite('filter1', false);
	
	close(true); --For performance reasons, close this script once the stage is fully loaded, as this script won't be used anymore after loading the stage
end