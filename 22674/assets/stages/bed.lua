function onCreate()
	-- background shit
	makeLuaSprite('bed', 'leroom/bed', -500, -200);
	setScrollFactor('bed', 0.9, 0.9);

	addLuaSprite('bed', false);
	
	close(true); --For performance reasons, close this script once the stage is fully loaded, as this script won't be used anymore after loading the stage
end